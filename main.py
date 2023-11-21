#Paso 1. Instalamos la libreria pandas
#   - Ir al menú File->Settings: buscar la opción "Python Interpreter"
#   - Agregar la librería pandas


import pandas as pd



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Importar datos en formato csv.
    d = pd.read_csv('students.csv')

    # Leer los primeros registros
    print(d.head())
    print()
    print()
    print(d[0:5]['AREA NAME'])
    print()
    print()
    # Partir los datos en dos grupos. Concatenarlos por posición.

    p1 = d[['AREA NAME', 'COUNTY']][0:2]
    print(p1)

    print()
    print()
    p2 = d[['AREA NAME', 'COUNTY']][2:5]
    print(p2)

    print()
    print()
    n = pd.concat([p1,p2])
    print(n)
    n.to_csv('sample_data1.csv')

