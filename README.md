# csv from zip buffer
get csv data from a zip file buffer

## example

```python
my_data = csv_from_zip_buffer(Settings(
    ",",
    "https://mysite.com/myfile.zip",
    "target_file_name.csv"
))

print(my_data[0][0])
```
