import os
from dotenv import load_dotenv

load_dotenv()



SERP_API_KEY = os.getenv("SERP_API_KEY")

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
MODEL = os.getenv("MODEL")

print(ANTHROPIC_API_KEY)
print(MODEL)