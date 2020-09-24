def birthdayCakeCandles(candles):
    # Write your code here

    print(candles.count(max(candles)))


if __name__ == '__main__':
    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    birthdayCakeCandles(candles)