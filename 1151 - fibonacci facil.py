seq = int(input())
count = 0
n1 = 0
n2 = 1
soma = n1 + n2
print(n1, end="")
print(f" {n2}", end="")
while count <= seq - 3:
    soma = n1 + n2
    n1 = n2
    n2 = soma
    print(f" {soma}", end="")
    count += 1
print("")
    
    
    
    
