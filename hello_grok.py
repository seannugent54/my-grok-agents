import os
from dotenv import load_dotenv
from xai_sdk import Client
from xai_sdk.chat import user, system

# Load your API key from .env
load_dotenv()

client = Client(api_key=os.getenv("XAI_API_KEY"))

# Create a chat with Grok
chat = client.chat.create(model="grok-4.3")

# Add system prompt and user message
chat.append(system("You are a helpful AI assistant."))
chat.append(user("Hello Grok! Tell me something interesting about building AI agents."))

# Get response
response = chat.sample()

print("✅ Grok responded:")
print(response.content)