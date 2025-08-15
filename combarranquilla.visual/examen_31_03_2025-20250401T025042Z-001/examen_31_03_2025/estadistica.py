# construye un programa que, al recibir como datos el peso, la altura, y el genero
#de N personas, que pertenecen a un estado de un pais, obtenga el promedio del peso
# y el promedio de la altura, tanto la poblacion masculino, como la femenina

# esta varible sirve para muvhos ejercicios sirve para que cuando inicies una variable o ciclo 
# en cero te de una comprobacion tambien sirve para evaluar caulquier metodo que realizes como genero numero etc.


# realizar un programa que permita liquidar los salarios de N empleados de una empresa,

# de acuerdo a su cargo con relación a las horas laboradas y el precio de la hora

# se debe pedir la cantidad de empleados a liquidar, se debe solicitar el cargo y la cantidad

# de horas laboradas, al final debe mostrar la cantidad de empleados liquidados por cargos,

# y el total pagado por cargos, rezalizar las validaciones de datos ingresados(Opcional)

# los cargos son: Gerente, Administrativo, Operario

# las tarifas son: Gerente: 65000, Administrativo: 45000, Operarario: 25000

# Buena Suerte!!

comprobar = True

while comprobar == True:
    n = int(input("ingrese la cantida de personas a liquidar: "))

    if n >=0:

        comprobar=False

        horas_gere= 0
        horas_ad= 0
        horas_ope= 0

        cantidad_gere=0
        cantidad_ope=0
        cantidad_ad=0

        for i in range(n):
            horas= int(input("ingrese horas trabajada: "))
            
            comprobar_genero = True
            while comprobar_genero == True:
                cargo= input("ingrese el cargo al que pertenece gerente/administrativo/operarario): ")
                

    #el upper sirve para que cuando el usuario  ingrese la minuscula internamente en el codigo se convierta en mayuscula y el lower para la minuscula
    #forma que da un mejor uso al momento de querer hacer alguna operacion
                if cargo.upper() == "GERENTE":
                    comprobar_genero = False
                    horas_gere +=  horas
                    cantidad_gere +=1
                    pago1 = 65000


                elif cargo.upper() == "ADMINISTRATIVO":
                    comprobar_genero = False
                    horas_ad +=  horas
                    cantidad_ad +=1
                    pago2 = 45000

                elif cargo.upper() == "OPERARIO":
                    comprobar_genero = False
                    horas_ope +=  horas
                    cantidad_ope +=1
                    pago3 = 25000

                else:
                    print("ingrese cargo  correcto")

        promedio_horas_gere = 0
        if cantidad_gere >0:                                           
            promedio_horas_gere = horas_gere * pago1
                
        promedio_horas_ad = 0
        if cantidad_ad >0:
            promedio_horas_ad = horas_ad * pago2

        promedio_horas_ope = 0
        if cantidad_ope >0:                                           
            promedio_horas_ope = horas_ope * pago3


#el \n sirve para no usar varios sprint si mo usar uno solo para llevar un amejor estructura en el codigo
        print("\nde los datos obtenidos para la liquidacion son:"
        "\n promedio liquidacion gerentes:",promedio_horas_gere,
        "\n promedio liquidacion administrativo: ", promedio_horas_ad ,
        "\npromedio liquidacion operarios: " , promedio_horas_ope , 
        "\n"
        "\nGERENTE"
        "\npromedio liquidacion gerente : ", cantidad_gere,
        "\nhoras trabajada promedio gerente:", horas_gere,
        "\n"
        "\nADMINISTRATIVO"
        "\n promedio liquidacion administrativo: ",cantidad_ad, 
        "\nhoras trabajada promedio administrativos", horas_ad,
        "\n"
        "\nOPERARIO"
        "\npromedio liquidacion operario: ", cantidad_ope, 
        "\nhoras trabajada de un operarios: ", horas_ope)


    else:
        print("numero incorrecto, intente de nuevo ")