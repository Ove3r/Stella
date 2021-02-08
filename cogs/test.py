from discord.ext import commands

class TestCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='test')
    async def test(self, ctx, *arg):
        try:
            await ctx.send(arg)
        except Exception as e:
            await ctx.send(f'Test Error: {e}')


def setup(bot):
    bot.add_cog(TestCog(bot))
