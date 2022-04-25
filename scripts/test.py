def check_inputs(val):
    for n in range(2, int(val**0.5) + 1):
        print(n)
        if val % n == 0:
            print("Not prime")
        else:
            print("Prime number")
            pass


def main():
    check_inputs(49)
