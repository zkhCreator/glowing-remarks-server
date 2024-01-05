from openai import AsyncOpenAI

from common.setting import settings

client = AsyncOpenAI(
    # Defaults to os.environ.get("OPENAI_API_KEY")
    # Otherwise use: api_key="Your_API_Key",
    api_key=settings.OPENAI_API_KEY
)


class OpenAIService():
    @staticmethod
    async def assistant_create(name: str, instructions: str, model: str="gpt-4-1106-preview", tools: list = [{"type": "code_interpreter"}]):
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
        response = await client.beta.threads.create(
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
