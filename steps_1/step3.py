class Check:
    count = 0

    def __init__(self):
        Check.count += 1


if __name__ == "__main__":
    a = Check()  # 4
    b = Check()  # 4
    c = Check()  # 4
    d = Check()  # 4
    print(c.count)  # 4
    print(Check.count)  # 4
