import requests
from bs4 import BeautifulSoup

def fetch_youtube_trends():
    # URL for the YouTube trending page for India (can adjust region if needed)
    url = "https://www.youtube.com/feed/trending?bp=6gQJRkVleHBsb3Jl"

    # Make the request to the YouTube trending page
    response = requests.get(url)
    print(f"Response Content (first 500 characters): {response.text[:500]}")
    # Parse the page content with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all the video titles in the page
    video_titles = []

    # YouTube video titles are typically inside <a> tags with the 'yt-simple-endpoint' class
    for video in soup.find_all('a', class_='yt-simple-endpoint style-scope ytd-video-renderer'):
        title = video.get('title')
        if title and ('animation' in title.lower() or 'kids' in title.lower() or 'cartoon' in title.lower()):
            video_titles.append(title)

    return video_titles

# Fetch the trending kids' animation topics
topics = fetch_youtube_trends()

# Print out the top trending topics related to animation for kids
if topics:
    print("Top trending kids' animation topics:")
    for idx, topic in enumerate(topics, 1):
        print(f"{idx}. {topic}")
else:
    print("No relevant trending topics found.")