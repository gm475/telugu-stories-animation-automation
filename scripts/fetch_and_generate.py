import os
from selenium import webdriver  # type: ignore
from selenium.webdriver.common.by import By  # type: ignore
from selenium.webdriver.chrome.options import Options  # type: ignore
from selenium.webdriver.chrome.service import Service  # type: ignore
from webdriver_manager.chrome import ChromeDriverManager  # type: ignore
import time
from openai import OpenAI  # type: ignore

# Function to fetch YouTube trends
def fetch_youtube_trends_from_channel(channel_url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(channel_url)
    time.sleep(5)

    video_titles = []
    video_elements = driver.find_elements(By.XPATH, '//a[@id="video-title"]')
    for video in video_elements:
        title = video.get_attribute('title')
        if title and ('animation' in title.lower() or 'kids' in title.lower() or 'cartoon' in title.lower()):
            video_titles.append(title)
    driver.quit()
    return video_titles

# Function to generate stories
def generate_story(topic):
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    prompt = (
        f"Write a short Telugu kids' story about '{topic}'. "
        "Use very simple Telugu language, suitable for young children. "
        "Avoid difficult words and keep the sentences short and easy to understand. "
        "Make sure the story is engaging, fun, and grammatically correct."
    )
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            temperature=0.5,
            messages=[
                {"role": "developer", "content": "You are a helpful assistant that generates engaging stories."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error generating story: {str(e)}"

def refine_story_with_feedback(initial_story):
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    feedback_prompt = (
        "Refine the following Telugu story to make it simpler and ensure there are no grammar mistakes. "
        "Avoid using difficult Telugu words and make the language suitable for children. "
        "Here is the story:\n\n" + initial_story
    )
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a Telugu language expert."},
            {"role": "user", "content": feedback_prompt}
        ]
    )
    return response.choices[0].message.content


# Function to save the story to a file
def save_story_to_file(story, file_path):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(story)

# Main Workflow
if __name__ == "__main__":
    channel_url = "https://www.youtube.com/channel/UCiBigY9XM-HaOxUc269ympg"
    topics = fetch_youtube_trends_from_channel(channel_url)

    if topics:
        print("Trending Topics:")
        for idx, topic in enumerate(topics, 1):
            print(f"{idx}. {topic}")
        
        # Pick the first topic for story generation
        topic = topics[0]
        print(f"\nGenerating story for topic: {topic}")
        kids_story = generate_story(topic)
        refined_story = refine_story_with_feedback(kids_story)

        if refined_story.startswith("Error"):
            print(refined_story)
        else:
            print("\nGenerated Story:\n", refined_story)
            # Save the story to the output folder
            output_file_path = "output/script.txt"
            save_story_to_file(refined_story, output_file_path)
            print(f"\nStory saved to {output_file_path}")
    else:
        print("No relevant topics found.")
