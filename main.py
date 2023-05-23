from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def get_news():
    data = requests.get(
        "https://newsapi.org/v2/everything?q=Apple&from=2023-05-22&sortBy=popularity&apiKey=913dfba790dc45c58171f4a119b33269")
    res = data.json()["articles"]
    titles = []
    description = []
    page_url = []
    image_url = []

    for i in res:
        titles.append(i["title"])
        description.append(i["description"])
        page_url.append(i["url"])
        image_url.append(i["urlToImage"])

    return render_template('index.html', info=[titles, description, page_url, image_url])


if __name__ == '__main__':
    app.run(debug=True)
