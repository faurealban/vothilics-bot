#get token
TOKEN = ""
with open(".git/token", "r") as token_file:
    TOKEN = token_file.read().rstrip()

config = {
    "token": TOKEN,
    "intents": discord.Intents.all(),
    "console_prefix": ">> ",
    "command_prefix": "!"
}
