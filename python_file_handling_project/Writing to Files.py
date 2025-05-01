
# Writing to Files
To write data to a file, you need to open the file in write ('w') or append ('a') mode. Writing in write mode ('w') will overwrite the existing contents of the file, while append mode will add new data to the end.

## Writing a String to a File
```python
file = open('output.txt', 'w')
file.write('Hello, world!
')
file.write('This is a new line.
')
file.close()
```

## Writing Multiple Lines to a File
```python
lines = ['First line
', 'Second line
', 'Third line
']
file = open('output.txt', 'w')
file.writelines(lines)
file.close()
```
