from slack_bolt.context.ack.async_ack import AsyncAck
from slack_bolt.context.respond.async_respond import AsyncRespond
from logging import Logger


async def sample_command_callback(command, ack: AsyncAck, respond: AsyncRespond, logger: Logger):
    try:
        await ack()
        await respond(f"Responding to the sample command! Your command was: {command['text']}")
    except Exception as e:
        logger.error(e)
