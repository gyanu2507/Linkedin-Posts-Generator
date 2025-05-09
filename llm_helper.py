from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()
llm = ChatGroq(groq_api_key=os.getenv("GROQ_API_KEY"), model_name="llama-3.3-70b-versatile")

def test_llm_connection():
    """Test if the LLM connection is working properly"""
    try:
        # Simple test prompt to verify connection
        test_prompt = "Explain what is Python programming language in one sentence."
        response = llm.invoke(test_prompt)
        print("✅ LLM Connection Test:")
        print(response.content)
        return True
    except Exception as e:
        print(f"❌ Connection Error: {str(e)}")
        return False

if __name__ == "__main__":
    # Run connection test
    test_llm_connection()





