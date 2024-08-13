import os

class Config:
    API_ID = int(os.getenv("API_ID", 16536417))
    API_HASH = os.getenv("API_HASH", 'f6e58a549da642d7b765744a2f82c6d9')
    BOT_TOKEN = os.getenv("BOT_TOKEN", '7445547849:AAHfX4_8TQ57cg71Q_l9ABoa6RfgfPWHgsE')
