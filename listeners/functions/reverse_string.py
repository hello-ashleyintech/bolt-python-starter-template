from slack_bolt.context.complete_success.async_complete_success import AsyncCompleteSuccess
from slack_bolt.context.complete_error.async_complete_error import AsyncCompleteError
from logging import Logger


async def reverse_string(event, complete_success: AsyncCompleteSuccess, complete_error: AsyncCompleteError, logger: Logger):
    try:
        string_to_reverse = event["inputs"]["stringToReverse"]
        await complete_success({
            "reverseString": string_to_reverse[::-1]
        })
    except Exception as e:
        logger.error(e)
        await complete_error("Cannot reverse string")
        raise e
