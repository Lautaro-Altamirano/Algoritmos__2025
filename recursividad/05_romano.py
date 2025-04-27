def convertir_a_decimal(romano):
    
    letras = {
            "I" : 1,"V" : 5,"X" : 10,"L" : 50,"C" : 100,"D" : 500,"M" : 1000
            }
    if len(romano) == 1:
        return letras[romano]

    if letras[romano[0]] >= letras[romano[1]]:
        return letras[romano[0]] + convertir_a_decimal(romano[1:])
    else:  
        return - letras[romano[0]] + convertir_a_decimal(romano[1:])
    
romano = input("Ingresar número Romano: ")
romano = romano.upper()
resultado = convertir_a_decimal(romano)
print(f"Número decimal: {resultado}")