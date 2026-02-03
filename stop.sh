#!/bin/bash
# 停止小红书 MCP 服务器

echo "🛑 停止小红书 MCP 服务器"
echo "================================================================================"

cd docker
docker compose down

echo "✅ 服务器已停止"
