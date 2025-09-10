class Course:
    def __init__(self, name, code, credits, fee):
        self.name = name
        self.code = code
        self.credits = credits
        self.__fee = fee  

    def get_fee(self):
        return self.__fee

    def display(self):
        print(f"{self.code}: {self.name} | Credits: {self.credits} | Fee: ${self.__fee}")
