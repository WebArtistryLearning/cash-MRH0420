num = int(input())
cnt = []
for i in [25, 10, 5, 1]:
    cnt.append(num // i)
    num -= cnt[-1] * i
print(sum(cnt))
