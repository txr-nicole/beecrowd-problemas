a, b , c = list(map(int,input().split()))
s = (a + b + c) / 2
area = (s*(s-a)*(s-b)*(s-c))**0.5
print(f'{area:.3f} m2')
