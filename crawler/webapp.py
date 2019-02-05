from flask_bootstrap import Bootstrap
from flask import Flask, render_template
from progress import read_progress,init
from main_beerwulf_scraper import run_beerwulf_scraping

app = Flask(__name__)
Bootstrap(app)
init()

@app.route('/')
def app_entrypoint():
    return render_template('index.html')

@app.route('/scrape')
def scrape_beerwulf():
    progress = read_progress()
    run_beerwulf_scraping()
    return render_template('index.html', progress=progress)


if __name__ == '__main__':
    app.run(debug=True)