from pytrends.request import TrendReq

def fetch_indian_kids_animation_topic():
    pytrends = TrendReq(hl="en-US", tz=360)
    trending_searches = pytrends.trending_searches(pn="india")
    
    # Focus on kids' content, animation, Telugu/Hindi
    animation_keywords = [
        "kids animation", "2D animation", "3D animation", "cartoon", "children story", 
        "Chhota Bheem", "Bal Ganesh", "Doraemon", "Krishna", "Motu Patlu", "animated series",
        "telugu animation", "hindi animation", "kids cartoon"
    ]
    
    for topic in trending_searches[0]:
        if any(keyword.lower() in topic.lower() for keyword in animation_keywords):
            return topic  # Return the first matching topic

    return "No relevant Indian kids' animation topic found"

topic = fetch_indian_kids_animation_topic()

print(f"Top trending Indian kids' animation topic: {topic}")
