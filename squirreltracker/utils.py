import csv
from app.models import Squirrelinfo
import os
from squirrel_project.settings import BASE_DIR
from matplotlib import pyplot as plt
import uuid


def get_file_headers(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        headers = next(reader)
        file_headers = []
        for header in headers:
            header = str(header).lower().replace(' ', '').replace('/', '')
            file_headers.append(header)
    return file_headers


def write_export_data(filename):
    squirrelinfos = Squirrelinfo.objects.all().values()
    with open('export' + filename, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(get_file_headers(filename))
        for sqluireel in squirrelinfos:
            print(sqluireel)
            del sqluireel['id']
            writer.writerow([v for k, v in sqluireel.items()])


def write_import_data(filename):
    with open(filename, 'r') as f:
        csv_reader = csv.reader(f)
        headers = next(csv_reader)
        headers_dict = []
        for header in headers:
            header = str(header).lower().replace(' ', '').replace('/', '')
            headers_dict.append(header)
        while True:
            try:
                data = next(csv_reader)
                print(data)
                if not data:
                    print('read file finish')
                    break
            except Exception as e:
                break
            squirrel = {}
            for d in range(len(data)):
                squirrel[headers_dict[d]] = data[d]
            sighting_object = Squirrelinfo.objects.create(**squirrel)
            sighting_object.save()


def stas_png(data):
    figure = plt.figure(figsize=(2, 3))
    labels = [k for k in data.keys()]
    sizes = [v for v in data.values()]
    colors_base = ['red', 'yellowgreen', 'lightskyblue', 'yellow', 'blue', 'black', 'green']
    color = []
    for i in range(len(labels)):
        colors = color.append(colors_base[i])
    explode = [0 for i in range(len(labels))]
    axes = plt.subplot(1, 1, 1)
    axes.pie(sizes,
             explode=explode,
             labels=labels,
             colors=colors,
             autopct='%3.2f%%',
             shadow=False,
             startangle=90,
             pctdistance=0.6)
    filename = uuid.uuid4()
    filename = str(filename)+'.jpg'
    file_path = os.path.join(BASE_DIR, 'app','static', filename)
    plt.savefig(file_path)
    return '/static/' + filename
