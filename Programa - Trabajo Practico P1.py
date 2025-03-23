import pwinput

claveUsuario = "12345"
nombreUsuario = "admin"
cont = 0

user = input("Ingresar usuario: ")
password = pwinput.pwinput(prompt= "Ingresar contraseña: ")

while (cont<=1 and (password != claveUsuario or user != nombreUsuario)): 
    print("")
    print("Usuario y/o Contrasena incorrecta...")
    print("")
    cont = cont+1
    user = input("Ingresar usuario: ")
    password = pwinput.pwinput(prompt="Ingresar contraseña: ")

if (password == "12345" and user == "admin"):
    orden = 1
    while orden != "0": 
        print("")
        print("1. Gestión de locales")
        print("2. Crear cuentas de dueños de locales")
        print("3. Aprobar / Denegar solicitud de descuento")
        print("4. Gestión de Novedades")
        print("5. Reporte de utilización de descuentos")
        print("0. Salir")
        print("")

        orden = str(input("Digite el menu deseado: "))
        while orden not in ["0", "1", "2", "3", "4", "5"]:
            orden = str(input("Digite el menu deseado: "))


        if(orden=="1"):
            orden2 = 0 
            while orden2 != "d":
                print("")
                print("1. Gestión de locales")
                print("     a. Crear locales")
                print("     b. Modificar local")
                print("     c. Eliminar local")
                print("     d. Volver al menu principal")
                print("")

                orden2 = str(input("Digite el menu deseado: "))
                while orden2 not in ["a", "b", "c", "d"]:
                    orden2 = str(input("Digite el menu deseado: "))
                    
                if(orden2=="a"):
                    
                    print("")
                    
                    indu = 0
                    perfumeria = 0
                    comida = 0
                    orden4 = 2    
                    while orden4 != "0":
                        
                        rubro = "0"

                        print("")
                        print("Creador de Locales")
                        print("")
                        nombreLocal = str(input("Ingresar nombre de local a crear: "))
                        ubicacionLocal = str(input("Ingresar ubicación del local: "))

                        rubro = str(input("Ingresar el rubro del local (Perfumeria, Indumentaria, Comida): "))
                        rubro = rubro.upper()
                        while rubro not in ["PERFUMERIA", "INDUMENTARIA", "COMIDA"]:
                            rubro = str(input("Ingresar un rubro del local válido (Perfumeria, Indumentaria, Comida): "))
                            rubro = rubro.upper()

                        if (rubro == "PERFUMERIA"):
                            perfumeria = perfumeria+1
                        elif (rubro == "COMIDA"):
                            comida = comida+1
                        elif (rubro == "INDUMENTARIA"):
                            indu = indu+1
                        

                        print("")
                        print("1. Crear nuevo local")
                        print("0. Salir del creador")
                        print("")
                        orden4 = str(input("Digite el menu deseado: "))
                        while orden4 not in ["0", "1"]:
                            orden4 = str(input("Digite un menu valido: "))

                    print("")
                    if (indu>perfumeria)and(perfumeria>comida):
                        print("Indumentaria:", indu, "local/es")     
                        print("Comida:", comida, "local/es")
                    elif (indu>perfumeria)and(comida>perfumeria)and(indu>comida):
                        print("Indumentaria:", indu, "local/es")
                        print("Perfumeria:", perfumeria, "local/es")
                    elif (indu>perfumeria)and(perfumeria==comida):
                        print("Indumentaria:", indu, "local/es")
                        print("Comida y Perfumeria:", comida, "local/es")
                    elif (perfumeria>indu)and(comida<indu):
                        print("Perfumeria:", perfumeria, "local/es")
                        print("Comida:", comida, "local/es")
                    elif (perfumeria>indu)and(comida>indu)and(perfumeria>comida):
                        print("Perfumeria:", perfumeria, "local/es")
                        print("Indumentaria:", indu, "local/es")
                    elif (comida<perfumeria)and(comida==indu):
                        print("Perfumeria:", perfumeria, "local/es")
                        print("Indumentaria y Comida:", comida, "local/es")
                    elif (comida>perfumeria)and(perfumeria<indu)and(comida>indu):
                        print("Comida:", comida, "local/es")
                        print("Perfumeria:", perfumeria, "local/es")
                    elif (comida>perfumeria)and(perfumeria>indu):
                        print("Comida:", comida, "local/es")
                        print("Indumentaria:", indu, "local/es")
                    elif (comida>perfumeria)and(perfumeria==indu):
                        print("Comida:", comida, "local/es")
                        print("Indumentaria y Perfumeria:", indu, "local/es")

                    print("")
                    input("Presione enter para continuar: ")
                    
                elif(orden2=="b"):
                    print("")
                    print("...En construccion...")
                    input("")
                    
                elif(orden2=="c"):
                    print("")
                    print("...En construccion...")
                    input("")

        elif(orden=="2"):
            print("")
            print("...En construccion...")
            input("")
        elif(orden=="3"):
            print("")
            print("...En construccion...")
            input("")

        elif(orden=="4"):
            orden3 = 0 
            while orden3 != "e":
                print("")
                print("4. Gestión de locales")
                print("     a. Crear novedades")
                print("     b. Modificar novedad")
                print("     c. Eliminar novedad")
                print("     d. Ver Reporte de novedad")
                print("     e. Volver al menu principal")
                print("")

                orden3 = str(input("Digite el menu deseado: "))
                while orden3 not in ["a", "b", "c", "d", "e"]:
                    orden3 = str(input("Digite el menu deseado: "))
                    
                if(orden3=="a"):
                    print("")
                    print("...En construccion...")
                    input("")
                    
                elif(orden3=="b"):
                    print("")
                    print("...En construccion...")
                    input("")
                    
                elif(orden3=="c"):
                    print("")
                    print("...En construccion...")
                    input("")
                elif(orden3=="d"):
                    print("")
                    print("...En construccion...")
                    input("")
            
        elif(orden=="5"):
            print("")
            print("...En construccion...")
            input("")

        else:
            input("Saliendo...")


else:
    print("")
    print("Superaste 3 intentos, presione enter para salir")
    input("")