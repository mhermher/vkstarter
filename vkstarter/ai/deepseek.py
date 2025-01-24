import os

from langchain_openai.chat_models.base import BaseChatOpenAI
from pydantic import SecretStr

API_KEY = SecretStr(os.environ.get("DEEPSEEK_API_KEY") or '')

DeepSeekModel = BaseChatOpenAI(
    model = 'deepseek-chat',
    api_key = API_KEY,
    base_url = 'https://api.deepseek.com',
    max_tokens = 1024
)

## ~ $0.014 per 1M tokens
