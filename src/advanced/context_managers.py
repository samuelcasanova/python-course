from contextlib import contextmanager
from os import path

dir_path = path.dirname(__file__)
data_path = path.join(dir_path, '../data')

# Applicable to files, db connections, thread locks, network connections, etc.
with open(path.join(data_path, 'sample.txt'), 'w') as file:
    file.write("This is a sample text file.")

# equivalent to:
file = open(path.join(data_path, 'sample.txt'), 'w')
try:
    file.write("This is a sample text file.")
finally:
    file.close()


class CustomFileWriterContextManagerClass:
    def __init__(self, filename):
        self.filename = filename
        self.file = None
        print(f"CustomFileWriterContextManager initialized for file: {self.filename}")

    def __enter__(self):
        print("Entering the context")
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context")
        if self.file:
            self.file.close()
        if exc_type:
            print(f"An exception occurred but the file was closed: {exc_value}")


with CustomFileWriterContextManagerClass(path.join(data_path, 'custom_context.txt')) as custom_file:
    custom_file.write("Writing to file using custom context manager.\n")


@contextmanager
def custom_file_writer_context_manager_function(filename):
    print("Entering the context (function-based)")
    file = open(filename, 'w')
    try:
        yield file
    except Exception as e:
        print(f"An exception occurred but the file was closed: {e}")
    finally:
        print("Exiting the context (function-based)")
        file.close()


with custom_file_writer_context_manager_function(path.join(data_path, 'custom_function_context.txt')) as custom_file:
    custom_file.write("Writing to file using function-based context manager.\n")
