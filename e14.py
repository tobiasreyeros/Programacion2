matriz = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12],
          [13,14,15,16]]
contador = 1
suma_principal = 0
multi_principal = 1
suma_contra = 0
multi_contra = 1

print("Numeros en la matriz")
for i in range(4):
    for j in range(4):
        print(f"{matriz[i][j]:2}")
    
        if i == j:
            suma_principal += matriz[i][j]
            multi_principal *= matriz[i][j]
            
        if i + j == 3:
            suma_contra += matriz[i][j]
            multi_contra *= matriz[i][j]
    print() 


print(f"Diagonal Principal: suma{suma_principal}, multiplicación = {multi_principal}")
print(f"Contra Diagonal: suma{suma_contra}, multiplicación = {multi_contra}")