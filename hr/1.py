import sys


def main():
    num = int(input())
    dct = dict()
    for i in range(num):
        key, value = input().split()
        dct[key] = value


if __name__ == "__main__":
    main()