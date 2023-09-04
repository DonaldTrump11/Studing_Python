class Human :
    def __init__(self, name, age=0):
        self.name = name
        self.age = age
        
    def say_text(self, text) :
        print(text)
    
    def say_name(self):
        self.say_text(f"Hello, Im {self.name}")
        
    def say_how_old(self):
        self.say_text(f"Im {self.age} yers old")
        
