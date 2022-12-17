# csv from zip buffer
get csv data from a zip file buffer without creating temporary files.

> Requires the [requests](https://pypi.org/project/requests/) module.

## example

```python

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

```
