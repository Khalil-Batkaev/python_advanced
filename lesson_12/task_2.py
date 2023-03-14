class Factorial:
    def __init__(self, *args):
        match len(args):
            case 1:
                self.stop = args[0]
                self.start = self.step = 1
            case 2:
                self.start, self.stop = args
                self.step = 1
            case 3:
                self.start, self.stop, self.step = args
        self.result = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.result = 1
        for i in range(2, self.start):
            self.result *= i

        while self.start <= self.stop:
            self.result *= self.start
            self.start += self.step
            return self.result
        raise StopIteration


if __name__ == '__main__':
    f = Factorial(5, 10, 2)
    for num in f:
        print(num)
