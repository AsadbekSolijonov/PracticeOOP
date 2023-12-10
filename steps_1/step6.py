class Simple:
    count = 0

    def __init__(self):
        self.count += 1
        Simple.count += 1


if __name__ == "__main__":
    a = Simple()
    b = Simple()
    c = Simple()
    print(Simple.count)
    print(b.count)
    print(c.count)
