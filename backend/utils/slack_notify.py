import os
import requests

SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")

def send_slack_ping(llm_name, question=None):
    if not SLACK_WEBHOOK_URL:
        return
    message = f":rotating_light: ClubOS Lite pinged by *{llm_name}*"
    if question:
        message += f"\n> {question[:200]}"
    try:
        requests.post(SLACK_WEBHOOK_URL, json={"text": message})
    except Exception as e:
        print(f"[Slack ping failed] {e}")