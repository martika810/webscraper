import pickle


class Progress:
    def __init__(self):
        self.filename = "progress.pickle"

    def save_number_items_scraped_so_far(self, number):
        progress = pickle.load(open(self.filename, "rb"))
        progress['items_scraped'] = number
        pickle.dump(progress, open(self.filename, "wb"))

    def save_total_number_items(self,number):
        progress = pickle.load(open(self.filename, "rb"))
        progress['total'] = number
        pickle.dump(progress, open(self.filename, "wb"))

    def save_items_scraped(self,scraped_items):
        progress = pickle.load(open(self.filename, "rb"))
        progress['items'] = scraped_items
        pickle.dump(progress, open(self.filename, "wb"))

    def add_item_scraped(self, item):
        progress = pickle.load(open(self.filename, "rb"))
        progress['items'].append(item)
        pickle.dump(progress, open(self.filename, "wb"))

    def read_progress(self):
        try:
            progress = pickle.load(open(self.filename, "rb"))
            return progress
        except (OSError, IOError) as e:
            self.init()
            progress = pickle.load(open(self.filename, "rb"))
            return progress


    def read_number_items_scraped_so_far(self):
        try:
            progress = pickle.load(open(self.filename, "rb"))
            return progress['items_scraped']
        except (OSError, IOError) as e:
            self.init()
            progress = pickle.load(open(self.filename, "rb"))
            return progress['total']

    def read_total_number_items(self):
        try:
            progress = pickle.load(open(self.filename, "rb"))
            return progress['total']
        except (OSError, IOError) as e:
            self.init()
            progress = pickle.load(open(self.filename, "rb"))
            return progress['total']

    def init(self):
        progress = {}
        progress['items_scraped'] = 0
        progress['total'] = 0
        progress['items'] = []
        pickle.dump(progress, open("progress.pickle", "wb"))