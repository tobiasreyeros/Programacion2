b=1000
b2=200
c=0

print('Cuanto dinero desear retirar')
c=int(input())

v=(c%b)

v2=(v//b2)

v=(c//b)
print('Recibira su monto de ',c,'en ',v,' billetes de ',b,' y ',v2,' de ',b2,)

t=(v*b+v2*b2)
r=(c-t)

print('No se pudieron extraer ',r,' billetes')



