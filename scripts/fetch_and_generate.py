import os
from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")  # Retrieve the API key from environment variables
)

# Define the function to generate a trending topic for kids' animation
def generate_story(topic):
    prompt = (
        f"Write a short, fun Telugu kids' story about '{topic}'. Make it adventurous, creative, and engaging "
        "for children, with a fun and exciting narrative that will captivate their attention."
    )

    try:
        # Use the correct method with the client and model (gpt-4o-mini)
        completion = client.chat.completions.create(
            model="gpt-4o-mini",  # Specify the gpt-4o-mini model
            messages=[
                {"role": "developer", "content": "You are a helpful assistant that generates engaging stories."},
                {"role": "user", "content": prompt}
            ]
        )

        # Extract and print the generated story
        story = completion.choices[0].message
        return story

    except Exception as e:
        return f"Error generating topic: {str(e)}"

# Call the function and print the trending topic
if __name__ == "__main__":
    topic = "Chhota Bheem - New Year Party with Bheem & Friends"
    kids_story = generate_story(topic)
    print("Story for Kids' Animation:", kids_story)