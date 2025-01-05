import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from openai import OpenAI

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
        f"Write a short, fun Telugu kids' story about '{topic}'. Make it adventurous, creative, and engaging "
        "for children, with a fun and exciting narrative that will captivate their attention."
    )
    try:
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "developer", "content": "You are a helpful assistant that generates engaging stories."},
                {"role": "user", "content": prompt}
            ]
        )
        return completion.choices[0].message["content"]
    except Exception as e:
        return f"Error generating topic: {str(e)}"

# Main Workflow
if __name__ == "__main__":
    channel_url = "https://www.youtube.com/channel/UCiBigY9XM-HaOxUc269ympg"
    topics = fetch_youtube_trends_from_channel(channel_url)
    
    if topics:
        print("Trending Topics:")
        for idx, topic in enumerate(topics, 1):
            print(f"{idx}. {topic}")
        
        # Pick the first topic for story generation
        selected_topic = topics[0]
        print(f"\nGenerating story for topic: {selected_topic}")
        kids_story = generate_story(selected_topic)
        print("\nGenerated Story:\n", kids_story)
    else:
        print("No relevant topics found.")
