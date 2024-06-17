n1 = input()
n2 = input()

result = ""

for i in range(len(n1) - 1, -1, -1):
    result += n1[i] + n2[i]

result = int(result)

print(result)
