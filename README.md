

<h1 align="center">ServiceNow Test Automation using AI-Powered Browser-Use</h1>

This project is a **customized version of [browser-use](https://github.com/browser-use/browser-use)**, modified to automate **ServiceNow testing** using natural language prompts. The AI-powered agent takes descriptive prompts, converts them into browser actions, executes them, and logs the actions for traceability and debugging.

---

## 📚 Introduction

`browser-use` is an open-source AI agent that connects to the browser and performs tasks based on natural language prompts. 

✅ In this customized version:
- It automates **ServiceNow UI testing** using AI.
- **Input:** Natural language prompt describing a test task.
- **Action Conversion:** Converts the prompt to browser actions.
- **Execution:** Performs the actions using Playwright.
- **Logging:** Logs actions, errors, and test results for review.

---
# Quick start

1. Clone this repository and cd inside the project
2. Create a virtual python environmet </br>
`uv venv --python 3.11` </br>
`uv pip install -e ".[dev]"`
3. Install playwright
`playwright install `
4. Set up your environment variable file, ask the appropriate authority for the credentials </br>
`cp .env.example .env`


# Demo
1. Navigate to examples folder
2. In the main function you can customize the prompt, i.e. the task to perform desired tests.
```
if __name__ == "__main__":
    load_dotenv()
    task = "login with username: admin, password: admin" + " navigate to Workflow Studio" + "check if the page is 
    loaded"
    llm_model = "gpt-4o"
    asyncio.run(main(task, llm_model))
```
3. In the terminal run </br>
`python3 script.py`





###Browser-USe Citation

```bibtex
@software{browser_use2024,
  author = {Müller, Magnus and Žunič, Gregor},
  title = {Browser Use: Enable AI to control your browser},
  year = {2024},
  publisher = {GitHub},
  url = {https://github.com/browser-use/browser-use}
}
```

---

