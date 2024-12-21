import sys


def one_summ(num):
    lst = list()
    for i in range(num):
        lst.append(1)
    print(*lst, sep=" + ")

def main():
    num = int(input())
    one_summ(num)
    


if __name__ == '__main__':
    main()