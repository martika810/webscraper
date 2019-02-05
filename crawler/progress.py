import pickle

filename = "cookies.pickle"

def save_number_items_scraped_so_far(number):
    progress = pickle.load(open("progress.pickle", "rb"))
    progress['items_scraped'] = number
    pickle.dump(progress, open("progress.pickle", "wb"))

def save_total_number_items(number):
    progress = pickle.load(open("progress.pickle", "rb"))
    progress['total'] = number
    pickle.dump(progress, open("progress.pickle", "wb"))

def read_progress():
    try:
        progress = pickle.load(open("progress.pickle", "rb"))
        return progress
    except (OSError, IOError) as e:
        init()
        progress = pickle.load(open("progress.pickle", "rb"))
        return progress


def read_number_items_scraped_so_far():
    try:
        progress = pickle.load(open("progress.pickle", "rb"))
        return progress['items_scraped']
    except (OSError, IOError) as e:
        init()
        progress = pickle.load(open("progress.pickle", "rb"))
        return progress['total']

def read_total_number_items():
    try:
        progress = pickle.load(open("progress.pickle", "rb"))
        return progress['total']
    except (OSError, IOError) as e:
        init()
        progress = pickle.load(open("progress.pickle", "rb"))
        return progress['total']

def init():
    progress = {}
    progress['items_scraped'] = 0
    progress['total'] = 0
    pickle.dump(progress, open("progress.pickle", "wb"))