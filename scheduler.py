from telegram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from config import BOT_TOKEN

from database import SessionLocal

from models import Subscriber

from odds import fetch_odds



bot = Bot(
    token=BOT_TOKEN
)



async def send_alerts():

    picks = fetch_odds()


    if not picks:
        return


    message = "🔥 New 2.00+ Odds Alert\n\n"


    for pick in picks:

        message += (
            f"⚽ {pick['event']}\n"
            f"📌 {pick['market']}\n"
            f"💰 Odds: {pick['odds']}\n\n"
        )


    db = SessionLocal()


    users = db.query(
        Subscriber
    ).all()


    for user in users:

        try:

            await bot.send_message(
                chat_id=user.telegram_id,
                text=message
            )

        except Exception:

            pass


    db.close()



def start_scheduler():

    scheduler = AsyncIOScheduler()


    scheduler.add_job(
        send_alerts,
        "interval",
        minutes=30
    )


    scheduler.start()
