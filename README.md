# StandupBot
A bot that allows asynchronous configurable standups in Discord. When you initialize the bot in a channel, you allow participants to enter their weekly/daily tasks in a web form which will be bundled on a public or private website and posted in the channel as a pinned message.

How to add the bot to your Discord server

Create a Discord bot token on https://discordapp.com/developers
Create a .env file and enter your Discord token: DISCORD_TOKEN=TOKENHERE
Invite the bot to your server with this URL: https://discordapp.com/api/oauth2/authorize?permissions=67497024&scope=bot&client_id=YOUR_BOTS_DISCORD_CLIENT_ID
Installation

Create a .env file with DISCORD_TOKEN=TOKENHERE in it
Tweak any settings in standup/settings.py to your needs
Run the Django server (python manage.py runserver for a dev server, production deploy with gunicorn or uwsgi on demand)
Run the python manage.py run_bot command in a seperate background process (supervisord)
Run python manage.py createsuperuser to create a admin user
Run python manage.py collectstatic to gather your static files for the website
Go to the admin on /admin in your browser, log in and....
Update the Site in Sites to match your servers URL
Set up the first standup types with questions
Start using the bot in Discord using the !newstandup and !addparticipant commands
See all available commands by executing !standup, the bot will DM a overview
