from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

@tool
def chain_historical_expert(input_text: str) -> str:
    """Fornisce approfondimenti storici, risponde a domande e agisce come un assistente esperto di storia."""
    model = ChatOpenAI(model_name="gpt-4o")
    
    system_prompt = (
        "You are an historical expert.\n"
        "Your mission is to provide in-depth content on the topic,\n"
        "answer questions, and act as an assistant.\n"
        "Use emojis to make your answers more engaging and friendly.\n"
        "Always strive to be approachable and helpful, offering the\n"
        "most accurate and useful information possible to users."
    )
    
    prompt = ChatPromptTemplate([
        ("system", "{system_prompt}"),
        ("user", "{input}")
    ])
    
    chain = prompt | model
    
    result = chain.invoke({
        "input": input_text,
        "system_prompt": system_prompt
    })
    
    print(" " * 80)
    print("chain_historical_expert")
    print("*" * 80)
    
    return result