import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
ENV_FILE = BASE_DIR / ".env"

load_dotenv(dotenv_path=ENV_FILE)

print("ENV FILE:", ENV_FILE)
print("ENV EXISTS:", ENV_FILE.exists())
print("GROQ KEY LOADED:", bool(os.getenv("GROQ_API_KEY")))

from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools


def build_agent():
    return Agent(
        model=Groq(
            id="qwen/qwen3.8-27b",
            max_tokens=800
        ),
        tools=[
            YFinanceTools(),
            DuckDuckGoTools()
        ],
        markdown=True,
        add_datetime_to_context=True,
        description=(
            "You are an investment analyst that researches stock prices, "
            "analyst recommendations, and stock fundamentals."
        ),
        instructions=[
            "Use given tools whenever possible.",
            "Format your response using Markdown.",
            "Use tables to display data where possible."
        ],
        debug_mode=True
    )
