
from openai import AsyncOpenAI

from common.setting import settings

client = AsyncOpenAI(
    # Defaults to os.environ.get("OPENAI_API_KEY")
    # Otherwise use: api_key="Your_API_Key",
    api_key=settings.OPENAI_API_KEY,
    base_url="https://openai.toriai.lol/v1"
)
