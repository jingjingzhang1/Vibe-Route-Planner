# Xiaohongshu MCP Server - Project Status

## ✅ Current Status

**Server is running successfully!**

- **Container name**: xiaohongshu-mcp-server
- **Port**: 18060
- **Access URL**: http://localhost:18060
- **Status**: Running (Up 14 minutes)

## 📦 Project Structure

```
rednote-mcp/
├── docker/
│   ├── docker-compose.yml      # Docker Compose configuration
│   ├── start-server.sh         # Startup script
│   └── test-server.sh          # Test script
├── cookies.json                # Xiaohongshu login cookies
├── xiaohongshu-login-darwin-arm64   # Login tool (macOS ARM64)
├── xiaohongshu-mcp-darwin-arm64     # MCP server (macOS ARM64)
└── test_mcp.py                 # Python test script
```

## 🚀 How to Use

### Start Server
```bash
cd docker
./start-server.sh
```

### Stop Server
```bash
cd docker
docker compose down
```

### View Logs
```bash
docker logs -f xiaohongshu-mcp-server
```

### Test Server
```bash
./test-server.sh
# or
python3 test_mcp.py
```

## 🔧 MCP Server Features

This MCP server provides **12 tools** for:
- 🔍 Searching Xiaohongshu notes
- 👤 Getting user information
- ✈️ Scraping travel-related content
- 📊 Other Xiaohongshu data interfaces

## 🎯 Next Steps (Based on Your Travel Planning Project)

### Phase 1: Data Scraping
- [x] Set up Xiaohongshu MCP server
- [ ] Implement keyword-based note search
- [ ] Extract scenic spot information from high-view blogs
- [ ] Secondary verification of scenic spot info (operating status, best visit times)

### Phase 2: User Input
- [ ] Design user preference questionnaire
  - Travel style (leisure, sightseeing, photography, sports, etc.)
  - Time range
  - Destination options
  - Allergy information, etc.

### Phase 3: Route Planning
- [ ] Integrate Google Maps API (global)
- [ ] Integrate Baidu Maps API (China)
- [ ] Implement route optimization algorithm

### Phase 4: Output Generation
- [ ] Generate travel plan text
- [ ] Generate route map (JPG)
- [ ] Add reminders and booking links
- [ ] Support PDF export

## 📝 Notes

1. **Cookies**: [cookies.json](cookies.json:1) contains Xiaohongshu login credentials for API access
2. **Docker**: Uses Docker for cross-platform support
3. **Port**: Ensure port 18060 is not occupied

## 🔗 References

- GitHub repository: https://github.com/xpzouying/xiaohongshu-mcp
- MCP protocol: Model Context Protocol (2024-11-05)
