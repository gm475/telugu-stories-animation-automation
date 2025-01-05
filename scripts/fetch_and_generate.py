import os
from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")  # Retrieve the API key from environment variables
)

# Define the function to generate a trending topic for kids' animation
def generate_trending_topic(topic):
    prompt = (
        f"Write a short, fun Telugu kids' story about '{topic}'. Make it adventurous, creative, and engaging "
        "for children, with a fun and exciting narrative that will captivate their attention."
    )

    try:
        # Use the correct method with the client and model (gpt-4o-mini)
        completion = client.chat.completions.create(
            model="gpt-4o-mini",  # Specify the gpt-4o-mini model
            messages=[
                {"role": "system", "content": "You are a helpful assistant that generates engaging stories."},
                {"role": "user", "content": prompt}
            ]
        )

        # Extract and return the generated story
        story = completion.choices[0]['message']['content']
        return story

    except Exception as e:
        return f"Error generating story: {str(e)}"

# Example trending topic from Chhota Bheem
topic = "Chhota Bheem - New Year Party with Bheem & Friends | Cartoons for Kids"

# Call the function and print the generated story
if __name__ == "__main__":
    kids_story = generate_trending_topic(topic)
    print("Generated Kids' Story:\n", kids_story)
