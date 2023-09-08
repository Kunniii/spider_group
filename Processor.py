from os import listdir
from os.path import abspath, join
from threading import Thread
from bs4 import BeautifulSoup
from pandas import DataFrame
import pickle


class Processor:
    columns = ["RollNumber", "Surname", "Middle_name", "Given_name"]
    data = []
    workers = []
    files = []

    def __init__(self, folder: str, worker: int) -> None:
        self.folder = folder
        self.worker = worker
        self.files = [abspath(p) for p in [join(folder, f)
                                           for f in listdir(folder)]]

    def parse_table(self, file) -> list:
        data = []
        with open(file, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f.read(), "html.parser")
        table_rows = soup.find_all("tr")

        for row in table_rows:
            temp = []
            for td in row:
                temp.append(td.text)
            data.append(temp[-4:])
        return tuple(data)

    def process(self):
        while self.files:
            file = self.files.pop(0)
            self.data += self.parse_table(file)

    def run_extract_data(self):
        for i in range(self.worker):
            worker = Thread(target=self.process)
            worker.start()
            self.workers.append(worker)

        for worker in self.workers:
            worker.join()

    def to_pickle(self, file):
        with open(abspath(file), "wb") as f:
            pickle.dump(self.data, f)

    def load_pickle(self, file):
        """
        Load data from Pickle file.
        """
        with open(abspath(file), "rb") as f:
            self.data = pickle.load(f)
