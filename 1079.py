n = int(input())
contador = 0
while contador < n:
    x = input().split()
    vr1, vr2, vr3 = x
    mp = ((float(vr1)*2) + (float(vr2)*3) + (float(vr3)*5))/(2+3+5)
    
    contador = contador + 1
    print("{:.1f}".format(mp))
