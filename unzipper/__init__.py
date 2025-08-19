import logging
from pyromod import listen
from .client import UnzipperBot
from .client.caching import update_cache

# Logging stuff
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

# Update cache
update_cache()

# Remove Buttons instantiation
# It will be handled in main.py
