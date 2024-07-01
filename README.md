# Discord Bot README

## Introduction

Gym-Bot is a Discord Bot built using the `discord.py` library. The bot includes several commands to interact with users, such as listing commands, tracking workouts, and displaying user statistics.

The aim of this project is to motivate users to go to the gym as the "stats" page will always call out the user with the least gym trips.

## Prerequisites

- Python 3.8 or higher
- `discord.py` library
- `python-dotenv` library

## Setup

1. **Clone the repository:**

   ```sh
   git clone https://github.com/PIEALLDAYALLPIE/Gym-Bot.git
   ```

2. **Install dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

3. **Create a `.env` file in the root directory and add your Discord bot token:**

   ```env
   TOKEN=your_discord_bot_token
   ```

4. **Run the bot:**

   ```sh
   python bot.py
   ```
   or
   ```sh
   python3 bot.py
   ```

## Bot Commands

The bot supports the following commands:

### `/commands`
- **Description:** Lists all commands
- **Usage:** `/commands`

### `/ping`
- **Description:** Replies with "Pong!" and the bot's latency
- **Usage:** `/ping`

### `/set`
- **Description:** Set the number of workouts completed for a user
- **Usage:** `/set <member> <number>`

### `/jim`
- **Description:** Add a workout to the user's total
- **Usage:** `/jim`

### `/stats`
- **Description:** Shows total workouts per user
- **Usage:** `/stats`

### `/commandstack`
- **Description:** See the most recent commands used
- **Usage:** `/commandstack`

## Code Overview

The bot is built using the `discord.py` library and uses application commands (slash commands) to interact with users. The main functionalities are as follows:

- **Command Handling:** The bot uses `discord.ext.commands` for defining and handling commands.
- **Embeds:** The bot uses `discord.Embed` for rich-formatted responses.
- **Environment Variables:** The bot token is loaded from a `.env` file using the `dotenv` library.
- **Data Storage:** The bot keeps track of user statistics and recent commands using dictionaries and lists.

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.
