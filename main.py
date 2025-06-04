from calculator import check_valid
class Calculator:
    def __init__(self):
        self.isrunning = True
    def run(self):
        while self.isrunning:
            a = input("Input the first number: ")
            o = input("Input the operator: ")
            b = input("Input the second number: ")
            if not check_valid(a,o,b):
                print("Something went wrong!")
                continue
if __name__ == "__main__":
    APP = Calculator()
    APP.run()