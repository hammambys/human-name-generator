from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

def generate_baby_name(gender,country, name_type):
    # Load your Groq API key from environment
    groq_api_key = os.getenv("GROQ_API_KEY")

    # Initialize Groq LLM (OpenAI-compatible)
    llm = ChatOpenAI(
        model="llama-3.3-70b-versatile",
        api_key=groq_api_key,
        base_url="https://api.groq.com/openai/v1",
        temperature=0.9
    )

    # Prompt template
    prompt_template_name = PromptTemplate(
        input_variables=['gender', 'country', 'name_type'],
        template=(
            "I have a {gender} baby coming soon and I want a cool name for it, "
            "I'm from {country} and I want a {name_type} name. "
            "Suggest me 5 names, each on a new line. "
            "Don't include any explanation, just give me the names."
            "Be creative and fun!"
        )
    )

    # Build chain
    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="baby_name")

    response = name_chain({'gender':gender, 'country': country, 'name_type': name_type})
    return response

if __name__ == "__main__":
    print(generate_baby_name("Male", "Tunisia", "Modern"))
