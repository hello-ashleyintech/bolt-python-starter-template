import os
import logging
import asyncio

from slack_bolt.async_app import AsyncApp
from slack_bolt.adapter.socket_mode.async_handler import AsyncSocketModeHandler

from listeners import register_listeners


# Initialization
app = AsyncApp(token=os.environ.get("SLACK_BOT_TOKEN"))
logging.basicConfig(level=logging.DEBUG)

# Register Listeners
register_listeners(app)


async def main(app):
    handler = AsyncSocketModeHandler(app, os.environ["SLACK_APP_TOKEN"])
    await handler.start_async()

# Start Bolt app
if __name__ == "__main__":
    asyncio.run(
        main(app)
    )
