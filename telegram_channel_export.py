import csv
import logging
from telethon.sync import TelegramClient
from telethon.errors import SessionPasswordNeededError

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(message)s")

# Replace with your Telegram API credentials
API_ID = YOUR_API_ID  # Example: 123456
API_HASH = "YOUR_API_HASH"  # Example: "abcdef1234567890abcdef1234567890"
SESSION_NAME = "telegram_channel_export"

# Output file
OUTPUT_FILE = "telegram_channels.csv"

def main():
    """Exports Telegram channels to a CSV file including channel links."""
    try:
        with TelegramClient(SESSION_NAME, API_ID, API_HASH) as client:
            logging.info("✅ Connected to Telegram. Fetching channels...")

            channels = []
            for dialog in client.iter_dialogs():
                if dialog.is_channel:
                    username = dialog.entity.username
                    if username:
                        link = f"https://t.me/{username}"
                    else:
                        link = "Private"

                    channels.append([
                        dialog.title, 
                        dialog.entity.id, 
                        username or "Private", 
                        link
                    ])

            if not channels:
                logging.info("⚠️ No channels found!")
                return

            # Save to CSV
            with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["Channel Name", "Channel ID", "Username", "Channel Link"])
                writer.writerows(channels)

            logging.info(f"✅ Export completed! Channels saved in '{OUTPUT_FILE}'")

    except SessionPasswordNeededError:
        logging.error("⚠️ Two-Step Verification is enabled. Please provide your password.")
    except Exception as e:
        logging.error(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    main()
