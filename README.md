# Telegram Channels Export Script

This python script allows you to export all the Telegram channels you are a member of, including both public and private channels. The output will contain the channel name, ID, username (if available), and a direct link to the channel.

## Features
- ✅ Exports **all** channels (public & private)
- ✅ Saves **channel name, ID, username, and link**
- ✅ Outputs data in a **CSV file** for easy use
- ✅ Improved error handling and logging
- ✅ Reusable without needing to log in again

## Prerequisites
1. **Get Telegram API Credentials**
   - Go to [my.telegram.org](https://my.telegram.org/)
   - Log in and navigate to **API Development Tools**
   - Create a new application and copy your `api_id` and `api_hash`

2. **Install Dependencies**
   - Install `Telethon`, a Telegram API library for Python:
     ```bash
     pip install telethon
     ```

## Usage
1. **Clone this repository**:
   ```bash
   git clone https://github.com/fd2013/telegram-channels-export.git
   cd telegram-channels-export
   ```

2. **Edit the script to add your API credentials**:
   - Open `telegram_channel_export.py` in a text editor.
   - Replace the placeholders with your **API ID** and **API Hash**:
     ```python
     API_ID = YOUR_API_ID  # Example: 123456
     API_HASH = "YOUR_API_HASH"  # Example: "abcdef1234567890abcdef1234567890"
     ```

3. **Run the script**:
   ```bash
   python telegram_channel_export.py
   ```

4. **Login**
   - The first time you run the script, you'll need to enter your **Telegram phone number**.
   - A **verification code** will be sent to Telegram—enter it in the terminal.

5. **Check the exported file**:
   - After running, a file called `telegram_channels.csv` will be created, containing:
     ```csv
     Channel Name,Channel ID,Username,Channel Link
     Crypto News,123456789,cryptonews,https://t.me/cryptonews
     Private Group A,987654321,Private,Private
     Tech Updates,567890123,techupdates,https://t.me/techupdates
     ```

## Notes
- **Public channels** will have a clickable link in the format `https://t.me/username`.
- **Private channels** do not have usernames and will be labeled as `"Private"` in the link column.
- The script creates a session file (`telegram_channel_export.session`), so you **don’t need to log in every time**.
- If you have **Two-Step Verification (2FA) enabled**, the script will prompt you for your password.
- If you want to log in with a new account, delete the `.session` file and rerun the script.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contribution
Feel free to contribute! Open an issue or submit a pull request.

