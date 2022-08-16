from logging import Logger

from slack_bolt.context.say.async_say import AsyncSay
from slack_bolt.context.async_context import AsyncBoltContext
from slack_sdk import WebClient


async def sample_message_callback(context: AsyncBoltContext, say: AsyncSay, logger: Logger):
    try:
        greeting = context["matches"][0]
        await say(f"{greeting}, how are you?")
    except Exception as e:
        logger.error(e)
