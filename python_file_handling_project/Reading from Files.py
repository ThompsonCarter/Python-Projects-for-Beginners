
# Reading from Files
Once a file is opened in read mode, you can use various methods to read the data inside the file.

## Reading the Entire File
```python
file = open('data.txt', 'r')
content = file.read()
print(content)
file.close()
```

## Reading Line by Line
```python
file = open('data.txt', 'r')
line = file.readline()
while line:
    print(line, end='')
    line = file.readline()
file.close()
```

## Reading All Lines into a List
```python
file = open('data.txt', 'r')
lines = file.readlines()
for line in lines:
    print(line, end='')
file.close()
```
