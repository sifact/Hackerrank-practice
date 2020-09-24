def compareTriplets(a, b):
    a_score, b_score = 0, 0

    for i in range(len(a)):
        if a[i] > b[i]:
            a_score += 1
        elif b[i] > a[i]:
            b_score += 1

    return a_score, b_score


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

# solution 2:

def solve(a0, a1, a2, b0, b1, b2):
    alice = [a0, a1, a2]
    bob = [b0, b1, b2]
    score = [0, 0]
    for a, b in zip(alice, bob):
        if a > b:
            score[0]+= 1
        elif b > a:
            score[1]+=1
    return score
