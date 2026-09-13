from flask import Flask, render_template, request
import feedparser

app = Flask(__name__)

sources = {
    "World": [
        "https://feeds.bbci.co.uk/news/world/rss.xml",
        "https://www.thehindu.com/news/international/feeder/default.rss",
        "https://rss.nytimes.com/services/xml/rss/nyt/World.xml",
        "https://www.theguardian.com/world/rss",
        "http://timesofindia.indiatimes.com/rssfeeds/296589292.cms",
        "https://www.aljazeera.com/xml/rss/all.xml"
    ],
    "Sports": [
        "https://rss.nytimes.com/services/xml/rss/nyt/Sports.xml",
        "https://feeds.bbci.co.uk/sport/rss.xml",
        "https://www.thehindu.com/sport/football/feeder/default.rss",
        "https://www.thehindu.com/sport/motorsport/feeder/default.rss",
        "https://rss.nytimes.com/services/xml/rss/nyt/Hockey.xml",
        "http://timesofindia.indiatimes.com/rssfeeds/4719148.cms",
        "https://www.theguardian.com/uk/sport/rss"
    ],
    "Technology": [
        "https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml",
        "https://feeds.bbci.co.uk/news/technology/rss.xml",
        "https://rss.nytimes.com/services/xml/rss/nyt/PersonalTech.xml",
        "http://timesofindia.indiatimes.com/rssfeeds/66949542.cms",
        "https://www.theguardian.com/uk/technology"
    ],
    "Business": [
        "https://rss.nytimes.com/services/xml/rss/nyt/Business.xml",
        "https://rss.nytimes.com/services/xml/rss/nyt/Economy.xml",
        "https://www.thehindu.com/business/Industry/feeder/default.rss",
        "https://www.thehindu.com/business/markets/feeder/default.rss",
        "http://feeds.bbci.co.uk/news/business/rss.xml",
        "http://timesofindia.indiatimes.com/rssfeeds/1898055.cms"


    ]
}


def fetch_news(category=None, keyword=""):
    headlines = []
    if category and category in sources:
        urls = sources[category]
    else:
        # If no category, show all
        urls = [url for group in sources.values() for url in group]

    for url in urls:
        feed = feedparser.parse(url)
        source = feed.feed.get('title', 'Unknown Source')
        for entry in feed.entries:  # show more news
            title = entry.get('title', 'No Title')
            published = entry.get('published', 'No Date')
            link = entry.get('link', '#')
            if keyword.lower() in title.lower():
                headlines.append({"source": source, "title": title, "published": published, "link": link})
    return headlines

@app.route("/")
def home():
    return render_template("index.html", headlines=fetch_news())
@app.route("/category/<name>")
def category(name):
    return render_template("index.html", headlines=fetch_news(category=name), category=name)

@app.route("/search")
def search():
    keyword = request.args.get("keyword", "")
    return render_template("index.html", headlines=fetch_news(keyword=keyword), keyword=keyword)

if __name__ == "__main__":
    app.run(debug=True)
