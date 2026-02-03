#!/bin/bash
# 启动小红书 MCP 服务器

echo "🚀 启动小红书 MCP 服务器"
echo "================================================================================"

# 检查 Docker 是否运行
if ! docker info > /dev/null 2>&1; then
    echo "❌ Docker 未运行，请先启动 Docker"
    exit 1
fi

# 启动服务器
cd docker
docker compose up -d

sleep 5

# 检查状态
if docker ps | grep -q "xiaohongshu-mcp-server"; then
    echo "✅ 服务器已启动"
    echo "📡 MCP Server URL: http://localhost:18060"
    echo ""
    echo "下一步: 运行 ./login.sh 检查登录状态"
else
    echo "❌ 启动失败，查看日志:"
    docker logs xiaohongshu-mcp-server --tail 20
fi
