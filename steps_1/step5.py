class Simple:
    count = 0

    def __init__(self):
        type(self).count += 1


if __name__ == "__main__":
    a = Simple()  # 3
    b = Simple()  # 3
    c = Simple()  # 3
    print(b.count)  # 3
    print(Simple.count)  # 3
    print(c.count)  # 3
