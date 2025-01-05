import os
import openai  # Correct import

# Initialize the OpenAI client
openai.api_key = os.environ.get("OPENAI_API_KEY")  # Retrieve the API key from environment variables

# Define the function to generate a kids' animation story
def generate_story(topic):
    prompt = (
        f"Write a short, fun Telugu kids' story about '{topic}'. Make it adventurous, creative, and engaging "
        "for children, with a fun and exciting narrative that will captivate their attention."
    )

    try:
        # Use the correct method with the client and model (gpt-4o-mini)
        completion = openai.ChatCompletion.create(
            model="gpt-4o-mini",  # Specify the gpt-4o-mini model
            messages=[
                {"role": "system", "content": "You are a helpful assistant that generates engaging stories."},
                {"role": "user", "content": prompt}
            ]
        )

        # Extract and print the generated story
        story = completion['choices'][0]['message']['content']
        return story

    except Exception as e:
        return f"Error generating story: {str(e)}"

# Call the function and print the generated story
if __name__ == "__main__":
    # Example of a topic, e.g., a trending topic
    topic = "Chhota Bheem - New Year Party with Bheem & Friends"
    kids_story = generate_story(topic)  # Pass the topic here
    print("Story for Kids' Animation:", kids_story)