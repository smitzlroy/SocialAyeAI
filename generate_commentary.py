import os
import openai
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

def generate_commentary(title, description):
    openai.api_key = OPENAI_API_KEY
    prompt = (
        "Provide a thoughtful and insightful commentary on the following news article. "
        "Your tone should be normal sounding, non-biased, fair, subjective, opinionated, and kind.\n"
        f"Title: {title}\n"
        f"Description: {description}\n"
        "Commentary:"
    )
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Specify the GPT-4 model
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message['content'].strip()
    except openai.error.OpenAIError as e:
        print(f"Error generating commentary: {e}")
        if "quota" in str(e):
            return "Unable to generate commentary at this time due to quota limits. Please try again later."
        return "Unable to generate commentary at this time."
