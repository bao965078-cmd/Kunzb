# KunZ Telegram Bot

## 1. Upload these files to GitHub

- `bot.py`
- `requirements.txt`
- `.github/workflows/bot.yml`

## 2. Add Telegram token

GitHub repository:
Settings → Secrets and variables → Actions → New repository secret

Name:
`BOT_TOKEN`

Value:
Token lấy từ BotFather.

Có thể thêm:
`API_URL`

## 3. Chạy

Vào:
Actions → KunZ Telegram Bot → Run workflow

Bot hỗ trợ:
`/start`
`/help`
`/status`
`/config`
`/run`
`/stop`

Không đưa BOT_TOKEN trực tiếp vào code hoặc commit lên GitHub.
