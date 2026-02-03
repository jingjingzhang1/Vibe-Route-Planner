#!/usr/bin/env python3
"""
解析并展示 Tokyo Coffee 搜索结果
"""
import json

# 读取结果文件
with open('tokyo_coffee_results.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 提取 feeds 数据
text_content = data['result']['content'][0]['text']
feeds_data = json.loads(text_content)
feeds = feeds_data['feeds']

print("=" * 100)
print(f"🍵 Tokyo Coffee 搜索结果 - 共找到 {feeds_data['count']} 条笔记")
print("=" * 100)
print()

# 过滤掉 hot_query 类型的项
actual_notes = [f for f in feeds if f['modelType'] == 'note']

for i, feed in enumerate(actual_notes, 1):
    note = feed.get('noteCard', {})
    
    print(f"【{i}】 {note.get('displayTitle', 'N/A')}")
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    
    # 用户信息
    user = note.get('user', {})
    print(f"👤 作者: {user.get('nickname', 'N/A')}")
    
    # 互动数据
    interact = note.get('interactInfo', {})
    print(f"❤️  点赞: {interact.get('likedCount', '0')}")
    print(f"💬 评论: {interact.get('commentCount', '0')}")
    print(f"⭐️ 收藏: {interact.get('collectedCount', '0')}")
    print(f"🔄 分享: {interact.get('sharedCount', '0')}")
    
    # 笔记信息
    print(f"🆔 笔记ID: {feed.get('id', 'N/A')}")
    print(f"🔑 访问令牌: {feed.get('xsecToken', 'N/A')[:20]}...")
    
    # 封面图片
    cover = note.get('cover', {})
    if cover.get('urlDefault'):
        print(f"📷 封面: {cover['urlDefault'][:80]}...")
    
    print()

print("=" * 100)
print("📊 统计信息")
print("=" * 100)
print(f"总笔记数: {len(actual_notes)}")
print(f"总点赞数: {sum(int(f.get('noteCard', {}).get('interactInfo', {}).get('likedCount', '0')) for f in actual_notes)}")
print(f"总收藏数: {sum(int(f.get('noteCard', {}).get('interactInfo', {}).get('collectedCount', '0')) for f in actual_notes)}")
print()

# 找出最受欢迎的笔记
sorted_feeds = sorted(actual_notes, 
                     key=lambda x: int(x.get('noteCard', {}).get('interactInfo', {}).get('likedCount', '0')), 
                     reverse=True)

print("🏆 TOP 5 最受欢迎的笔记:")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
for i, feed in enumerate(sorted_feeds[:5], 1):
    note = feed.get('noteCard', {})
    interact = note.get('interactInfo', {})
    print(f"{i}. {note.get('displayTitle')} - ❤️ {interact.get('likedCount')} 👤 {note.get('user', {}).get('nickname')}")

