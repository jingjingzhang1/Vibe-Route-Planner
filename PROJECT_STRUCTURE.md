# 项目结构

```
rednote-mcp/
├── README.md                      # 完整文档
├── QUICKSTART.md                  # 快速开始指南
├── xiaohongshu_api.py            # 核心 API（主要代码）
├── start.sh                       # 启动 MCP 服务器
├── login.sh                       # 登录检查和二维码生成
├── stop.sh                        # 停止服务器
├── cookies.json                   # 登录凭证（自动生成）
├── docker/
│   ├── docker-compose.yml        # Docker 配置
│   └── start-server.sh           # Docker 启动脚本
├── tokyo_coffee_clean.txt        # 示例输出（Tokyo Coffee）
└── 东京咖啡_notes.txt             # 测试输出
```

## 核心文件说明

### xiaohongshu_api.py
主要的 Python API，包含：
- `XiaohongshuAPI` 类
- `check_login()` - 检查登录
- `search()` - 搜索笔记列表
- `get_note_content()` - 获取单条笔记
- `search_and_extract()` - 搜索并提取完整内容

### start.sh
一键启动 Docker 容器，运行 MCP 服务器

### login.sh
检查登录状态，如果未登录则生成二维码

### stop.sh
停止 Docker 容器

## 输出文件

每次搜索会生成一个文件，文件名格式：
- `{关键词}_notes.txt`

例如：
- `tokyo_coffee_notes.txt`
- `东京旅游_notes.txt`

## 不需要的文件

以下文件可以删除（已在 .gitignore 中）：
- `*_notes.txt` - 输出文件
- `qrcode.png` - 临时二维码
- `tokyo_coffee_results.json` - 原始搜索结果
