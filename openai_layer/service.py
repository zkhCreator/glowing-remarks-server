from typing import List, Literal, Union
from uuid import UUID

from auth.db_models import User
from auth.models import UserRead
from openai_layer.usage.model import UsageTokenModel, UserUsageTokenModel
from openai_layer.usage.service import UsageService
from openai_layer.usage.utils import UsageUtils
from .common import client
from openai.types.chat.chat_completion_message_param import ChatCompletionMessageParam
from openai.types.chat.chat_completion_message_param import ChatCompletionUserMessageParam
from openai.types.chat.chat_completion import ChatCompletion
from openai.types.beta.thread import Thread
from sqlalchemy.ext.asyncio import AsyncSession


class OpenAIService():
    # @staticmethod
    # async def assistant_create(name: str, instructions: str, model: str = "gpt-4-1106-preview", tools: list = [{"type": "code_interpreter"}]):
    #     response = await client.beta.assistants.create(
    #         name,
    #         instructions,
    #         model,
    #         tools=tools
    #     )

    #     return response.id

    # @staticmethod
    # async def assistant_retrieve(assistant_id: str):
    #     response = await client.beta.assistants.retrieve(assistant_id)
    #     return response.id

    # @staticmethod
    # async def thread_create(message: str, params: str):
    #     response: Thread = await client.beta.threads.create(
    #         message=message,
    #         params=params
    #     )
    #     return response.id

    # @staticmethod
    # async def thread_retrieve(thread_id: str):
    #     response = await client.beta.threads.retrieve(thread_id)
    #     return response.id

    # @staticmethod
    # async def run_create(assistant_id: str, thread_id: str, instruction: str):
    #     run = await client.beta.threads.runs.create(
    #         thread_id=thread_id,
    #         assistant_id=assistant_id,
    #         instructions=instruction
    #     )
    #     return run.id

    # @staticmethod
    # async def run_retrieve(run_id: str, thread_id: str):
    #     response = await client.beta.threads.runs.retrieve(run_id, thread_id)
    #     return response.id

    # @staticmethod
    # async def message_list(thread_id: str):
    #     response = await client.beta.threads.messages.list(thread_id)
    #     return response.data

    @staticmethod
    async def chat_completion(db: AsyncSession,
                              user_id: UUID,
                              messages: List[ChatCompletionMessageParam],
                              max_tokens: int = 4096,
                              model_name: Union[
                                  str,
                                  Literal[
            "gpt-4-1106-preview",
            "gpt-4-vision-preview",
            "gpt-4",
            "gpt-4-0314",
            "gpt-4-0613",
            "gpt-4-32k",
            "gpt-4-32k-0314",
            "gpt-4-32k-0613",
            "gpt-3.5-turbo",
            "gpt-3.5-turbo-16k",
            "gpt-3.5-turbo-0301",
            "gpt-3.5-turbo-0613",
            "gpt-3.5-turbo-1106",
            "gpt-3.5-turbo-16k-0613",
                                      ],
                              ] = "gpt-3.5-turbo-1106") -> ChatCompletion:
        response = await client.chat.completions.create(
            model=model_name,
            max_tokens=max_tokens,
            messages=messages,
            stream=False
        )

        if not response.choices:
            raise ValueError("response_message is empty")
        print("is ok here?")
        request_token_model: UsageTokenModel = UsageTokenModel(
            "send content", response.usage.prompt_tokens)
        response_token_model: UsageTokenModel = UsageTokenModel(
            response.choices[0].message.content, response.usage.completion_tokens)

        dict_value = {
            "user_id": user_id,
            "request_message": request_token_model.content,
            "request_token": request_token_model.token,
            "response_message": response_token_model.content,
            "response_token": response_token_model.token
        }
        usage = UserUsageTokenModel(**dict_value)

        UsageService.addUsage(usage, db=db)

        return response
