import csv

class SimpleIterator:
    def __init__(self, annotation_path: str) -> None:
        self.ap = annotation_path
        self.list = self.load_images()
        self.limit = len(self.list)
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.limit:
            result = self.list[self.counter]
            self.counter += 1
            return result
        else:
            raise StopIteration

    def load_images(self) -> list:
        with open(self.ap, mode='r', encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)
            return [row for row in reader]
