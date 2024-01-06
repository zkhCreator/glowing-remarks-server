from typing import List, Literal, Union
from .common import client
from openai.types.chat.chat_completion_message_param import ChatCompletionMessageParam
from openai.types.chat.chat_completion import ChatCompletion
from openai.types.beta.thread import Thread

class OpenAIService():
    @staticmethod
    async def assistant_create(name: str, instructions: str, model: str = "gpt-4-1106-preview", tools: list = [{"type": "code_interpreter"}]):
        response = await client.beta.assistants.create(
            name,
            instructions,
            model,
            tools=tools
        )

        return response.id

    @staticmethod
    async def assistant_retrieve(assistant_id: str):
        response = await client.beta.assistants.retrieve(assistant_id)
        return response.id

    @staticmethod
    async def thread_create(message: str, params: str):
        response: Thread = await client.beta.threads.create(
            message=message,
            params=params
        )
        return response.id

    @staticmethod
    async def thread_retrieve(thread_id: str):
        response = await client.beta.threads.retrieve(thread_id)
        return response.id

    @staticmethod
    async def run_create(assistant_id: str, thread_id: str, instruction: str):
        run = await client.beta.threads.runs.create(
            thread_id=thread_id,
            assistant_id=assistant_id,
            instructions=instruction
        )
        return run.id

    @staticmethod
    async def run_retrieve(run_id: str, thread_id: str):
        response = await client.beta.threads.runs.retrieve(run_id, thread_id)
        return response.id

    @staticmethod
    async def message_list(thread_id: str):
        response = await client.beta.threads.messages.list(thread_id)
        return response.data

    @staticmethod
    async def chat_completion(messages: List[ChatCompletionMessageParam], max_tokens: int = 4096, model: Union[
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
    ] = "gpt-3.5-turbo-1106", ) -> ChatCompletion:
        response = await client.chat.completions.create(
            model=model,
            max_tokens=max_tokens,
            messages=messages,
        )
        return response
