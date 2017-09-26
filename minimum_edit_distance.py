dist = 0
str1 = "INTENTION"
str2 = "EXECUTION"
n = len(str1)
m = len(str2)
# lookup = dict()
lookup = []


def distance(l1, l2):
    global dist
    global lookup
    if l1 == 0 and l2 == 0:
        return 0
    if l1 == 0:
        return l2
    if l2 == 0:
        return l1

    for i in range(1, l1 + 1):
        for j in range(1, l2 + 1):
            if lookup[i][j] == -1:
                d1 = distance(i - 1, j) + 1
                d2 = distance(i, j - 1) + 1
                d3 = distance(i - 1, j - 1) + (2 if str1[i - 1] != str2[j - 1] else 0)
                dist = min(d1, d2, d3)
                lookup[i][j] = dist
            else:
                dist = lookup[i][j]

    return dist


if __name__ == '__main__':
    lookup = [[-1 for j in range(m + 1)] for i in range(n + 1)]

    # for i in range(n+1):
    #     lookup1[i][0] = 0
    # for j in range(m+1):
    #     lookup1[0][j] = 0

    print(distance(n, m))
    pass
