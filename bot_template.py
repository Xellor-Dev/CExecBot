import discord
from discord.ext import commands
import subprocess
import os

# IDs of users who are allowed to execute the command
ALLOWED_USERS = [ID, ID, ...]

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command(name="exec_c")
async def execute_c_code(ctx, *, code: str):
    if ctx.author.id not in ALLOWED_USERS:
        await ctx.send("You are not authorized to use this command.")
        return

    if code.startswith("```") and code.endswith("```"):
        code = code[3:-3].strip()

    code_filename = "user_code.c"
    binary_filename = "user_program"

    with open(code_filename, "w") as f:
        f.write(code)

    compile_command = ["gcc", code_filename, "-o", binary_filename]
    compile_result = subprocess.run(compile_command, capture_output=True, text=True)

    if compile_result.returncode != 0:
        
        await ctx.send(f"Compilation error:\n```\n{compile_result.stderr}\n```")
        return

    
    run_command = ["./" + binary_filename]
    run_result = subprocess.run(run_command, capture_output=True, text=True)

    
    if run_result.returncode == 0:
        await ctx.send(f"Result:\n```\n{run_result.stdout}\n```")
    else:
        await ctx.send(f"Error:\n```\n{run_result.stderr}\n```")

    
    os.remove(code_filename)
    os.remove(binary_filename)

bot.run('Discord Bot Token')
