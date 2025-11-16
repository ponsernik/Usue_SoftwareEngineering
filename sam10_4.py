class Repeat:
    def __init__(self, n=1):
        self.n = n

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            for i in range(self.n):
                result = func(*args, **kwargs)
            return result

        return wrapper

@Repeat(3)
def say_hello():
    print("Привет!")

@Repeat(2)
def calculate():
    print("5 * 5 = 25")

say_hello()
calculate()