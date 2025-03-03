import sys

class RedicetStdoutToFile:
    def __enter__(self):
        self.old_stdout = sys.stdout
        self.file = open('output2.txt','w')
        sys.stdout = self.file
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        sys.stdout = self.old_stdout
        self.file.close()
        if(exc_type):
            print(f"Error occurred: {exc_value}")
        return False
    
with RedicetStdoutToFile() as r:
    print('This is will be written in to output2.txt')
print("This will also be printed on the console after file writing.")