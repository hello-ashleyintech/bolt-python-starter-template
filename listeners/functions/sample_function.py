

from logging import Logger
from slack_bolt.async_app import AsyncComplete


async def sample_function(event, complete: AsyncComplete, logger: Logger):
    try:
        message = event["inputs"]["message"]
        await complete(
            outputs={
                "updatedMsg": f":wave: You submitted the following message: \n\n>{message}"
            }
        )
    except Exception as e:
        logger.error(e)
        await complete(error="Cannot submit the message")
        raise e
