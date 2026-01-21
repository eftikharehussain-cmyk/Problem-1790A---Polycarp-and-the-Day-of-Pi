# Problem-1790A---Polycarp-and-the-Day-of-Pi
for _ in range(int(input())):
    target = "314159265358979323846264338327"
    n = input().strip()
    count = 0
    for i in range(len(n)):
        if n[i] == target[i]:
            count += 1
        else:
            break
    print(count)
