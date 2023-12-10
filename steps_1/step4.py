class Simple:
    count = 0

    def __init__(self):
        self.count += 1
        if type(self).count == self.count:
            print(True)
        else:
            print(False)


if __name__ == "__main__":
    a = Simple()
    b = Simple()
    c = Simple()
    print(b.count)  # 1
    print(Simple.count)  # 0
