from logging import Logger

from slack_bolt.context.ack.async_ack import AsyncAck
from slack_sdk.web.async_client import AsyncWebClient


async def sample_view_callback(view, ack: AsyncAck, body: dict, client: AsyncWebClient, logger: Logger):
    try:
        await ack()
        sample_user_value = body["user"]["id"]
        provided_values = view["state"]["values"]
        logger.info(f"Provided values {provided_values}")
        sample_input_value = provided_values["input_block_id"]["sample_input_id"]["value"]
        sample_convo_value = provided_values["select_channel_block_id"]["sample_dropdown_id"]["selected_conversation"]

        await client.chat_postMessage(
            channel=sample_convo_value,
            text=f"<@{sample_user_value}> submitted the following :sparkles: "
            + f"hopes and dreams :sparkles:: \n\n {sample_input_value}",
        )
    except Exception as e:
        logger.error(e)
