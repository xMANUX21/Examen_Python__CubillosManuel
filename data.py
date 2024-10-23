from datetime import datetime
import datetime


def registro(usuarios):
    try:
        NoIdentificacion=int(input("Ingrese su numero de identificacion por favor: "))
        for i in usuarios:
            if i["identificacion"]==NoIdentificacion:
                print("Numero de identificacion repetido")
                break
            else:
                print("Numero de identificacion aceptable.")
    
        nombre=input("Ingrese su nombre: ")
        cargo=input("Ingrese su cargo: ")
        salario=int(input("Ingrese su salario: "))
        if salario<=0:
            print("Ingrese un valor mayor a 0")
            return
        usuarios.append({"identificacion":NoIdentificacion,
                         "nombre":nombre,
                         "cargo":cargo,
                         "salario":salario,"inasistencias":[]})
    except ValueError:
        print("Tipo de dato no valido.")
    
    print(f"Usuario creado con nombre {nombre}")  
    print(f"numero de identificacion {NoIdentificacion}")

def inasistencias(usuarios):
    try:
        Noidentificacion=input("Ingrese su numero de identificacion: ")
        encontrado=False
        for datos in usuarios: #puede que sea Noidentificacion in usuarios 
            if datos["identificacion"]==Noidentificacion:
                encontrado=True
                inasistencias=int(input("Ingrese las inasistencias de un colaborador para regristarlas: "))
                ColaboradorIdentificacion=int(input("Ingrese el numero de identificacion del colaboral al que quiere perjudicar: "))
                fecha_y_hora_actuales = datetime.now()
                fecha_y_hora = fecha_y_hora_actuales.strftime("%d/%m/%Y Hora: %H:%M")
                for colaborador in usuarios:
                    if colaborador['identificacion']==ColaboradorIdentificacion:
                        colaborador['identificacion'].append({"inasistencias":inasistencias,"fecha":fecha_y_hora})
                        break
            else:
                print("Numero de identificacion no coincide")
        if not encontrado:
            print("Usuario no encontrado")
    except ValueError:
        print("Tipo de dato no valido")

def bonos(usuarios,bonos):
    Noidentificacion=input("Ingrese el numero de identificacion del usuario: ")
    encontrado=False
    for datos in usuarios: #puede que sea Noidentificacion in usuarios
        if datos["identificacion"]==Noidentificacion:
            encontrado=True
            fecha_y_hora_actuales = datetime.now()
            fecha_y_hora = fecha_y_hora_actuales.strftime("%d/%m/%Y Hora: %H:%M")
            valor=int(input("Ingrese el valor del bono: "))
            concepto=input("Ingrese el motivo del bono (salud , pension): ").lower().strip()
            if concepto=="salud":
                bonos.append({"valor":valor,"concepto":concepto,"fecha":fecha_y_hora})
            elif concepto=="pension":
                bonos.append({"valor":valor,"concepto":concepto,"fecha":fecha_y_hora})
            else:
                print("Concepto no valido.")
        else:
            print("Numero de identificacion no coincide")

    if not encontrado:
        print("Usuario no encontrado")

def nomina(usuarios,bonos,totales):
    print("Calcular nomina")
    while True:
            print("1.Descuentos de bonos")
            print("2.Salarios minimos")
            print("3.Descuentos por novedades")
            print("0.Salir")
            opc=int(input("Ingrese la opcion que desee: "))
            if opc==1:
                Noidentificacion=input("Ingrese el numero de identificacion del usuario para saber su nomina: ")
                encontrado=False
                for datos in usuarios: #puede que sea Noidentificacion in usuarios
                    if datos["identificacion"]==Noidentificacion:
                        encontrado=True
                        existe=False
                        for datos in bonos:
                            if datos['concepto']=="salud":
                                salud=len(datos["concepto"])
                                existe=True
                                descuentoSalud=(salud*4)/100
                                for empleado in usuarios:
                                    if empleado["salario"]>=descuentoSalud:
                                        empleado["salario"]-=descuentoSalud
                                        totales.append({"cantidad":empleado['salario']})
                                        break
                            else:
                                print("Bono de salud no existe.")
                                break
                    
                            if datos['concepto']=="pension":
                                pension=len(datos["concepto"])
                                existe=True
                                descuentoPension=(pension*4)/100
                                for empleado in usuarios:
                                    if empleado["salario"]>=descuentoSalud:
                                        empleado["salario"]-=descuentoPension
                                        total.append({"cantidad":empleado['salario']})
                                        break
                            else:
                                print("Bono de pension no existe.")
                        print(f"Su salario es de {empleado['salario']}")
                        if not existe:
                            print("Bonos no encontrados")
                if not encontrado:
                    print("Usuario no encontrado")
            elif opc==2:
                Noidentificacion=input("Ingrese el numero de identificacion del usuario para saber su nomina: ")
                encontrado=False
                for datos in usuarios: #puede que sea Noidentificacion in usuarios
                    if datos["identificacion"]==Noidentificacion:
                        encontrado=True
                        existe=False
                        if datos['salario']<2000000:
                            auxilioTransporte=(empleado['salario']*10)/100
                            total=empleado['salario']+auxilioTransporte
                            totales.append({"cantidad":total})
                            print(f"Su salario es de {total}")
                        else:
                            print("No cuenta con auxilio de transporte ")
                    else:
                        print("Numero de identificacion no coincide")
                if not encontrado:
                    print("Usuario no encontrado.")

            elif opc==3:
                Noidentificacion=input("Ingrese el numero de identificacion del usuario para saber su nomina: ")
                encontrado=False
                for datos in usuarios: #puede que sea Noidentificacion in usuarios
                    if datos["identificacion"]==Noidentificacion:
                        encontrado=True
                        for empleado in datos:
                            if len(empleado['inasistencias'])==0:
                                print("No se encuentran inasistencias")
                            else:
                                cantidad=len(empleado['inasistencias'])
                                dia=(datos['salario']/30)
                                totalDescuento=dia*cantidad
                                total=datos['salario'] - totalDescuento
                                totales.append({"cantidad":total})
                                print(f"Su salario es de {total}")
            elif opc==0:
                break

            else:
                print("Opcion no valida")

                            
            
           
            
        
        
        
        
        

