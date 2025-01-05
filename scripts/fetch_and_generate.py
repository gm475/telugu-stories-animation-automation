import os
from pytrends.request import TrendReq
import openai

# Fetch OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# Fetch trending topics using Google Trends
def fetch_trending_topics():
    pytrends = TrendReq(hl='en-US', tz=360)
    trending_searches = pytrends.trending_searches(pn='united_states')
    return trending_searches

# Generate script based on the trending topic
def generate_script(trending_topic):
    prompt = f"Create a short, fun Telugu story for kids about the trending topic: {trending_topic}."
    response = openai.chat.Completion.create(
        model="gpt-3.5-turbo",  # Updated to a supported model
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1000,
        temperature=0.7
    )
    return response['choices'][0]['message']['content'].strip()

topics = fetch_trending_topics()
script = generate_script(topics[0])  # Use the top trending topic
print(script)