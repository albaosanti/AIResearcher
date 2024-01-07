import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_KEY = os.getenv("OPENAI_API_KEY")
brwoserless_api_key = os.getenv("BROWSERLESS_API_KEY")
serper_api_key = os.getenv("SERP_API_KEY")
airtable_api_key = os.getenv("AIRTABLE_API_KEY")


msg = "Hello World"

print(f"OPEN AI: {OPENAI_KEY} \n BROWSER KEY \n {brwoserless_api_key} SERP KEY : {serper_api_key} \n AIR KEY : {airtable_api_key}")