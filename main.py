def bin(x):
    x=int(x)
    liczba = ""
    while x != 0:
        liczba = str(x%2) + liczba
        x = int(x/2)
    while len(liczba)<8:
        liczba="0" + liczba
    return liczba

def dez(x):
    i=len(x)-1
    dez = 0
    for n in x:
        dez += int(n) * pow(2,i)
        i -= 1
    return dez

print("Ip:")
ip=input().split(".")

print("Maska:")
maska=input().split(".")

maskaNot=""
odp=[]
for i in range(4):
    maskaZmiana = bin(maska[i])
    for n in range(8):
        if maskaZmiana[n]=="1":
          maskaNot = maskaNot + "0"
        else:
            maskaNot = maskaNot + "1"
    odp.append(int(dez(maskaNot))+int(ip[i]))

fodp=""
for x in range(4):
    fodp = fodp + str(odp[x]) + "."
print(fodp)


