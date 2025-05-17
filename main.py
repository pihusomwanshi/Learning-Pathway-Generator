from fastapi import FastAPI,HTTPException
from fastapi.middleware.cors import CORSMiddleware

from openai import AzureOpenAI
from dotenv import load_dotenv
import os


# Load environment variables
load_dotenv("Config.env")

OPENAI_API_VERSION = os.getenv("OPENAI_API_VERSION")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")

print(OPENAI_API_VERSION)
print(AZURE_OPENAI_ENDPOINT)
print(AZURE_OPENAI_API_KEY)

# Initialize OpenAI client
client = AzureOpenAI()

# Create FastAPI instance
app = FastAPI()

# Allow frontend (React app) to communicate with backend (FastAPI)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    # ["https://tourmaline-cocada-0a58a7.netlify.app"],  # Specify React frontend URL
    #allow_origins=["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Define API route
@app.get("/generate_learning_pathway/")
def generate_learning_pathway(topic: str, proficiency_level: str):

    prompt = f"Create a structured learning pathway for a {proficiency_level} level on the topic: {topic}."

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": "You are an expert educator."},
                  {"role": "user", "content": prompt}],
        temperature= 0.7,
        max_tokens= 256,
        top_p= 0.6,
        frequency_penalty= 0.7
    )

    return {"learning_pathway": response.choices[0].message.content}
