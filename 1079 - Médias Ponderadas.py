casos = int(input())
count = 0
while count < casos:
    v1,v2,v3 = map(float,input().split())
    media = ((v1*2)+(v2*3)+(v3*5))/(2+3+5)
    print(f"{media:.1f}")
    count += 1
