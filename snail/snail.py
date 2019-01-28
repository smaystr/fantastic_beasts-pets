n = int(input())
m = n // 2 + n % 2
a = [[0 for j in range(n)] for i in range(n)]
count = 0
for x in range(n):
    for i in range(n):
        for j in range(n):
            if (m > i == x) & (n - x > j >= x):
                count += 1
                a[i][j] = count
    for i in range(n):
        for j in range(n):
            if (n - x > i > x) & (m <= j == n - 1 - x):
                count += 1
                a[i][j] = count
    for i in range(n):
        for j in range(n):
            if (m <= i == n - 1 - x) & (x <= j < n - 1 - x):
                count += 1
                a[i][-2 - j] = count
    for i in range(n):
        for j in range(n):
            if (x < i < n - 1 - x) & (m > j == x):
                count += 1
                a[-1 - i][j] = count
for i in range(n):
    for j in range(n):
        print(a[i][j], end='\t')
    print()
