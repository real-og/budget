from csv import writer, DictReader
from datetime import datetime
  

def add_expense(name, date, value):
    with open('storage.csv', 'a', newline='') as f:
        writer_object = writer(f)
        writer_object.writerow((name, date, value))
        f.close()

def get_data() -> list(dict()):
    with open('storage.csv', newline='') as f:
        return list(DictReader(f))

def get_data_by_cat(month=0)-> dict():
    if month:
        data = get_data_by_month(month)
    else:
        data = get_data()
    result = dict()
    for item in data:
        if item['Category'] in result:
            result[item['Category']] +=  float(item['Amount'])
        else:
            result[item['Category']] =  float(item['Amount'])
    return result

def get_data_by_month(month)-> list(dict()):
    res = [item for item in get_data() if datetime.strptime(item['Date'], '%Y-%m-%d').date().month == month]
    return res


    

