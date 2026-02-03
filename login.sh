#!/bin/bash
# 检查登录状态并提供登录二维码

echo "🔐 小红书登录检查"
echo "================================================================================"

# 初始化会话
INIT_RESPONSE=$(curl -s -i -X POST http://localhost:18060/mcp \
  -H 'Content-Type: application/json' \
  -d '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"login","version":"1.0"}}}')

SESSION_ID=$(echo "$INIT_RESPONSE" | grep -i "Mcp-Session-Id:" | cut -d' ' -f2 | tr -d '\r')

# 发送初始化通知
curl -s -X POST http://localhost:18060/mcp \
  -H 'Content-Type: application/json' \
  -H "Mcp-Session-Id: $SESSION_ID" \
  -d '{"jsonrpc":"2.0","method":"notifications/initialized"}' > /dev/null

sleep 1

# 检查登录状态
echo "检查登录状态..."
RESULT=$(curl -s -X POST http://localhost:18060/mcp \
  -H 'Content-Type: application/json' \
  -H "Mcp-Session-Id: $SESSION_ID" \
  -d '{"jsonrpc":"2.0","id":2,"method":"tools/call","params":{"name":"check_login_status","arguments":{}}}')

if echo "$RESULT" | grep -q "已登录"; then
    echo "✅ 已登录！可以开始使用了。"
    exit 0
fi

echo "❌ 未登录"
echo ""
echo "正在生成登录二维码..."

# 获取二维码
QR_RESULT=$(curl -s -X POST http://localhost:18060/mcp \
  -H 'Content-Type: application/json' \
  -H "Mcp-Session-Id: $SESSION_ID" \
  -d '{"jsonrpc":"2.0","id":3,"method":"tools/call","params":{"name":"get_login_qrcode","arguments":{}}}')

# 提取并保存二维码
echo "$QR_RESULT" | python3 -c "
import sys, json
data = json.load(sys.stdin)
if 'result' in data and 'content' in data['result']:
    for item in data['result']['content']:
        if item.get('type') == 'image':
            print(item.get('data', ''))
            break
" 2>/dev/null | base64 -d > qrcode.png 2>/dev/null

if [ -f qrcode.png ]; then
    echo "✅ 二维码已生成: qrcode.png"
    echo ""
    echo "📱 请用小红书 APP 扫描二维码登录"
    echo ""
    open qrcode.png 2>/dev/null || echo "请手动打开 qrcode.png"
    echo ""
    echo "登录后，重新运行 ./login.sh 检查状态"
else
    echo "❌ 生成二维码失败"
fi
