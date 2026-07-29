from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from datetime import date
import os
from dotenv import load_dotenv
from tools import (
    get_total_salary,
    get_total_expenses,
    get_balance,
    expense_by_category,
    largest_expense,
    add_expense,
)
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
print(groq_api_key) 

model = init_chat_model(
    "llama-3.3-70b-versatile",
    model_provider="groq",
)
response = model.invoke("Say Hello")

print(response.content)

tools = [
    get_total_salary,
    get_total_expenses,
    get_balance,
    expense_by_category,
    largest_expense,
    add_expense,
]

system_prompt = """
You are a helpful personal banking assistant.

Your responsibilities:

- Answer questions about salary.
- Answer questions about expenses.
- Calculate balance.
- Use tools whenever information is needed.
- Never guess financial information.
- If a tool is available, always use it.
"""
agent = create_agent(
    model=model,
    tools=tools,
    system_prompt=system_prompt,
)

print("🏦 Bank Assistant")
print("Type 'exit' to quit.\n")

while True:
    question = input("👤 You: ")

    if question.lower() in ["exit", "quit"]:
        print("👋 Goodbye!")
        break

    response = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": question,
                }
            ]
        }
    )
    print("\n\n")
    for message in response["messages"]:
        print(f"\n📌 {type(message).__name__}")

        if hasattr(message, "content"):
            print(message.content)

        if hasattr(message, "tool_calls") and message.tool_calls:
            print("Tool Calls:", message.tool_calls)
    print("\n\n")
    print(f"\n🤖 Assistant: {response['messages'][-1].content}\n")