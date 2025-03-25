
import sys
import asyncio
from langchain_openai import AzureChatOpenAI
from browser_use import Agent
from dotenv import load_dotenv
from pydantic import SecretStr
from browser_use import BrowserConfig
from browser_use.browser.browser import Browser
import os
import logging

logger = logging.getLogger(__name__)

async def main(task, llm_model):
    config = BrowserConfig(
        chrome_instance_path="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    )

    browser = Browser(config=config)

    llm = AzureChatOpenAI(
        model="gpt-4o",
        api_version="2024-10-21",
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT", ""),
        api_key=SecretStr(os.getenv("AZURE_OPENAI_KEY", "")),
    )
    
    agent = Agent(
        task=task,
        llm=llm,
        save_conversation_path="logs/conversation",
    )

    result = await agent.run()

    # Process results token-wise
    for action in result.action_results():
      print(action.extracted_content,end="\r",flush=True)
      print("\n\n")
      if action.is_done:
         print(action.extracted_content)

    # Close the browser after completion
    await browser.close()

    


if __name__ == "__main__":
    load_dotenv()
    task = "login with username: admin, password: admin" + " navigate to Workflow Studio" + "check if the page is loaded"
    llm_model = "gpt-4o"
    asyncio.run(main(task, llm_model))


