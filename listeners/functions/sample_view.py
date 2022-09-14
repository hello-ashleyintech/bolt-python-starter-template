import logging

from slack_sdk.web.async_client import AsyncWebClient

from slack_bolt.async_app import AsyncComplete, AsyncAck


async def sample_view(event, client: AsyncWebClient, complete: AsyncComplete, logger: logging.Logger):
    try:
        interactivity_pointer = event["inputs"]["interactivity"]["interactivity_pointer"]
        await client.views_open(
            interactivity_pointer=interactivity_pointer,
            trigger_id=None,
            view={
                "type": "modal",
                "callback_id": "func_sample_view_id",
                "title": {"type": "plain_text", "text": "Sample modal title"},
                "blocks": [
                    {
                        "type": "input",
                        "block_id": "input_block_id",
                        "label": {
                            "type": "plain_text",
                            "text": "What are your hopes and dreams?",
                        },
                        "element": {
                            "type": "plain_text_input",
                            "action_id": "sample_input_id",
                            "multiline": True,
                        },
                    },
                ],
                "submit": {"type": "plain_text", "text": "Submit"},
                "notify_on_close": True,
            },
        )
    except Exception as e:
        logger.error(e)
        await complete(error="Cannot create view")
        raise e


async def sample_view_submission(ack: AsyncAck, view, complete: AsyncComplete, logger: logging.Logger):
    try:
        message = view["state"]["values"]["input_block_id"]["sample_input_id"]["value"]
        await ack()
        await complete(outputs={"markdown": f":wave: You submitted the following message: \n\n>{message}"})
    except Exception as e:
        logger.error(e)
        await complete(error="Cannot submit form")
        raise e


async def sample_view_closed(ack: AsyncAck, complete: AsyncComplete, logger: logging.Logger):
    try:
        await ack()
        await complete(outputs={"markdown": f"You closed the form"})
    except Exception as e:
        logger.error(e)
        await complete(error="Cannot close form")
        raise e
