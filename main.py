from flask import Flask, render_template,request
import requests

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def get_news():
    titles = []
    description = []
    page_url = []
    image_url = []
    if request.method == "GET":
        data = requests.get(
            "https://newsapi.org/v2/everything?q=Apple&from=2023-05-22&sortBy=popularity&apiKey=API_KEY")
        res = data.json()["articles"]
        

        for i in res:
            titles.append(i["title"])
            description.append(i["description"])
            page_url.append(i["url"])
            image_url.append(i["urlToImage"])

        return render_template('index.html', info=[titles, description, page_url, image_url])
    return render_template('index.html', info=[titles, description, page_url, image_url])



if __name__ == '__main__':
    app.run(debug=True)
