from pytrends.request import TrendReq

def fetch_trending_topics():
    pytrends = TrendReq(hl="en-US", tz=360)
    trending_searches = pytrends.trending_searches(pn="india")
    return trending_searches[0][0]  # Return top trending topic

topic = fetch_trending_topics()

print(f"Top trending topic in India: {topic}")