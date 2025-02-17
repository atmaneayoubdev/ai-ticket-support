import openai
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from app.core.config import settings

# Set the OpenAI API key from settings
openai.api_key = settings.OPENAI_API_KEY


def generate_response_with_gpt(prompt: str) -> str:
    """
    Generates a response using GPT-4 through OpenAI's API with Langchain.

    :param prompt: The input prompt to be sent to GPT-4.
    :return: The generated response from GPT-4.
    """
    prompt_template = PromptTemplate(
        input_variables=["prompt"], template="{prompt}")
    llm = LLMChain(prompt=prompt_template,
                   llm=openai.Completion.create(model="gpt-4"))

    # Use Langchain to pass the prompt to GPT-4
    response = llm.run(prompt)
    return response
