class Test():
    def __init__(self):
        self.paraname = "bla1"
        self.blub = 23


if __name__ == "__main__":
    a = Test()
    print(a.paraname)
    print(a.paraname.__name__)
