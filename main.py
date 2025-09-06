import asyncio
import os
from bot import bot

async def load_cogs():
    """Load all cog files"""
    cogs = ['cogs.moderation', 'cogs.fun']
    
    for cog in cogs:
        try:
            await bot.load_extension(cog)
            print(f'✅ Loaded {cog}')
        except Exception as e:
            print(f'❌ Failed to load {cog}: {e}')

async def main():
    """Main function to start the bot"""
    await load_cogs()
    
    token = os.getenv('DISCORD_TOKEN')
    if not token:
        print("Error: DISCORD_TOKEN not found in environment variables!")
        print("Please create a .env file with your bot token.")
        return
    
    try:
        await bot.start(token)
    except Exception as e:
        print(f"Error starting bot: {e}")

if __name__ == "__main__":
    asyncio.run(main())