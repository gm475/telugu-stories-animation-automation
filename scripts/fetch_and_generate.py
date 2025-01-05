from pytrends.request import TrendReq

def fetch_indian_kids_animation_topic():
    pytrends = TrendReq(hl="en-US", tz=360)
    trending_searches = pytrends.trending_searches(pn="india")
    
    # List of keywords related to Indian animation and languages
    animation_keywords = ["animation", "cartoon", "2D", "3D", "kids story", "children", "telugu", "hindi", "short films", "animated series"]
    
    for topic in trending_searches[0]:
        if any(keyword.lower() in topic.lower() for keyword in animation_keywords):
            return topic  # Return the first matching topic

    return "No relevant Indian kids' animation topic found"  # If no match found

topic = fetch_indian_kids_animation_topic()

print(f"Top trending Indian kids' animation topic: {topic}")