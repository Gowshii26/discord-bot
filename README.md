# Discord Bot

A feature-rich Discord bot built with Python using the discord.py library.

## Features

### Basic Commands
- `!hello` - Greet the user
- `!ping` - Check bot latency
- `!info` - Display bot information
- `!say <message>` - Make the bot say something
- `!userinfo [@user]` - Get user information
- `!serverinfo` - Get server information

### Fun Commands
- `!roll [sides]` - Roll a dice (default 6 sides)
- `!coinflip` - Flip a coin
- `!8ball <question>` - Ask the magic 8-ball
- `!choose <option1, option2, ...>` - Choose randomly from options
- `!joke` - Tell a random joke

### Moderation Commands (Requires Permissions)
- `!kick <@user> [reason]` - Kick a member
- `!ban <@user> [reason]` - Ban a member
- `!clear [amount]` - Clear messages (default 5)

## Setup

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Create Discord Application**
   - Go to [Discord Developer Portal](https://discord.com/developers/applications)
   - Create a new application
   - Go to the "Bot" section
   - Create a bot and copy the token

3. **Configure Environment**
   - Copy `.env.example` to `.env`
   - Add your bot token to the `.env` file:
     ```
     DISCORD_TOKEN=your_bot_token_here
     ```

4. **Invite Bot to Server**
   - Go to OAuth2 > URL Generator in Discord Developer Portal
   - Select "bot" scope
   - Select required permissions:
     - Send Messages
     - Read Message History
     - Embed Links
     - Manage Messages (for moderation)
     - Kick Members (for moderation)
     - Ban Members (for moderation)
   - Use the generated URL to invite the bot

5. **Run the Bot**
   ```bash
   python main.py
   ```
   
   Or run directly:
   ```bash
   python bot.py
   ```

## Project Structure

```
discord-bot/
├── bot.py              # Main bot file with basic commands
├── main.py             # Entry point with cog loading
├── requirements.txt    # Python dependencies
├── .env.example       # Environment variables template
├── .env               # Your environment variables (create this)
├── README.md          # This file
└── cogs/              # Command modules
    ├── moderation.py  # Moderation commands
    └── fun.py         # Fun commands
```

## Adding New Commands

To add new commands, you can either:

1. **Add to bot.py** for simple commands
2. **Create a new cog** in the `cogs/` directory for organized command groups

### Example Cog Structure

```python
import discord
from discord.ext import commands

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def mycommand(self, ctx):
        await ctx.send("Hello from my cog!")

async def setup(bot):
    await bot.add_cog(MyCog(bot))
```

## Permissions

The bot requires the following permissions:
- **Basic**: Send Messages, Read Message History, Embed Links
- **Moderation**: Manage Messages, Kick Members, Ban Members
- **Advanced**: Administrator (for full functionality)

## Support

For issues or questions:
1. Check the Discord.py documentation: https://discordpy.readthedocs.io/
2. Discord.py community: https://discord.gg/dpy
3. Discord Developer Portal: https://discord.com/developers/docs/