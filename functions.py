def read_csv(path):
  import csv
  record = {}
  table = []

  with open(path,'r', encoding='utf8',errors='ignore') as csvfile:
    reader = csv.reader(csvfile,delimiter=',')
    header = next(reader)
    for row in reader:
      iterable = zip(header,row)
      record = {key: value for key, value in iterable}
      table.append(record)
    return table

def add_col(list,new_column):
  for i in list:
    i[new_column] = ''
  return list

def write_csv(path,list_of_dicts):
  import csv
  field = list_of_headers(list_of_dicts)
  with open(path,'w',newline='') as file:
    d_writer = csv.DictWriter(file,fieldnames=field)
    d_writer.writeheader()
    d_writer.writerows(list_of_dicts)

def write_csv(path,list_of_dicts):
  import csv

  field = list_of_headers(list_of_dicts)
  with open(path,'w',newline='') as file:
    d_writer = csv.DictWriter(file,fieldnames=field)
    d_writer.writeheader()
    d_writer.writerows(list_of_dicts)

def list_of_headers(list_of_dicts):
    result = []
    dict_keys = list_of_dicts[1].keys()
    for i in dict_keys:
        result.append(i)
    return result    