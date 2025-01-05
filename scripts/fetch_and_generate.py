from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def fetch_youtube_trends_from_channel(channel_url):
    # Setup ChromeDriver (make sure you have Chrome installed)
    driver = webdriver.Chrome(ChromeDriverManager().install())
    
    # Open the YouTube channel URL
    driver.get(channel_url)

    # Wait for the page to load (adjust time if necessary)
    time.sleep(5)

    # Get all video titles (they may appear after JavaScript renders them)
    video_titles = []

    # Find all video elements on the page (based on video title 'id')
    video_elements = driver.find_elements(By.XPATH, '//a[@id="video-title"]')

    for video in video_elements:
        title = video.get_attribute('title')
        if title and ('animation' in title.lower() or 'kids' in title.lower() or 'cartoon' in title.lower()):
            video_titles.append(title)
    
    # Close the driver
    driver.quit()

    return video_titles

# Example YouTube Channel URLs for kids' animation (e.g., Chhota Bheem)
channel_urls = [
    "https://www.youtube.com/channel/UCiBigY9XM-HaOxUc269ympg",
]

# Fetch trending kids' animation topics from selected channels
for url in channel_urls:
    print(f"Trending topics from {url}:")
    topics = fetch_youtube_trends_from_channel(url)
    if topics:
        for idx, topic in enumerate(topics, 1):
            print(f"{idx}. {topic}")
    else:
        print("No relevant topics found.\n")
