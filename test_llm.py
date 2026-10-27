from llm import get_llm

llm = get_llm()
print("Calling Gemini...")
print(llm.invoke("Say hello in one word").content)