#!/usr/bin/env python3
"""
小红书内容抓取 API
支持搜索任意关键词并提取笔记的标题和正文
"""
import requests
import json
import time
import sys
from typing import List, Dict, Optional

class XiaohongshuAPI:
    """小红书 MCP API 客户端"""
    
    def __init__(self, mcp_url: str = "http://localhost:18060/mcp"):
        self.mcp_url = mcp_url
        self.session_id = None
        
    def _init_session(self) -> str:
        """初始化 MCP 会话"""
        response = requests.post(self.mcp_url, json={
            "jsonrpc": "2.0",
            "id": 1,
            "method": "initialize",
            "params": {
                "protocolVersion": "2024-11-05",
                "capabilities": {},
                "clientInfo": {"name": "xiaohongshu-api", "version": "1.0"}
            }
        })
        
        self.session_id = response.headers.get('Mcp-Session-Id')
        
        # 发送初始化完成通知
        requests.post(
            self.mcp_url,
            headers={'Mcp-Session-Id': self.session_id},
            json={"jsonrpc": "2.0", "method": "notifications/initialized"}
        )
        
        time.sleep(1)
        return self.session_id
    
    def check_login(self) -> bool:
        """检查登录状态"""
        if not self.session_id:
            self._init_session()
            
        response = requests.post(
            self.mcp_url,
            headers={'Mcp-Session-Id': self.session_id},
            json={
                "jsonrpc": "2.0",
                "id": 2,
                "method": "tools/call",
                "params": {
                    "name": "check_login_status",
                    "arguments": {}
                }
            }
        )
        
        result = response.json()
        if 'result' in result and 'content' in result['result']:
            text = result['result']['content'][0]['text']
            return "✅" in text or "已登录" in text
        return False
    
    def search(self, keyword: str, max_results: int = 20) -> List[Dict]:
        """
        搜索小红书笔记
        
        Args:
            keyword: 搜索关键词
            max_results: 最大返回结果数
            
        Returns:
            包含笔记基本信息的列表
        """
        if not self.session_id:
            self._init_session()
            
        response = requests.post(
            self.mcp_url,
            headers={'Mcp-Session-Id': self.session_id},
            json={
                "jsonrpc": "2.0",
                "id": 3,
                "method": "tools/call",
                "params": {
                    "name": "search_feeds",
                    "arguments": {
                        "keyword": keyword,
                        "filters": {"sort_by": "综合"}
                    }
                }
            }
        )
        
        result = response.json()
        
        if 'result' not in result or 'content' not in result['result']:
            return []
            
        text = result['result']['content'][0]['text']
        feeds_data = json.loads(text)
        feeds = [f for f in feeds_data['feeds'] if f.get('modelType') == 'note']
        
        return feeds[:max_results]
    
    def get_note_content(self, feed_id: str, xsec_token: str, timeout: int = 30) -> Optional[Dict]:
        """
        获取笔记详细内容

        Args:
            feed_id: 笔记ID
            xsec_token: 访问令牌
            timeout: 请求超时时间（秒）

        Returns:
            包含标题和内容的字典，或 None
        """
        if not self.session_id:
            self._init_session()

        try:
            response = requests.post(
                self.mcp_url,
                headers={'Mcp-Session-Id': self.session_id},
                json={
                    "jsonrpc": "2.0",
                    "id": 4,
                    "method": "tools/call",
                    "params": {
                        "name": "get_feed_detail",
                        "arguments": {
                            "feed_id": feed_id,
                            "xsec_token": xsec_token
                        }
                    }
                },
                timeout=timeout
            )

            result = response.json()

            if 'result' not in result or 'content' not in result['result']:
                return None

            text = result['result']['content'][0]['text']
            detail_data = json.loads(text)

            return {
                'title': detail_data['data']['note']['title'],
                'content': detail_data['data']['note']['desc']
            }

        except requests.exceptions.Timeout:
            print(f"⏱️  请求超时 (>{timeout}秒)", file=sys.stderr)
            return None
        except Exception as e:
            print(f"获取笔记详情失败: {e}", file=sys.stderr)
            return None
    
    def search_and_extract(
        self, 
        keyword: str, 
        max_notes: int = 10,
        delay: float = 1.5
    ) -> List[Dict]:
        """
        搜索并提取笔记完整内容
        
        Args:
            keyword: 搜索关键词
            max_notes: 要提取的笔记数量
            delay: 每次请求间隔（秒）
            
        Returns:
            包含标题和内容的笔记列表
        """
        print(f"🔍 搜索关键词: {keyword}")
        
        # 1. 搜索笔记
        feeds = self.search(keyword, max_notes)
        print(f"✅ 找到 {len(feeds)} 条笔记")
        
        # 2. 提取详细内容
        results = []
        for i, feed in enumerate(feeds, 1):
            print(f"[{i}/{len(feeds)}] 获取笔记内容...")
            
            note = self.get_note_content(feed['id'], feed['xsecToken'])
            if note:
                results.append(note)
                print(f"   ✅ {note['title'][:40]}...")
            else:
                print(f"   ❌ 获取失败")
                
            if i < len(feeds):
                time.sleep(delay)
        
        return results


def main():
    """命令行入口"""
    if len(sys.argv) < 2:
        print("用法: python3 xiaohongshu_api.py <关键词> [笔记数量]")
        print("示例: python3 xiaohongshu_api.py 'Tokyo Coffee' 10")
        sys.exit(1)
    
    keyword = sys.argv[1]
    max_notes = int(sys.argv[2]) if len(sys.argv) > 2 else 10
    
    # 创建API客户端
    api = XiaohongshuAPI()
    
    # 检查登录
    print("🔐 检查登录状态...")
    if not api.check_login():
        print("❌ 未登录！请先运行 ./login.sh 扫码登录")
        sys.exit(1)
    print("✅ 已登录\n")
    
    # 搜索并提取内容
    results = api.search_and_extract(keyword, max_notes)
    
    # 保存结果
    output_file = f"{keyword.replace(' ', '_').lower()}_notes.txt"
    with open(output_file, 'w', encoding='utf-8') as f:
        for i, note in enumerate(results, 1):
            content = f"\n{'=' * 100}\n"
            content += f"笔记 {i}\n"
            content += f"{'=' * 100}\n"
            content += f"标题: {note['title']}\n\n"
            content += f"{note['content']}\n"
            content += f"{'=' * 100}\n"
            f.write(content)
    
    print(f"\n✅ 完成！共提取 {len(results)} 条笔记")
    print(f"💾 内容已保存到: {output_file}")


if __name__ == "__main__":
    main()
