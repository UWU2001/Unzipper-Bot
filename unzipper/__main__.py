import logging
from pyromod import listen
from .client import UnzipperBot
from .client.caching import update_cache

# Logging stuff
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

# Update cache (can stay here as it doesn’t depend on unzip_client)
update_cache()

# Remove the unzip_client instantiation here
# It will be handled in main.py instead

# Buttons
from .helpers_nexa.buttons import Unzipper_Buttons
Buttons = Unzipper_Buttons()
