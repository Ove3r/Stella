import discord
import json, requests
from discord.ext import commands
from discord.ext.commands import MemberConverter
from helpers import key
from helpers.player import Player
from helpers.errors import *

class Skyborn_Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="poll",
        brief="Admin Command",
        help=(
        "**stella poll [ign] [optional : force]**\n"
        "Attempts to post a poll for Skyborn.\n"
        "Notes: \n "
        "• If the word `force` follows the name argument, the application will be processed ignoring any requirements."
        )
    )
    @commands.has_role(604433471284445184)
    async def poll(self, ctx, name, args=None):
        force = False
        if args: #Add aditional options for arguments that are given
            if args.lower() == "force":
                force = True

        responses = requests.get(key.SKYBORN_POLLS).json()
        responses = list(reversed(responses["values"]))
        for entry in responses:
            if name.lower() == entry[0].lower():
                application = entry
                break

        try:
            applicant = Player(application[0],profile=application[15])
        except ProfileNotFound:
            await ctx.reply("ProfileNotFound Error")
            return
        except PlayerNotFound:
            await ctx.reply("PlayerNotFound Error")
            return
        except UnboundLocalError:
            await ctx.reply(f"Applicant `{name}` could not be found in google sheet.")
            return

        applicant.get_player_summary()
        if applicant.skill_average >= key.skyborn_skill_requirement or force: #Skill Average requirement for Skyborn
            #Poll embed
            embed=discord.Embed(title=f"{applicant.name} ~~ {applicant.fruit}", description=application[1], color=0xdc6565)
            embed.set_thumbnail(url=f"https://visage.surgeplay.com/bust/{applicant.uuid}")
            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
            if force:
                embed.set_footer(text="Stella Bot by Over#6203. This application was forced through, ignoring requirement checks.")
            else:
                embed.set_footer(text="Stella Bot by Over#6203")
            embed.add_field(name="Activity", value=application[2],inline=False)
            embed.add_field(name="Stella Calculated Skill Average", value=f"{applicant.skill_average}\n**The following is information from the application.**",inline=True)
            embed.add_field(name="Skills", value=application[3],inline=False)
            embed.add_field(name="Slayers", value=application[4],inline=False)
            embed.add_field(name="Wealth and Acquisition", value=application[5],inline=False)
            embed.add_field(name="List some of your most valuable items.", value=application[6],inline=False)
            embed.add_field(name="What Armor sets do you own?", value=application[7],inline=False)
            embed.add_field(name="What are the strongest sword and bow you own?", value=application[8],inline=False)
            embed.add_field(name="Minion Slots", value=application[9],inline=False)
            embed.add_field(name="What's your most impressive collection/skill stat?", value=application[10],inline=False)
            embed.add_field(name="Timezone", value=application[11],inline=False)
            embed.add_field(name="How did you hear about us?", value=application[14],inline=False)

            if application[13] != "": #Optional Field
                embed.add_field(name="Anything else we need to know?", value=application[13],inline=False)

            polls_channel = self.bot.get_channel(604434538936008768)
            poll = await polls_channel.send(embed=embed)
            reactions = ['👍', '👤', '👎']
            for emoji in reactions:
                await poll.add_reaction(emoji)
            await ctx.reply(f"`{applicant.name}` meets the skill average requirement and has been put into the polls channel.")

            #Success message to applicant
            if force:
                applicantMessage=discord.Embed(title=f"SkyBorn Application ~~ `{applicant.name}`", description=f"Your application has been manually forced through into a polls channel. \nYou will receive a response in approximately 24 hours. \nIf you do not receive this response, please message an officer or the GM.", color=0xdc6565)
                applicantMessage.set_thumbnail(url=f"https://visage.surgeplay.com/bust/{applicant.uuid}")
                applicantMessage.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
                applicantMessage.set_footer(text="Stella Bot by Over#6203")
            else:
                applicantMessage=discord.Embed(title=f"SkyBorn Application ~~ `{applicant.name}`", description=f"Your application has been processed and put into a polls channel. \nYou will receive a response in approximately 24 hours. \nIf you do not receive this response, please message an officer or the GM.", color=0xdc6565)
                applicantMessage.set_thumbnail(url=f"https://visage.surgeplay.com/bust/{applicant.uuid}")
                applicantMessage.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
                applicantMessage.set_footer(text="Stella Bot by Over#6203")

        else:
            await ctx.reply(f"`{applicant.name}` does not meet the skill average requirement. \nTo force the poll type `stella poll {applicant.name} force`")
            applicantMessage=discord.Embed(title=f"SkyBorn Application ~~ `{applicant.name}`", description=f"Your application to Skyborn has been declined for the following reason(s): \nSkill Average does not meet requirement of {skillRequirement}.", color=0xdc6565)
            applicantMessage.set_thumbnail(url=f"https://visage.surgeplay.com/bust/{applicant.uuid}")
            applicantMessage.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
            applicantMessage.set_footer(text="Stella Bot by Over#6203")


        try:
            converter = MemberConverter()
            user = await converter.convert(ctx,application[1])
            await user.send(embed=applicantMessage)
            await ctx.reply(f"Applicant {application[1]} has received the following response message",embed=applicantMessage)
        except Exception as e:
            await ctx.reply(f"Error sending response message to applicant: {e}")

    @commands.command(name="reqs",aliases=["req"],
        brief="Returns Skyborn Requirements",
        help=(
        "**stella reqs**\n"
        "Returns the current minimum requirements to be polled for Skyborn."
        )
    )
    async def requirements(self, ctx):
        embed=discord.Embed(title="Skyborn Requirements", description="These are minimum to be polled. You may/may not be accepted.", color=0xdc6565)
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url="https://cdn.discordapp.com/icons/604420816817356822/a_1f3464f9dc5ace6959a5818238f920ff.png?size=256")
        embed.set_footer(text="Stella Bot by Over#6203")
        embed.add_field(name="Skills",value=f"Average: {key.skyborn_skill_requirement}",inline=True)
        embed.add_field(name="To Apply",value="[Google Form Application](http://bit.ly/skybornguild)",inline=True)
        embed.add_field(name="Slayers",value=f"Average: {key.skyborn_slayer_requirement}",inline=False)

        await ctx.reply(embed=embed)



def setup(bot):
    bot.add_cog(Skyborn_Commands(bot))