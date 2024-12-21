import sys


def summ(num):
    lst_one_nums = list()
    for i in range(num):
        lst_one_nums.append(1)
    print(*lst_one_nums, sep=" + ")


def lexicographically(num):
    first_num = 2
    while first_num != num:
        lst = [1]
        lst[0] = first_num
        while sum(lst) != num:
            lst.append(1)
        print(*lst, sep=" + ")
        lst.clear()
        first_num += 1


def main():
    num = int(input())
    summ(num)
    lexicographically(num)
    print(num)
    

if __name__ == '__main__':
    main()