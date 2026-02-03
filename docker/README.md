# Xiaohongshu MCP Server

This directory contains the setup for running the Xiaohongshu (RedNote) MCP (Model Context Protocol) server using Docker.

## Quick Start

### Method 1: Using Docker Compose (Recommended)

1. Start the server:
   ```bash
   chmod +x start-server.sh
   ./start-server.sh
   ```

2. Or manually:
   ```bash
   docker compose up -d
   ```

### Method 2: Using Docker Run

```bash
docker run -d \
  --name xiaohongshu-mcp-server \
  --platform linux/amd64 \
  -p 18060:18060 \
  -e TZ=Asia/Shanghai \
  -e ROD_BROWSER_BIN=/usr/bin/google-chrome \
  xpzouying/xiaohongshu-mcp:latest
```

## Server Information

- **Port**: 18060
- **Container Name**: xiaohongshu-mcp-server
- **Platform**: linux/amd64 (for Mac compatibility)
- **Server URL**: http://localhost:18060

## Management Commands

### View Logs
```bash
# With Docker Compose
docker compose logs -f

# With Docker
docker logs -f xiaohongshu-mcp-server
```

### Stop Server
```bash
# With Docker Compose
docker compose down

# With Docker
docker stop xiaohongshu-mcp-server
```

### Restart Server
```bash
# With Docker Compose
docker compose restart

# With Docker
docker restart xiaohongshu-mcp-server
```

### Remove Container
```bash
# With Docker Compose
docker compose down --volumes

# With Docker
docker rm -f xiaohongshu-mcp-server
```

## Troubleshooting

1. **Container won't start**: Check Docker logs with `docker compose logs`
2. **Port conflict**: Change the port mapping in `docker-compose.yml` if port 18060 is already in use
3. **Performance issues**: This runs AMD64 image on ARM Mac with emulation, which may be slower

## What is MCP?

Model Context Protocol (MCP) is a protocol that allows AI models to securely access external data sources and tools. This server provides integration with Xiaohongshu (RedNote) services.