
from openai import AsyncOpenAI

from common.setting import Settings

client = AsyncOpenAI(
    # Defaults to os.environ.get("OPENAI_API_KEY")
    # Otherwise use: api_key="Your_API_Key",
    api_key=Settings.OPENAI_API_KEY
)
