from config import ALERT_INTERVAL

scheduler.add_job(
    send_alerts,
    "interval",
    minutes=ALERT_INTERVAL
)
