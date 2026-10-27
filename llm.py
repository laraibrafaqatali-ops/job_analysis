import os
from dotenv import load_dotenv

load_dotenv()

PROVIDER = os.getenv("LLM_PROVIDER", "gemini")  # "gemini" ya "groq"


def get_llm():
    if PROVIDER == "groq":
        from langchain_groq import ChatGroq
        return ChatGroq(
            model="openai/gpt-oss-120b",
            api_key=os.getenv("GROQ_API_KEY"),
            temperature=0,
            timeout=30,
            max_retries=2,
        )

    from langchain_google_genai import ChatGoogleGenerativeAI
    return ChatGoogleGenerativeAI(
        model="gemini-3.8-flash",
        google_api_key=os.getenv("GOOGLE_API_KEY"),
        temperature=0,
        timeout=30,
        max_retries=2,
    )
 