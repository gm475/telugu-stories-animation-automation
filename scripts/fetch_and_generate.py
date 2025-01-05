import openai
import os

# Retrieve OpenAI API key from the environment variable set in GitHub Actions
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define a function to generate a trending topic for kids' animation
def generate_trending_topic():
    prompt = (
        "Generate a trending topic for a kids' animation video that is fun, creative, and engaging. "
        "The topic should involve an exciting adventure or a new creative idea that kids will find interesting and relevant. "
        "Please make it something that will attract attention and spark curiosity."
    )

    try:
        # Use the correct API method for chat-based completions (OpenAI v1.0.0+)
        response = openai.chat.completions.create(
            model="gpt-4o-mini",  # Use GPT-4 model
            prompt=prompt,
            temperature=0.7,  # Creativity level, adjust between 0 and 1
            n=1,  # Generate one result
        )

        # Extract and print the generated topic
        topic = response['choices'][0]['text'].strip()
        return topic

    except Exception as e:
        return f"Error generating topic: {str(e)}"

# Call the function and print the trending topic
if __name__ == "__main__":
    trending_topic = generate_trending_topic()
    print("Trending Topic for Kids' Animation:", trending_topic)
