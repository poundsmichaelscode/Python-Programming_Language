def announcer (f):

    def wrapper():
        print ("About to run function....")
        f()
        print("Done with the function")

        return wrapper
    
@announcer
def hello():
    print("Hello, world!")
hello()
