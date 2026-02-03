#!/bin/bash

# Test script for Xiaohongshu MCP Server

echo "🧪 Testing Xiaohongshu MCP Server..."
echo "================================="

# Check if container is running
if docker ps | grep -q "xiaohongshu-mcp-server"; then
    echo "✅ Container is running"
    
    # Test basic connectivity
    echo "🌐 Testing connectivity..."
    if curl -s http://localhost:18060 > /dev/null; then
        echo "✅ Server is responding on port 18060"
    else
        echo "❌ Server is not responding"
        exit 1
    fi
    
    # Show container status
    echo ""
    echo "📊 Container Status:"
    docker ps --filter name=xiaohongshu-mcp-server --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"
    
    # Show logs (last 10 lines)
    echo ""
    echo "📋 Recent Logs:"
    docker logs --tail 10 xiaohongshu-mcp-server
    
    echo ""
    echo "🎉 Xiaohongshu MCP Server is running successfully!"
    echo "📡 MCP Server URL: http://localhost:18060"
    echo "🔧 Use 'docker compose logs -f' to view live logs"
    
else
    echo "❌ Container is not running"
    echo "💡 Run './start-server.sh' to start the server"
    exit 1
fi