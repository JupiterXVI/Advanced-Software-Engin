class Test():

    def skip():
        if True:
            print("1")
            if True:
                print("2")
                
            print("3")
        print("4")

if __name__ == "__main__":
    Test.skip()