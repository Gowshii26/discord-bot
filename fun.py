import discord
from discord.ext import commands
import random

class Fun(commands.Cog):
    """Fun commands for entertainment"""
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='roll')
    async def roll(self, ctx, sides: int = 6):
        """Roll a dice with specified number of sides"""
        if sides < 2:
            await ctx.send("❌ Dice must have at least 2 sides!")
            return
        
        result = random.randint(1, sides)
        embed = discord.Embed(
            title="🎲 Dice Roll",
            description=f"You rolled a **{result}** on a {sides}-sided dice!",
            color=0x00ff00
        )
        await ctx.send(embed=embed)

    @commands.command(name='coinflip')
    async def coinflip(self, ctx):
        """Flip a coin"""
        result = random.choice(['Heads', 'Tails'])
        emoji = '🪙' if result == 'Heads' else '🔄'
        
        embed = discord.Embed(
            title=f"{emoji} Coin Flip",
            description=f"The coin landed on **{result}**!",
            color=0xffd700
        )
        await ctx.send(embed=embed)

    @commands.command(name='8ball')
    async def eightball(self, ctx, *, question):
        """Ask the magic 8-ball a question"""
        responses = [
            "It is certain", "It is decidedly so", "Without a doubt",
            "Yes definitely", "You may rely on it", "As I see it, yes",
            "Most likely", "Outlook good", "Yes", "Signs point to yes",
            "Reply hazy, try again", "Ask again later", "Better not tell you now",
            "Cannot predict now", "Concentrate and ask again",
            "Don't count on it", "My reply is no", "My sources say no",
            "Outlook not so good", "Very doubtful"
        ]
        
        response = random.choice(responses)
        embed = discord.Embed(
            title="🎱 Magic 8-Ball",
            color=0x800080
        )
        embed.add_field(name="Question", value=question, inline=False)
        embed.add_field(name="Answer", value=response, inline=False)
        await ctx.send(embed=embed)

    @commands.command(name='choose')
    async def choose(self, ctx, *, choices):
        """Choose randomly from a list of options (separate with commas)"""
        options = [choice.strip() for choice in choices.split(',')]
        
        if len(options) < 2:
            await ctx.send("❌ Please provide at least 2 choices separated by commas!")
            return
        
        chosen = random.choice(options)
        embed = discord.Embed(
            title="🤔 Random Choice",
            description=f"I choose: **{chosen}**",
            color=0xff69b4
        )
        embed.add_field(name="Options", value=", ".join(options), inline=False)
        await ctx.send(embed=embed)

    @commands.command(name='joke')
    async def joke(self, ctx):
        """Tell a random joke"""
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Why did the scarecrow win an award? He was outstanding in his field!",
            "Why don't eggs tell jokes? They'd crack each other up!",
            "What do you call a fake noodle? An impasta!",
            "Why did the math book look so sad? Because it had too many problems!",
            "What do you call a bear with no teeth? A gummy bear!",
            "Why don't programmers like nature? It has too many bugs!",
            "What's the best thing about Switzerland? I don't know, but the flag is a big plus!"
        ]
        
        joke = random.choice(jokes)
        embed = discord.Embed(
            title="😂 Random Joke",
            description=joke,
            color=0xffff00
        )
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Fun(bot))