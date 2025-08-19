import logging
from pyrogram import idle
from os import makedirs, path
from config import Config
from unzipper.client import UnzipperBot  # Import the class directly

if __name__ == "__main__":
    logging.info(" >> Checking download location...")
    if not path.isdir(Config.DOWNLOAD_LOCATION):
        makedirs(Config.DOWNLOAD_LOCATION)

    logging.info(" >> Applying custom methods...")
    from .client import init_patch
    init_patch()

    logging.info(" >> Starting client...")
    unzip_client = UnzipperBot()  # Create the instance here
    from unzipper.modules import *  # Import modules after client is created
    unzip_client.start()

    logging.info(" >> Checking Log Channel...")
    from .helpers_nexa.checks import check_log_channel
    check_log_channel()

    logging.info("Bot is active Now! Join @NexaBotsUpdates")
    idle()
