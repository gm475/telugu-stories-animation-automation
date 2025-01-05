import requests
from bs4 import BeautifulSoup

def fetch_youtube_trends_from_channel(channel_url):
    # Request the YouTube channel's video page
    response = requests.get(channel_url)
    
    # Parse the HTML content of the channel page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract video titles from the page
    video_titles = []

    # Find all <a> tags containing video titles or links
    for video in soup.find_all('a', {'id': 'video-title'}):
        title = video.get('title')
        if title and ('animation' in title.lower() or 'kids' in title.lower() or 'cartoon' in title.lower()):
            video_titles.append(title)

    return video_titles

# Example YouTube Channel URLs for kids' animation (can use popular channels like Chhota Bheem, etc.)
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
