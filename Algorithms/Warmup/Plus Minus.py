def plusMinus(arr):
    print("{:.6f}".format(len([1 for i in arr if i > 0]) / n))
    print("{:.6f}".format(len([1 for i in arr if i < 0]) / n))
    print("{:.6f}".format(len([1 for i in arr if i == 0]) / n))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)