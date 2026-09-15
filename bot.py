import os
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("8926598009:AAEQX4HlX7ABl5l0vjHOReB-lgwaHglnZU8", "").strip()

if not BOT_TOKEN:
    raise RuntimeError("Missing BOT_TOKEN environment variable.")

running = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 KunZ Telegram Bot\n\n"
        "Lệnh:\n"
        "/help - Xem hướng dẫn\n"
        "/status - Xem trạng thái\n"
        "/config - Xem cấu hình\n"
        "/run - Chạy tác vụ an toàn\n"
        "/stop - Dừng tác vụ"
    )

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📖 HƯỚNG DẪN\n\n"
        "/start — Khởi động bot\n"
        "/status — Kiểm tra bot\n"
        "/config — Xem cấu hình môi trường\n"
        "/run — Chạy tác vụ mẫu\n"
        "/stop — Dừng tác vụ đang chạy"
    )

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid = update.effective_user.id
    state = "🟢 Đang chạy" if running.get(uid) else "⚪ Đang chờ"
    await update.message.reply_text(f"📊 Trạng thái: {state}")

async def config(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "⚙️ CONFIG\n"
        f"API_URL: {os.getenv('API_URL', 'chưa đặt')}\n"
        "BOT_TOKEN: đã được nạp từ GitHub Secret\n\n"
        "Không hiển thị token để tránh lộ thông tin."
    )

async def run_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid = update.effective_user.id
    if running.get(uid):
        await update.message.reply_text("⚠️ Tác vụ của bạn đang chạy.")
        return

    running[uid] = True
    await update.message.reply_text(
        "▶️ Đã bắt đầu tác vụ.\n"
        "Đây là khung bot an toàn; không tự động tạo tài khoản hàng loạt."
    )

async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid = update.effective_user.id
    running[uid] = False
    await update.message.reply_text("⏹️ Đã dừng tác vụ.")

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CommandHandler("status", status))
    app.add_handler(CommandHandler("config", config))
    app.add_handler(CommandHandler("run", run_cmd))
    app.add_handler(CommandHandler("stop", stop))

    print("KunZ Telegram Bot is running...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
