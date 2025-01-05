import openai
from pytrends.request import TrendReq

openai.api_key = "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"

def fetch_trending_topics():
    pytrends = TrendReq(hl="en-US", tz=360)
    trending_searches = pytrends.trending_searches(pn="india")
    return trending_searches[0][0]  # Return top trending topic

def generate_script(topic):
    prompt = f"Write a short, fun Telugu kids' story about '{topic}'."
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=500,
        temperature=0.7
    )
    return response.choices[0].text.strip()

topic = fetch_trending_topics()
script = generate_script(topic)

with open("output/script.txt", "w", encoding="utf-8") as f:
    f.write(script)
