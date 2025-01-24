import os

from langchain_openai import ChatOpenAI
from pydantic import SecretStr

API_KEY = SecretStr(os.environ.get("OPENAI_API_KEY") or '')

GPTModel = ChatOpenAI(model="gpt-4o-mini", api_key = API_KEY)

## ~ $0.15 per 1M tokens
