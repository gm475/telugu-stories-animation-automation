from pytrends.request import TrendReq

# Initialize the pytrends request
pytrends = TrendReq(hl='en-US', tz=360)

# Define the keywords related to kids' animation
keywords = ['kids animation', 'cartoon story', 'children animation', 'animation series for kids', 'animated adventure']

# Get trending search topics for the defined keywords
pytrends.build_payload(keywords, cat=0, timeframe='now 7-d', geo='US', gprop='')

# Get the interest over time data
trending_data = pytrends.interest_over_time()

# Print trending topics for kids' animation
if not trending_data.empty:
    print("Trending Kids Animation Topics Over the Past Week:")
    for keyword in keywords:
        print(f"Topic: {keyword}")
        print(trending_data[keyword].tail(1))  # Display the most recent data for each keyword
else:
    print("No trending data available for the specified topics.")
