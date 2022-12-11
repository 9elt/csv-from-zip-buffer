import requests
import zipfile
import io
import csv


#   requests a zip file to a url and
#   returns the utf-8 decoded targeted file
def request_zip_file(settings):
    response = requests.get(settings.url)
    if response.status_code != 200:
        return response.status_code

    zip_archive = zipfile.ZipFile(io.BytesIO(response.content))

    file_bytes = zip_archive.read(settings.file)
    return file_bytes.decode("utf-8", errors='ignore')


#   opens a csv file from a zip file buffer and
#   returns the parsed data as a 2d array
def csv_from_zip_buffer(settings):
    data = []
    rows = request_zip_file(settings).split("\n")
    for cols in rows: data.append(cols.split(settings.delimiter))
    return data


#   csv_from_zip_buffer() settings
class Settings:
    def __init__(self, delimiter, target_url, target_file):
        self.delimiter = delimiter
        self.url = target_url
        self.file = target_file


#   example
my_data = csv_from_zip_buffer(Settings(
    ",",
    "https://mysite.com/myfile.zip",
    "target_file_name.csv"
))

print(my_data[0][0])
