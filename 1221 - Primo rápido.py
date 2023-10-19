def primo(p):
    if p == 0 or p == 1:
        return False
    elif p == 2:
        return True
    else:
        for i in range(2, int(p**0.5) + 1):
            if p % i == 0:
                return False
        return True

casos = int(input())
count = 0
while count < casos:
    num = int(input())
    if primo(num):
        print("Prime")
    else:
        print("Not Prime")
    count += 1
