from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes
)

from config import BOT_TOKEN

from odds import fetch_odds

from database import engine

from models import Base


Base.metadata.create_all(
    engine
)


async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    await update.message.reply_text(
        """
⚽ Odds Bot Online

Commands:

/odds - View 2.00+ odds
"""
    )


async def odds(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    picks = fetch_odds()

    if not picks:

        await update.message.reply_text(
            "No odds found."
        )

        return


    message = "🔥 Today's Picks\n\n"


    for pick in picks:

        message += (
            f"⚽ {pick['event']}\n"
            f"📌 {pick['market']}\n"
            f"💰 Odds: {pick['odds']}\n\n"
        )


    await update.message.reply_text(
        message
    )



app = Application.builder()\
    .token(BOT_TOKEN)\
    .build()


app.add_handler(
    CommandHandler(
        "start",
        start
    )
)


app.add_handler(
    CommandHandler(
        "odds",
        odds
    )
)


print(
    "Bot running..."
)


app.run_polling()
