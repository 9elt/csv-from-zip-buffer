import requests
import zipfile
from io import BytesIO 
import csv


# Error class
class RequestZipError:
    def __init__(self, code, msg):
        self.code = code
        self.msg = msg


class RequestZip:
    def __init__(self, delimiter, target_url, target_file):
        self.delimiter = delimiter
        self.url = target_url
        self.file = target_file

    #   opens a csv file from a zip file buffer and
    #   returns the a 2d array of the parsed data 
    def get(self):
        res = self.request_zip_file()
        if isinstance(res, RequestZipError):
            return res

        data = []
        try:
            rows = res.split("\n")
            for cols in rows: data.append(cols.split(self.delimiter))
        except:
            return RequestZipError(500, "failed parsing csv data")

        return data

    #   requests a zip file to a url and
    #   returns the utf-8 decoded targeted file
    def request_zip_file(self):
        try:
            response = requests.get(self.url)
        except:
            return RequestZipError(500, "failed request")

        if response.status_code != 200:
            return RequestZipError(response.status_code,"failed request with status code")

        try:
            zip_archive = zipfile.ZipFile(BytesIO(response.content))
        except:
            return RequestZipError(500, "failed opening zip file")

        try:
            file_bytes = zip_archive.read(self.file)
        except:
            return RequestZipError(500, "failed reading zip file")

        return file_bytes.decode("utf-8", errors='ignore')


#   example
res = RequestZip(
    ",", # csv delimiter
    "https://mysite.com/myfile.zip", # zip file url
    "target_file_name.csv" # targeted file name inside the zip archive
).get()

if isinstance(res, RequestZipError):
    print(f"{res.code} - {res.msg}")
else:
    print(res[0][0])

# expected output: my first column heading