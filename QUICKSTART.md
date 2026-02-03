# Quick Start Guide

## 3 Steps to Get Started

### Step 1: Start the Server
```bash
./start.sh
```

Wait 5 seconds, when you see "✅ Server started", you're ready.

### Step 2: Login
```bash
./login.sh
```

- If it shows "✅ Logged in" → Skip to Step 3
- If it shows "❌ Not logged in" → A QR code will be generated, scan it with the Xiaohongshu app

### Step 3: Search
```bash
python3 xiaohongshu_api.py "Tokyo Coffee" 10
```

Results will be saved to `tokyo_coffee_notes.txt`

---

## Common Use Cases

### Search Travel Information
```bash
python3 xiaohongshu_api.py "Tokyo Travel Guide" 15
python3 xiaohongshu_api.py "Kyoto Cherry Blossoms" 10
```

### Search Food
```bash
python3 xiaohongshu_api.py "Shanghai Michelin" 10
python3 xiaohongshu_api.py "Chengdu Hot Pot" 15
```

### Search Shopping
```bash
python3 xiaohongshu_api.py "Japan Drugstore Recommendations" 10
```

---

## Next Time You Use

Each time you reopen VSCode:

```bash
# 1. Start the server (if Docker was closed)
./start.sh

# 2. Check login (usually not needed)
./login.sh

# 3. Start searching
python3 xiaohongshu_api.py "keyword" 10
```

---

## Stop the Server

```bash
./stop.sh
```

---

## Having Issues?

Check the complete documentation: [README.md](README.md)
