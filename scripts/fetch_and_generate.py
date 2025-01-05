import os
from pytrends.request import TrendReq
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

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
        # The prompt for generating the script
        prompt = f"Create a short, fun Telugu story for kids about the trending topic: {trending_topic}."

        # Make the API call using chat.completions.create
        chat_response = client.chat.completions.create(
            model="gpt-4o",  # Specify the correct model here
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )

        # Extract the message from the response
        return chat_response['choices'][0]['message']['content'].strip()

    except Exception as e:
        print(f"Error generating script: {e}")
        return "Sorry, I couldn't generate a script at the moment."

def main():
    topics = fetch_trending_topics()
    
    if topics.empty:  # Explicit check if DataFrame is empty
        print("No trending topics found, exiting.")
        return
    
    trending_topic = topics.iloc[0]  # Use the top trending topic
    print(f"Using trending topic: {trending_topic}")
    
    script = generate_script(trending_topic)
    print(f"Final generated script: {script}")

if __name__ == "__main__":
    main()
