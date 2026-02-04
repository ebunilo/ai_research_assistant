from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search
from wsgiref import types
from pydantic import BaseModel, Field


def greeting_tool() -> str:
    """Returns a warm friendly greeting."""
    return "Hello from your specialized greeting tool. Welcome!"

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='A friendly agent that provides a special greeting.',
    instruction='You are a friendly agent. When the user greets you, you must use the greeting_tool to respond.',
    tools=[google_search],
    generate_content_config=types.GenerateContentConfig(
        temperature=0.2,
        max_output_tokens=250,
        safety_settings=[
            types.SafetySetting(
                category=types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
                threshold=types.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
            )
        ]
    )
)
