
# File Modes: Understanding How Files are Opened
The mode in which a file is opened determines how the file is accessed and whether it is read, written to, or appended to. Here is a quick summary of the most commonly used modes:

- 'r': Read mode – Opens the file for reading. The file must exist.
- 'w': Write mode – Opens the file for writing. If the file exists, it will be overwritten. If it doesn’t exist, it will be created.
- 'a': Append mode – Opens the file for appending data to the end. If the file doesn’t exist, it will be created.
- 'b': Binary mode – Opens the file in binary mode. Used for reading or writing binary files like images or audio files.
- 'x': Exclusive creation mode – Opens the file for writing, but the file must not exist. If it exists, Python will raise an error.
- 'rb': Read binary mode – Used to read binary files (e.g., images, videos).
