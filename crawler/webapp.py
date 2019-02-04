from flask_bootstrap import Bootstrap
from flask import Flask, render_template
from crawler.main_beerwulf_scraper import run_beerwulf_scraping

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def app_entrypoint():
    return render_template('index.html')

@app.route('/scrape')
def scrape_beerwulf():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)