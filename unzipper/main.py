import logging
from pyrogram import idle
from os import makedirs, path
from config import Config
from unzipper.client import UnzipperBot
from unzipper.helpers_nexa.buttons import Unzipper_Buttons  # Import the class

if __name__ == "__main__":
    logging.info(" >> Checking download location...")
    if not path.isdir(Config.DOWNLOAD_LOCATION):
        makedirs(Config.DOWNLOAD_LOCATION)

    logging.info(" >> Applying custom methods...")
    from .client import init_patch
    init_patch()

    logging.info(" >> Starting client...")
    unzip_client = UnzipperBot()
    from unzipper.modules import *  # Import modules after client
    unzip_client.start()

    logging.info(" >> Checking Log Channel...")
    from .helpers_nexa.checks import check_log_channel
    check_log_channel()

    # Define Buttons here after everything is set up
    global Buttons  # Make it accessible if needed elsewhere
    Buttons = Unzipper_Buttons()

    logging.info("Bot is active Now! Join @NexaBotsUpdates")
    idle()
