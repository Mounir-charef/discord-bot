import discord
from discord.ui import Button, View
import os
import pyjokes


def main():
    intents = discord.Intents().all()
    my_secret = os.environ['TOKEN']
    client = discord.Client(intents=intents)

    async def new_joke(inter):
        print(inter)
        await inter.response.send_message(pyjokes.get_joke(language='en', category='all'))

    async def send_joke(msg):
        joke = pyjokes.get_joke(language='en', category='all')
        button = Button(label='Another one?', style=discord.ButtonStyle.green, emoji='✌',
                        disabled=False)
        button.callback = new_joke
        view = View(timeout=10)
        view.add_item(button)
        await msg.channel.send(f'{joke}............ blame {msg.author.mention} for the joke', view=view)

    @client.event
    async def on_message(msg):
        if msg.author == client.user:
            return
        if msg.content.startswith('$'):
            command = msg.content[1:]
            match command:
                case 'hello':
                    await msg.channel.send(f'dasertni {msg.author.mention} ??!! huuuuh')
                case 'joke':
                    await send_joke(msg)

                case _:
                    await msg.channel.send('Unvalid Command inserted!!? yal hmar 🤦‍♂️')

    client.run(my_secret)


if __name__ == '__main__':
    main()
