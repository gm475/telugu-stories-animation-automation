import os
from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")  # Retrieve the API key from environment variables
)

# Define the function to generate a trending topic for kids' animation
def generate_trending_topic():
    prompt = (
        "Generate a trending topic for a kids' animation video that is fun, creative, and engaging. "
        "The topic should involve an exciting adventure or a new creative idea that kids will find interesting and relevant. "
        "Please make it something that will attract attention and spark curiosity."
    )

    try:
        # Use the correct method with the client and model (gpt-4o-mini)
        completion = client.chat.completions.create(
            model="gpt-4o-mini",  # Specify the gpt-4o-mini model
            messages=[
                {"role": "system", "content": "You are a helpful assistant that generates trending topics."},
                {"role": "user", "content": prompt}
            ]
        )

        # Extract the topic from the response
        topic = completion['choices'][0]['message']['content']
        return topic

    except Exception as e:
        return f"Error generating topic: {str(e)}"

# Call the function and print the trending topic
if __name__ == "__main__":
    trending_topic = generate_trending_topic()
    print("Trending Topic for Kids' Animation:", trending_topic)
