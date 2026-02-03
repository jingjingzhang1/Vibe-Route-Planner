#!/bin/bash

echo "================================================================================"
echo "🔐 获取小红书登录二维码"
echo "================================================================================"

# Initialize
INIT_RESPONSE=$(curl -s -i -X POST http://localhost:18060/mcp \
  -H 'Content-Type: application/json' \
  -d '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"login","version":"1.0"}}}')

SESSION_ID=$(echo "$INIT_RESPONSE" | grep -i "Mcp-Session-Id:" | cut -d' ' -f2 | tr -d '\r')

# Send initialized notification
curl -s -X POST http://localhost:18060/mcp \
  -H 'Content-Type: application/json' \
  -H "Mcp-Session-Id: $SESSION_ID" \
  -d '{"jsonrpc":"2.0","method":"notifications/initialized"}' > /dev/null

sleep 1

# Get QR code
echo "正在获取二维码..."
RESULT=$(curl -s -X POST http://localhost:18060/mcp \
  -H 'Content-Type: application/json' \
  -H "Mcp-Session-Id: $SESSION_ID" \
  -d '{"jsonrpc":"2.0","id":2,"method":"tools/call","params":{"name":"get_login_qrcode","arguments":{}}}')

# Extract base64 image
BASE64_IMAGE=$(echo "$RESULT" | python3 -c "
import sys, json
data = json.load(sys.stdin)
if 'result' in data and 'content' in data['result']:
    for item in data['result']['content']:
        if item.get('type') == 'image':
            print(item.get('data', ''))
            break
" 2>/dev/null)

if [ -n "$BASE64_IMAGE" ]; then
    echo "✅ 二维码已生成!"
    echo "$BASE64_IMAGE" | base64 -d > qrcode.png 2>/dev/null
    
    if [ -f qrcode.png ]; then
        echo "💾 二维码已保存到: qrcode.png"
        echo ""
        echo "📱 请用小红书 APP 扫描 qrcode.png 文件中的二维码登录"
        echo ""
        echo "打开二维码图片："
        open qrcode.png 2>/dev/null || echo "请手动打开 qrcode.png"
    else
        echo "保存失败，显示原始结果："
        echo "$RESULT" | python3 -m json.tool
    fi
else
    echo "获取二维码失败，显示原始结果："
    echo "$RESULT" | python3 -m json.tool
fi

