# 小红书内容抓取 API

通用的小红书笔记抓取工具，可以搜索任意关键词并提取笔记的标题和正文内容。

## 📋 目录

- [快速开始](#快速开始)
- [使用方法](#使用方法)
- [API 使用](#api-使用)
- [文件说明](#文件说明)
- [故障排查](#故障排查)

## 🚀 快速开始

### 首次使用

1. **启动 MCP 服务器**
   ```bash
   ./start.sh
   ```

2. **登录小红书账号**
   ```bash
   ./login.sh
   ```
   - 会生成 `qrcode.png` 二维码
   - 用小红书 APP 扫码登录
   - 登录成功后 cookies 会自动保存

3. **搜索并提取内容**
   ```bash
   python3 xiaohongshu_api.py "Tokyo Coffee" 10
   ```
   - 第一个参数：搜索关键词
   - 第二个参数：要提取的笔记数量（可选，默认10）

### 每次重新打开 VSCode

```bash
# 1. 启动服务器（如果没在运行）
./start.sh

# 2. 检查登录（如果 cookies 过期）
./login.sh

# 3. 开始使用
python3 xiaohongshu_api.py "你的搜索关键词" 10
```

## 📖 使用方法

### 基本用法

搜索单个关键词：
```bash
python3 xiaohongshu_api.py "东京咖啡" 15
```

搜索带空格的关键词：
```bash
python3 xiaohongshu_api.py "Tokyo Travel Guide" 10
```

### 输出文件

搜索结果会自动保存到文件，文件名根据关键词自动生成：
- 搜索 "Tokyo Coffee" → `tokyo_coffee_notes.txt`
- 搜索 "东京旅游" → `东京旅游_notes.txt`

### 输出格式

每条笔记包含：
- **标题**
- **正文内容**（包含地址、推荐理由、详细描述等）

示例：
```
====================================================================================================
笔记 1
====================================================================================================
标题: 东京·必打卡咖啡馆

☕️1. STREAMER COFFEE（图1-4）
世界拉花冠军泽田洋史开的店，主打一个拉花拿铁☕️
...
🏠：〒106-0032 Tokyo, Minato City, Roppongi, 6 Chome−11−16
====================================================================================================
```

## 💻 API 使用

### 在 Python 代码中使用

```python
from xiaohongshu_api import XiaohongshuAPI

# 创建 API 客户端
api = XiaohongshuAPI()

# 检查登录
if not api.check_login():
    print("请先登录")
    exit()

# 搜索笔记（只获取列表）
feeds = api.search("Tokyo Coffee", max_results=20)
print(f"找到 {len(feeds)} 条笔记")

# 获取单条笔记内容
note = api.get_note_content(feeds[0]['id'], feeds[0]['xsecToken'])
print(f"标题: {note['title']}")
print(f"内容: {note['content']}")

# 搜索并提取完整内容（推荐）
results = api.search_and_extract("东京美食", max_notes=10)
for note in results:
    print(note['title'])
    print(note['content'])
```

### API 方法

| 方法 | 说明 | 参数 | 返回值 |
|------|------|------|--------|
| `check_login()` | 检查登录状态 | 无 | bool |
| `search(keyword, max_results)` | 搜索笔记列表 | keyword: 关键词<br>max_results: 最大数量 | List[Dict] |
| `get_note_content(feed_id, xsec_token)` | 获取笔记详情 | feed_id: 笔记ID<br>xsec_token: 令牌 | Dict 或 None |
| `search_and_extract(keyword, max_notes, delay)` | 搜索并提取内容 | keyword: 关键词<br>max_notes: 数量<br>delay: 请求间隔 | List[Dict] |

## 📁 文件说明

### 核心文件
- `xiaohongshu_api.py` - 主要 API（**核心代码**）
- `start.sh` - 启动 MCP 服务器
- `login.sh` - 登录检查和二维码生成
- `stop.sh` - 停止服务器

### 配置文件
- `docker/docker-compose.yml` - Docker 配置
- `cookies.json` - 登录凭证（自动生成）

### 输出文件
- `*_notes.txt` - 提取的笔记内容
- `qrcode.png` - 登录二维码（临时）

## 🔧 故障排查

### 问题 1: 服务器无法启动

**症状**: 运行 `./start.sh` 失败

**解决方案**:
1. 确认 Docker 正在运行
2. 检查端口 18060 是否被占用：
   ```bash
   lsof -i :18060
   ```
3. 查看日志：
   ```bash
   docker logs xiaohongshu-mcp-server
   ```

### 问题 2: 登录失败或 cookies 过期

**症状**: 提示"未登录"

**解决方案**:
```bash
# 重新登录
./login.sh

# 扫码后，再次检查
./login.sh
```

### 问题 3: 搜索返回空结果

**可能原因**:
1. 关键词没有相关笔记
2. 网络连接问题
3. 被小红书限流

**解决方案**:
- 换个关键词试试
- 增加请求间隔（修改 `delay` 参数）
- 等待一段时间后重试

### 问题 4: 提取笔记失败

**症状**: 部分笔记显示 "❌ 获取失败"

**原因**: 
- API 限流
- 网络超时
- 笔记已删除

**解决方案**:
- 正常现象，忽略失败的笔记即可
- 减少 `max_notes` 数量
- 增加 `delay` 时间间隔

## 📌 使用建议

1. **首次使用**: 建议先搜索 5-10 条笔记测试
2. **批量抓取**: 建议每次不超过 20 条，避免被限流
3. **请求间隔**: 默认 1.5 秒，如果频繁失败可增加到 2-3 秒
4. **Cookies 管理**: 大约每周需要重新登录一次

## 🎯 使用场景

### 旅行规划
```bash
python3 xiaohongshu_api.py "东京美食推荐" 15
python3 xiaohongshu_api.py "京都住宿攻略" 10
python3 xiaohongshu_api.py "大阪购物清单" 10
```

### 咖啡店探索
```bash
python3 xiaohongshu_api.py "上海咖啡" 20
python3 xiaohongshu_api.py "北京精品咖啡" 15
```

### 产品调研
```bash
python3 xiaohongshu_api.py "iPhone 16 评测" 10
python3 xiaohongshu_api.py "护肤品推荐" 15
```

## 🔗 相关资源

- 原始 GitHub 仓库: https://github.com/xpzouying/xiaohongshu-mcp
- MCP 协议文档: Model Context Protocol

## ⚠️ 注意事项

1. **仅供学习研究**: 请遵守小红书的用户协议
2. **请求频率**: 不要过于频繁请求，避免被封号
3. **数据使用**: 抓取的数据仅供个人使用，请勿商业化
4. **隐私保护**: 不要抓取和传播用户隐私信息

## 📝 更新日志

### v1.0.0 (2026-01-20)
- ✅ 初始版本
- ✅ 支持任意关键词搜索
- ✅ 自动提取标题和正文
- ✅ 简化的启动流程
- ✅ 完整的错误处理
