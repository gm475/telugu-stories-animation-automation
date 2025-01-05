import os
from pytrends.request import TrendReq
import openai

# Fetch OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# Fetch trending topics using Google Trends (India)
def fetch_trending_topics():
    try:
        pytrends = TrendReq(hl='en-IN', tz=360)  # Set to India
        trending_searches = pytrends.trending_searches(pn='india')
        return trending_searches
    except Exception as e:
        print(f"Error fetching trending topics: {e}")
        return []

# Generate script based on the trending topic
def generate_script(trending_topic):
    try:
        prompt = f"Create a short, fun Telugu story for kids about the trending topic: {trending_topic}."
        response = openai.Completion.create(  # Corrected API call
            model="gpt-3.5-turbo",  # Updated to a supported model
            prompt=prompt,
            max_tokens=1000,
            temperature=0.7
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"Error generating script: {e}")
        return "Sorry, I couldn't generate a script at the moment."

def main():
    topics = fetch_trending_topics()
    
    if not topics:
        print("No trending topics found, exiting.")
        return
    
    trending_topic = topics[0]  # Use the top trending topic
    print(f"Using trending topic: {trending_topic}")
    
    script = generate_script(trending_topic)
    print(f"Final generated script: {script}")

if __name__ == "__main__":
    main()
