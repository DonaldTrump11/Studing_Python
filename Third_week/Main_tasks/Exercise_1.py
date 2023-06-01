class FileReader:
    def __init__(self, input_str):
        self.input_str = input_str
    def input_one(self):
        print(self.input_str)
    def read(self):
        try:
            with open(self.input_str, 'r') as file:
                reader = file.read()
                return reader
        except:
            return ''
