import discord
from discord.ext import commands

class HelpPaginator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='pixelhelp')
    async def pixelhelp(self, ctx):
        embeds = self.create_help_embeds()
        current_page = 0
        
        # Send the initial embed message
        message = await ctx.send(embed=embeds[current_page])

        # Add reactions for navigation
        await message.add_reaction("⬅️")
        await message.add_reaction("➡️")

        # Define the check for reaction
        def check(reaction, user):
            return user == ctx.author and reaction.message.id == message.id and str(reaction.emoji) in ["⬅️", "➡️"]

        # Pagination Logic
        while True:
            try:
                reaction, user = await self.bot.wait_for("reaction_add", timeout=60.0, check=check)
                
                # Navigate pages
                if str(reaction.emoji) == "➡️":
                    current_page = (current_page + 1) % len(embeds)
                elif str(reaction.emoji) == "⬅️":
                    current_page = (current_page - 1) % len(embeds)

                await message.edit(embed=embeds[current_page])
                await message.remove_reaction(reaction, user)

            except Exception:
                break

    def create_help_embeds(self):
        embeds = []

        # Page 1: System Management
        embed1 = discord.Embed(
            title="🗂️ System Management Commands",
            description="Commands to manage your system and profiles.",
            color=0x8A2BE2
        )
        embed1.add_field(name="`!create_system <name>`", value="Create a new system.", inline=False)
        embed1.add_field(name="`!edit_system`", value="Edit your existing system.", inline=False)
        embed1.add_field(name="`!delete_system`", value="Delete your system permanently.", inline=False)
        embed1.add_field(name="`!system`", value="Display system info.", inline=False)
        embed1.add_field(name="`!export_system`", value="Export your system data to JSON.", inline=False)
        embed1.add_field(name="`!import_system`", value="Import system data from JSON.", inline=False)
        embeds.append(embed1)

        # Page 2: Profile Management
        embed2 = discord.Embed(
            title="👥 Profile Management Commands",
            description="Commands to manage alters and profiles.",
            color=0x8A2BE2
        )
        embed2.add_field(name="`!create <name> <pronouns>`", value="Create a new profile with specified pronouns.", inline=False)
        embed2.add_field(name="`!edit <name>`", value="Edit an existing profile.", inline=False)
        embed2.add_field(name="`!delete <name>`", value="Delete a profile.", inline=False)
        embed2.add_field(name="`!show <name>`", value="Display profile info.", inline=False)
        embed2.add_field(name="`!list_profiles`", value="List all profiles.", inline=False)
        embeds.append(embed2)

        # Page 3: Folder Management
        embed3 = discord.Embed(
            title="📁 Folder Management Commands",
            description="Commands to manage folders and organize alters.",
            color=0x8A2BE2
        )
        embed3.add_field(name="`!create_folder <name>`", value="Create a new folder.", inline=False)
        embed3.add_field(name="`!edit_folder <name>`", value="Edit an existing folder.", inline=False)
        embed3.add_field(name="`!delete_folder <name>`", value="Delete a folder permanently.", inline=False)
        embed3.add_field(name="`!show_folder <name>`", value="Display folder info.", inline=False)
        embed3.add_field(name="`!list_folders`", value="List all folders.", inline=False)
        embeds.append(embed3)

        return embeds

async def setup(bot):
    await bot.add_cog(HelpPaginator(bot))
