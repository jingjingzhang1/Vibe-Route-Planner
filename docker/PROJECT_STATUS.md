# 小红书 MCP 服务器 - 项目状态

## ✅ 当前状态

**服务器已成功运行！**

- **容器名称**: xiaohongshu-mcp-server
- **端口**: 18060
- **访问地址**: http://localhost:18060
- **状态**: 运行中 (Up 14 minutes)

## 📦 项目结构

```
rednote-mcp/
├── docker/
│   ├── docker-compose.yml      # Docker Compose 配置
│   ├── start-server.sh         # 启动脚本
│   └── test-server.sh          # 测试脚本
├── cookies.json                # 小红书登录 cookies
├── xiaohongshu-login-darwin-arm64   # 登录工具（macOS ARM64）
├── xiaohongshu-mcp-darwin-arm64     # MCP 服务器（macOS ARM64）
└── test_mcp.py                 # Python 测试脚本
```

## 🚀 如何使用

### 启动服务器
```bash
cd docker
./start-server.sh
```

### 停止服务器
```bash
cd docker
docker compose down
```

### 查看日志
```bash
docker logs -f xiaohongshu-mcp-server
```

### 测试服务器
```bash
./test-server.sh
# 或
python3 test_mcp.py
```

## 🔧 MCP 服务器功能

这个 MCP 服务器提供了 **12 个工具**，用于：
- 🔍 搜索小红书笔记
- 👤 获取用户信息
- ✈️ 抓取旅行相关内容
- 📊 其他小红书数据接口

## 🎯 下一步计划（基于你的旅行规划项目）

### Phase 1: 数据抓取
- [x] 设置小红书 MCP 服务器
- [ ] 实现基于关键词的笔记搜索
- [ ] 提取高浏览量博客的景点信息
- [ ] 二次验证景点信息（营业状态、最佳访问时间）

### Phase 2: 用户输入
- [ ] 设计用户偏好问卷
  - 旅行风格（休闲、打卡、摄影、运动等）
  - 时间范围
  - 目的地选项
  - 过敏信息等

### Phase 3: 路线规划
- [ ] 集成 Google Maps API（全球）
- [ ] 集成 Baidu Maps API（中国）
- [ ] 实现路线优化算法

### Phase 4: 输出生成
- [ ] 生成旅行计划文本
- [ ] 生成路线地图（JPG）
- [ ] 添加提醒事项和预订链接
- [ ] 支持 PDF 导出

## 📝 注意事项

1. **Cookies**: [cookies.json](cookies.json:1) 包含小红书的登录凭证，用于访问小红书 API
2. **Docker**: 使用 Docker 运行，支持跨平台
3. **端口**: 确保 18060 端口未被占用

## 🔗 参考资料

- GitHub 仓库: https://github.com/xpzouying/xiaohongshu-mcp
- MCP 协议: Model Context Protocol (2024-11-05)
