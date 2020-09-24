def timeConversion(s):
    p = s[-2:]
    h = int(s[:2]) % 12 + (p == 'PM') * 12

    print('%02d' % h + s[2:-2])


s = input()
timeConversion(s)

# solution 2:
s = input()
zn = s[-2:]

if zn == "PM" and s[:2] != "12":
    s = str(12 + int(s[:2])) + s[2:]
if zn == "AM" and s[:2] == "12":
    s = "00" + s[2:]
print(s[:-2])

# solution 3:
time = input().strip()
h, m, s = map(int, time[:-2].split(':'))
p = time[-2:]
h = h % 12 + (p == 'PM') * 12
print('%02d:%02d:%02d' % (h, m, s))





