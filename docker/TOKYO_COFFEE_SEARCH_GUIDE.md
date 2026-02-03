# Tokyo Coffee 搜索指南

## 当前状态

✅ 小红书 MCP 服务器已启动
✅ Docker 容器运行正常
❌ 需要登录小红书账号才能搜索

## 登录步骤

### 方法 1: 扫描二维码登录（推荐）

1. **已生成二维码**: `qrcode.png`
2. **登录步骤**:
   - 打开小红书 APP
   - 点击右下角「我」
   - 点击右上角扫一扫图标
   - 扫描 `qrcode.png` 中的二维码
   - 在手机上确认登录

3. **登录后检查**:
   ```bash
   ./check_login.sh
   ```

### 方法 2: 使用本地登录工具

你的项目里有 `xiaohongshu-login-darwin-arm64` 可执行文件，可以直接运行：
```bash
./xiaohongshu-login-darwin-arm64
```

## 搜索 Tokyo Coffee

登录成功后，运行：
```bash
./search_tokyo_coffee_final.sh
```

这个脚本会：
1. 初始化 MCP 会话
2. 发送初始化通知
3. 搜索「Tokyo Coffee」
4. 保存结果到 `tokyo_coffee_results.json`

## 搜索结果格式

搜索结果将包含：
- 笔记标题
- 笔记内容
- 作者信息
- 点赞/收藏/评论数
- 笔记 ID 和访问令牌（用于获取详情）
- 发布时间
- 笔记类型（图文/视频）

## 可用的搜索选项

搜索时可以添加筛选条件：

```json
{
  "filters": {
    "sort_by": "综合|最新|最多点赞|最多评论|最多收藏",
    "note_type": "不限|视频|图文",
    "publish_time": "不限|一天内|一周内|半年内",
    "location": "不限|同城|附近",
    "search_scope": "不限|已看过|未看过|已关注"
  }
}
```

## 下一步：为旅行规划项目使用数据

登录并成功搜索后，你可以：

1. **搜索特定城市的咖啡店**:
   ```bash
   # 修改搜索关键词
   keyword="东京咖啡" 或 "Tokyo cafe"
   ```

2. **获取笔记详情**:
   - 从搜索结果中提取 `feed_id` 和 `xsec_token`
   - 使用 `get_feed_detail` 工具获取完整内容

3. **批量抓取数据**:
   - 循环搜索不同关键词
   - 提取景点、餐厅、咖啡店信息
   - 分析评论和互动数据

## 脚本列表

- `check_login.sh` - 检查登录状态
- `get_qrcode.sh` - 获取登录二维码
- `search_tokyo_coffee_final.sh` - 搜索 Tokyo Coffee
- `get_all_tools.sh` - 查看所有可用工具

## 故障排查

### 问题 1: cookies 过期
**解决方案**: 重新扫码登录

### 问题 2: 搜索返回空结果
**检查**:
1. 是否已登录（运行 `check_login.sh`）
2. 关键词是否正确
3. 网络连接是否正常

### 问题 3: 容器无法启动
**检查**:
```bash
docker ps -a
docker logs xiaohongshu-mcp-server
```

## 文件说明

- `qrcode.png` - 登录二维码图片
- `cookies.json` - 登录凭证（由挂载的 volume 自动更新）
- `tokyo_coffee_results.json` - 搜索结果（尚未生成）
- `docker/docker-compose.yml` - 已更新，包含 cookies volume 挂载

