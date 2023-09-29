num = int(input())
ante = 0
suce = 0
if num % 2 == 0:
    ante = num - 1
    suce = num + 2
else:
    ante = num - 2
    suce = num + 1
print(ante,suce)
