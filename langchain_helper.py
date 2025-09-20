from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

def generate_pet_name(animal_type, pet_color):
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
        input_variables=['animal_type', 'pet_color'],
        template=(
            "I have a {animal_type} pet and I want a cool name for it, "
            "it is {pet_color} in color. Suggest me five cool names for my pet."
            "Don't include any explanation, just give me the names."
            "Be creative and fun!"
        )
    )

    # Build chain
    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="pet_name")

    response = name_chain({'animal_type': animal_type, 'pet_color': pet_color})
    return response

if __name__ == "__main__":
    print(generate_pet_name("Dog", "Black"))
