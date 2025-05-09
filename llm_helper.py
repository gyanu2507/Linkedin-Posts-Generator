from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()
llm = ChatGroq(groq_api_key="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", model_name="llama-3.3-70b-versatile")


if __name__ == "__main__":
    response = llm.invoke("Two most important ingradient in samosa are ")
    print(response.content)





