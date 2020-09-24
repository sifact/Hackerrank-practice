def simpleArraySum(ar):

    # Write your code here.
    the_sum = 0
    for i in ar:
        the_sum += i
    return the_sum


ar_count = int(input())
ar = list(map(int, input().rstrip().split()))
print(simpleArraySum(ar))

    