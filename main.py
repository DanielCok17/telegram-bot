from telethon import TelegramClient, events

# Your API credentials
api_id = 23880538
api_hash = 'f19dfb33780354206bc1005a618afd4f'
# The phone number or bot token associated with your account
phone = '+421917387255'

# The chat ID of the person whose messages you want to resend
person_chat_id = 'panzerwagenn'
# The chat ID of the group where you want to resend the messages
group_chat_id = 'bitcoachCHAT'
# https://t.me/join_bitcoachCHAT

# Create a Telethon client
client = TelegramClient('session_name', api_id, api_hash)

# Connect to the Telegram server
client.start(phone)

# Define a handler for new messages from the person
@client.on(events.NewMessage(chats=person_chat_id))
async def handle_new_message(event):
    # Forward the message to the group
    await client.forward_messages(group_chat_id, event.message)

# Run the client
client.run_until_disconnected()
