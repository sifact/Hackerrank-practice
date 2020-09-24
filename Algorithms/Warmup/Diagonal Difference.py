def diagonalDifference(arr):
    # Write your code here
    ld, rd = 0, 0
    for i in range(n):
        ld += arr[i][i]
        rd += arr[i][- i - 1]

    return abs(ld - rd)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

