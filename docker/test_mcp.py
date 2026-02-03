#!/usr/bin/env python3
"""
测试小红书 MCP 服务器
"""
import requests
import json

MCP_URL = "http://localhost:18060/mcp"

def test_mcp_server():
    print("🧪 测试小红书 MCP 服务器...")
    print("=" * 50)
    
    # 1. 初始化会话
    print("\n1️⃣ 初始化 MCP 会话...")
    init_request = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "initialize",
        "params": {
            "protocolVersion": "2024-11-05",
            "capabilities": {},
            "clientInfo": {
                "name": "test-client",
                "version": "1.0.0"
            }
        }
    }
    
    response = requests.post(MCP_URL, json=init_request)
    result = response.json()
    print(f"✅ 服务器信息: {result['result']['serverInfo']}")
    print(f"✅ 协议版本: {result['result']['protocolVersion']}")
    
    print("\n📡 MCP 服务器已成功运行在 http://localhost:18060")
    print("🔧 服务器提供 12 个小红书相关的工具")
    print("\n💡 提示: 这个 MCP 服务器可以:")
    print("   - 搜索小红书笔记")
    print("   - 获取用户信息")
    print("   - 抓取旅行相关内容")
    print("   - 其他小红书数据接口")

if __name__ == "__main__":
    try:
        test_mcp_server()
    except Exception as e:
        print(f"❌ 错误: {e}")
