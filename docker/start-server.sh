#!/bin/bash

# Xiaohongshu MCP Server Docker Setup Script

echo "🔥 Starting Xiaohongshu MCP Server..."

# Check if Docker is running
if ! docker info > /dev/null 2>&1; then
    echo "❌ Docker is not running. Please start Docker first."
    exit 1
fi

# Option 1: Run with Docker Compose (recommended)
echo "📦 Starting with Docker Compose..."
docker compose up -d

# Wait a moment for the container to start
sleep 5

# Check if container is running
if docker ps | grep -q "xiaohongshu-mcp-server"; then
    echo "✅ Xiaohongshu MCP Server is running!"
    echo "🌐 Server is accessible at: http://localhost:18060"
    echo "📋 Container name: xiaohongshu-mcp-server"
    echo ""
    echo "🔧 Useful commands:"
    echo "  - View logs: docker compose logs -f"
    echo "  - Stop server: docker compose down"
    echo "  - Restart server: docker compose restart"
    echo ""
else
    echo "❌ Failed to start the container. Checking logs..."
    docker compose logs
fi