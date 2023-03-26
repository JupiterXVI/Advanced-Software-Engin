from threading import Thread

class Pint():
    def __init__(self):
        self.printed = False

    def printer(self):
        for x in range(7):
            print(x)
        self.printed = True
    
    def do(self):
        print("vor thread")
        Thread(target=self.printer).start()
        print("nach thread")

        while not self.printed:
            print("in while")

        print("end")

if __name__ == '__main__':
    Pint().do()