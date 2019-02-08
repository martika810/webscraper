#!/usr/bin/env python

import sys
import os
from flask_bootstrap import Bootstrap
from flask import Flask, render_template
from webscraper.progress import Progress
from webscraper.crawling_threading import CrawlingThreading

def main():
    if(getattr(sys, 'frozen', False)):
        template_folder = os.path.join(sys._MEIPASS,'webscraper/templates')
        static_folder = os.path.join(sys._MEIPASS,'static')
        app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)
    else:
        app= Flask(__name__, template_folder='webscraper/templates')

    Bootstrap(app)
    progress = Progress()
    progress.init()

    @app.route('/')
    def app_entrypoint():
        global progress
        progress_result = progress.read_progress()
        return render_template('index.html', progress=progress_result)

    @app.route('/scrape')
    def scrape_beerwulf():
        global progress
        progress_result = progress.read_progress()
        CrawlingThreading('')
        return render_template('index.html', progress=progress_result )

    app.run(debug=True)


if(getattr(sys, 'frozen', False)):
    template_folder = os.path.join(sys._MEIPASS,'webscraper/templates')
    static_folder = os.path.join(sys._MEIPASS,'static')
    app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)
else:
    app= Flask(__name__, template_folder='webscraper/templates')

Bootstrap(app)
progress = Progress()
progress.init()

@app.route('/')
def app_entrypoint():
    global progress
    progress_result = progress.read_progress()
    return render_template('index.html', progress=progress_result)

@app.route('/scrape')
def scrape_beerwulf():
    global progress
    progress_result = progress.read_progress()
    CrawlingThreading('')
    return render_template('index.html', progress=progress_result )

if __name__ == '__main__':
    app.run(debug=True)