sobrinhos = input().split()
H = int(sobrinhos[0])
Z = int(sobrinhos[1])
L = int(sobrinhos[2])
if ((H < Z and H > L) or (H>Z and H<L)):
    print("huguinho")
elif ((Z<H and Z>L)or(Z>H and Z<L)):
    print("zezinho")
else:
    print("luisinho")
