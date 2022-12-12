from csv import writer, DictReader
  

def add_expense(name, date, value):
    with open('storage.csv', 'a', newline='') as f:
        writer_object = writer(f)
        writer_object.writerow((name, date, value))
        f.close()

def get_data() -> list(dict()):
    with open('storage.csv', newline='') as f:
        return list(DictReader(f))
