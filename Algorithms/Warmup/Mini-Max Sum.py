def miniMaxSum(arr):
    arr.sort()
    maxi = sum(arr[1:])
    mini = sum(arr[:-1])
    print(mini, maxi)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
