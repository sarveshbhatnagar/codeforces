num = int(input())


def dist(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])


answers = []

for i in range(num):
    inp = list(map(int, input().split()))
    p1 = (1, 1)
    p2 = (1, inp[1])
    p3 = (inp[0], 1)
    p4 = (inp[0], inp[1])
    points = [p1, p2, p3, p4]

    distFromPerson = dict()
    distFromPoint = dict()
    for i in range(len(points)):
        distFromPerson[i] = dist((inp[2], inp[3]), points[i])

    selectPoint = max(distFromPerson, key=lambda x: distFromPerson[x])

    for i in range(len(points)):
        distFromPoint[i] = dist(points[selectPoint], points[i])

    maxval = -1
    p = 0
    for i in range(len(points)):
        if(distFromPoint[i] + distFromPerson[i] > maxval):
            maxval = distFromPoint[i] + distFromPerson[i]
            p = i

    answer = [points[p][0], points[p][1],
              points[selectPoint][0], points[selectPoint][1]]
    answer = [str(i) for i in answer]
    answer = " ".join(answer)

    answers.append(answer)

for i in answers:
    print(i)
