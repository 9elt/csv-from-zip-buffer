# csv from zip buffer
get csv data from a zip file buffer.

> Requires the [requests](https://pypi.org/project/requests/) module.

## example

```python
my_data = csv_from_zip_buffer(Settings(
    ",", # csv delimiter
    "https://mysite.com/myfile.zip", # zip file url
    "target_file_name.csv" # targeted file name inside the zip archive
))

print(my_data[0][0])
# output: my first clumn title
```
