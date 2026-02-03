# 快速开始指南

## 3 步开始使用

### 第 1 步：启动服务器
```bash
./start.sh
```

等待 5 秒，看到 "✅ 服务器已启动" 即可。

### 第 2 步：登录
```bash
./login.sh
```

- 如果显示 "✅ 已登录" → 跳到第 3 步
- 如果显示 "❌ 未登录" → 会生成二维码，用小红书 APP 扫码

### 第 3 步：搜索
```bash
python3 xiaohongshu_api.py "Tokyo Coffee" 10
```

结果会保存到 `tokyo_coffee_notes.txt`

---

## 常见用法

### 搜索旅游信息
```bash
python3 xiaohongshu_api.py "东京旅游攻略" 15
python3 xiaohongshu_api.py "京都赏樱" 10
```

### 搜索美食
```bash
python3 xiaohongshu_api.py "上海米其林" 10
python3 xiaohongshu_api.py "成都火锅" 15
```

### 搜索购物
```bash
python3 xiaohongshu_api.py "日本药妆推荐" 10
```

---

## 下次使用

每次重新打开 VSCode：

```bash
# 1. 启动服务器（如果 Docker 关闭了）
./start.sh

# 2. 检查登录（通常不需要）
./login.sh

# 3. 开始搜索
python3 xiaohongshu_api.py "关键词" 10
```

---

## 停止服务器

```bash
./stop.sh
```

---

## 遇到问题？

查看完整文档: [README.md](README.md)
