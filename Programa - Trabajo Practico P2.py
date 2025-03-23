# GRUPO 15
# Santiago Dedich - Bruno Galvani - Ivan Sanchez - Lautaro Ariel Caceres (K102)

import pwinput
import os 

def  construc():
	clear()
	print("...En construccion...")
	print("")
	input("Presione enter para volver: ")
	clear()

def clear():
	if os.name == "posix":
		os.system ("clear")
	elif os.name == "ce" or os.name == "nt" or os.name == "dos":
		os.system ("cls")

# MAPA:map                  map: array de [1..51,0..1] de str
MAPA=[0]*51
for i in range(1,51):
	MAPA[i]=[0]*2

# RUBROS:rub                  rub: array de [0..2] de str
RUBROS=[0]*3
TIPORUB=[""]*3
TIPORUB[0]="PERFUMERIA"
TIPORUB[1]="COMIDA"
TIPORUB[2]="INDUMENTARIA"

# LOCALES:loc                  loc: array de [1..50,0..4] de str
LOCALES=[""]*50
for i in range(1, 50):
	LOCALES[i]=[""]*5
k=0 #Para la carga de locales

 # USUARIOS:usu                  usu: array de [1..100,0..2] de str
USUARIOS=[""]*100
for i in range(1, 100):
	USUARIOS[i]=[""]*3

USUARIOS[1][0]="admin@shopping.com"
USUARIOS[1][1]="12345"
USUARIOS[1][2]="administrador"

USUARIOS[4][0]="localA@shopping.com"
USUARIOS[4][1]="AAAA1111"
USUARIOS[4][2]="dueñoLocal"

USUARIOS[6][0]="localB@shopping.com"
USUARIOS[6][1]="BBBB2222"
USUARIOS[6][2]="dueñoLocal"

USUARIOS[9][0]="unCliente@shopping.com"
USUARIOS[9][1]="33xx33"
USUARIOS[9][2]="cliente"

cont = 0
valid = 0

user = input("Ingresar usuario: ")
password = pwinput.pwinput(prompt= "Ingresar contraseña: ")

while (cont<2):
	
	i=1 
	while i<10 and (password != USUARIOS[i][1] or user != USUARIOS[i][0] or password == "" or user == ""): 
		i=i+1
	cont = cont+1
	if (i<10):
		cont = 3
		valid = 1
	else:
		print("")
		print("Usuario y/o Contrasena incorrecta...")
		print("")
		user = input("Ingresar usuario: ")
		password = pwinput.pwinput(prompt="Ingresar contraseña: ")	
		i=1
		while i<10 and (password != USUARIOS[i][1] or user != USUARIOS[i][0] or password == "" or user == ""): 
			i=i+1
		if (i<10):
			cont = 3
			valid = 1
	

if (valid==1):
	
	if USUARIOS[i][2]=="cliente":
		ordenc = "1"
		while ordenc != "0":    
			clear()
			print("Menu Principal")
			print("")
			print("1. Registrarme")
			print("2. Buscar descuentos en locales")
			print("3. Solicitar descuentos")
			print("4. Ver novedades")
			print("0. Salir")
			print("")

			ordenc = str(input("Digite el menu deseado: "))
			while ordenc !="0" and ordenc !="2" and ordenc !="3" and ordenc !="1" and ordenc !="4":
				ordenc = str(input("Digite el menu deseado: "))

			if(ordenc=="1"):
				construc()

			elif(ordenc=="2"):
				construc()

			elif(ordenc=="3"):
				construc()

			elif(ordenc=="4"):
				construc()


			elif(ordenc=="0"):
				clear()
			

	elif USUARIOS[i][2]=="dueñoLocal":
		ordenc = "1"
		while ordenc != "0":    
			clear()
			print("Menu Principal")
			print("")
			print("1. Gestión de descuentos")
			print("     a) Crear descuento para mi local")
			print("     b) Modificar descuento de mi local")
			print("     c) Eliminar descuento de mi local")
			print("     d) Volver")
			print("2. Aceptar / Rechazar pedido de descuento")
			print("3. Reporte de uso de descuentos")
			print("0. Salir")
			print("")

			ordenc = str(input("Digite el menu deseado: "))
			while ordenc !="0" and ordenc !="2" and ordenc !="3" and ordenc !="1":
				ordenc = str(input("Digite el menu deseado: "))

			if(ordenc=="1"):
				construc()

			elif(ordenc=="2"):
				construc()

			elif(ordenc=="3"):
				construc()

			elif(ordenc=="0"):
				clear()
			


	elif USUARIOS[i][2]=="administrador":
		clear()
		orden = "1"
		while orden != "0": 
			print("Menu Principal")
			print("")
			print("1. Gestión de locales")
			print("2. Crear cuentas de dueños de locales")
			print("3. Aprobar / Denegar solicitud de descuento")
			print("4. Gestión de Novedades")
			print("5. Reporte de utilización de descuentos")
			print("0. Salir")
			print("")

			orden = str(input("Digite el menu deseado: "))
			while orden !="0" and orden !="1" and orden !="2" and orden !="3" and orden !="4" and orden !="5":
				orden = str(input("Digite el menu deseado: "))


			if(orden=="1"):
				clear()
				orden2 = 0 
				while orden2 != "e":
					clear()
					print("1. Gestión de locales")
					print("")
					print("     a. Crear locales")
					print("     b. Modificar local")
					print("     c. Eliminar local")
					print("     d. Mapa de locales")
					print("     e. Volver al menu principal")
					print("")

					orden2 = str(input("Digite el menu deseado: "))
					while orden2 != "a" and orden2 != "b" and orden2 != "c" and orden2 != "d" and orden2 != "e":
						orden2 = str(input("Digite el menu deseado: "))
						
					if(orden2=="a"):
						orden4 = 2    
						while orden4 != "0":
							
							clear()
							k=k+1
							
							print("Creador de Locales")
							print("")
							nombre = str(input("Ingresar nombre de local a crear: "))
							valid2="0"
							while valid2!="1":
								j=1
								while (j<50 and (LOCALES[j][0]!=nombre)):
									j=j+1
								if j<50:
									print("")
									nombre = str(input("Nombre en uso, ingresar uno nuevo: "))  
									valid2="0"
								else:
									LOCALES[k][0] = nombre
									valid2="1"


							print("")
							LOCALES[k][1] = str(input("Ingresar ubicación del local: "))
							print("")

							rubro = str(input("Ingresar el rubro del local (Perfumeria, Indumentaria, Comida): "))
							rubro = rubro.upper() 
							while rubro != "PERFUMERIA" and rubro != "INDUMENTARIA" and rubro != "COMIDA":
								rubro = str(input("Ingresar un rubro del local válido (Perfumeria, Indumentaria, Comida): "))
								rubro = rubro.upper()
							LOCALES[k][2] = rubro

							print("")                           
							codigo = int(input("Ingresar código del dueño (Nro. entre 1 y 100): "))
							while USUARIOS[codigo][2] != "dueñoLocal":
								codigo = int(input("Ingresar un código de dueño válido (Nro. entre 1 y 100): "))

							LOCALES[k][3] = codigo
							LOCALES[k][4] = "A"
							
							MAPA[k][0]=k
							MAPA[k][1]=len(nombre)

							p=0
							while p<3 and rubro!=TIPORUB[p]:
								p=p+1
							if rubro==TIPORUB[p]:
								RUBROS[p]=RUBROS[p]+1
							
							for n in range(0, 2):
								for m in range (n+1,3):
									if RUBROS[n]<=RUBROS[m]:
										aux = RUBROS[n]
										RUBROS[n] = RUBROS[m]
										RUBROS[m] = aux
										aux2 = TIPORUB[n]
										TIPORUB[n] = TIPORUB[m]
										TIPORUB[m] = aux2
							print("")
							
							for o in range(0,3):
								print(TIPORUB[o],":", RUBROS[o], "locales")


							print("")
							print("1. Crear nuevo local")
							print("0. Salir del creador")
							print("")
							
							orden4 = str(input("Digite el menu deseado: "))
							while orden4 != "0" and orden4 != "1":
								orden4 = str(input("Digite un menu valido: "))

						
					elif(orden2=="b"):
						orden5=0
						clear()
						print("Modificador de Locales")
						print("")
						while(orden5!=1):
							j=1
							while (j<50 and (LOCALES[j][0]=="" or LOCALES[j][4]=="B")):
								j=j+1
							if j<50:
								codigo = int(input("Ingresar código de local (Nro. entre 1 y 50): "))
								while (codigo<1 or codigo>10) or LOCALES[codigo][0]=="" or LOCALES[codigo][4]=="B":
									print("") 
									codigo = int(input("Ingresar código de local válido (Nro. entre 1 y 50): "))
								print("")
								nombre = str(input("Ingresar nuevo nombre del local: "))

								valid2="0"
								while valid2!="1":
									j=1
									while (j<50 and (LOCALES[j][0]!=nombre)):
										j=j+1
									if j<50:
										print("")
										nombre = str(input("Nombre en uso, ingresar uno nuevo: "))  
										valid2="0"
									else:
										LOCALES[codigo][0] = nombre
										valid2="1"


								print("")
								LOCALES[codigo][1] = str(input("Ingresar ubicación del local: "))
								print("")

								prerubro = LOCALES[codigo][2]

								rubro = str(input("Ingresar el rubro del local (Perfumeria, Indumentaria, Comida): "))
								rubro = rubro.upper() 
								while rubro != "PERFUMERIA" and rubro != "INDUMENTARIA" and rubro != "COMIDA":
									rubro = str(input("Ingresar un rubro del local válido (Perfumeria, Indumentaria, Comida): "))
									rubro = rubro.upper()
								LOCALES[codigo][2] = rubro

								print("")                           
								cod = int(input("Ingresar código del dueño (Nro. entre 1 y 100): "))
								while USUARIOS[cod][2] != "dueñoLocal":
									cod = int(input("Ingresar un código de dueño válido (Nro. entre 1 y 100): "))

								LOCALES[codigo][3] = cod
								LOCALES[codigo][4] = "A"


								p=0
								while p<3 and rubro!=TIPORUB[p]:
									p=p+1
								if rubro==TIPORUB[p]:
									RUBROS[p]=RUBROS[p]+1

								p=0
								while p<3 and prerubro!=TIPORUB[p]:
									p=p+1
								if prerubro==TIPORUB[p]:
									RUBROS[p]=RUBROS[p]-1
									
								for n in range(0, 2):
									for m in range (n+1,3):
										if RUBROS[n]<=RUBROS[m]:
											aux = RUBROS[n]
											RUBROS[n] = RUBROS[m]
											RUBROS[m] = aux
											aux2 = TIPORUB[n]
											TIPORUB[n] = TIPORUB[m]
											TIPORUB[m] = aux2
								confirm = input("Desea modificar otro local? (S/N): ")
								confirm=confirm.upper()
								while(confirm!="S" and confirm!="N"):
									confirm = input("Infrese una opcion valida, (S/N): ")
								if confirm=="S":
									orden5=0
								elif confirm=="N":
									orden5=1


							else:
								clear()
								input("No hay locales creados, presione enter: ")	
								orden5=1



					elif(orden2=="c"):
						orden5=0
						while(orden5!=1):
							clear()
							print("Eliminador de locales")
							print("")
							j=1
							while (j<50 and (LOCALES[j][0]=="" or LOCALES[j][4]=="B")):
								j=j+1
							if j<50:
									codigo = int(input("Ingresar código de local (Nro. entre 1 y 50): "))
									while (codigo<1 or codigo>50) or LOCALES[codigo][0]=="" or LOCALES[codigo][4]=="B":
										print("") 
										codigo = int(input("Ingresar código de local válido (Nro. entre 1 y 50): "))

									print("")
									confirm = input("Desea definitivamente eliminar este local? (S/N): ")
									confirm=confirm.upper()
									while(confirm!="S" and confirm!="N"):
										print("")
										confirm = input("Infrese una opcion valida, (S/N): ")
									if confirm=="S":
										LOCALES[codigo][4]="B"
									else:
										valid3=1

									print("")
									salir = input("Desea eliminar otro local? (S/N): ")
									salir = salir.upper()
									while(salir!="S" and salir!="N"):
										print("")
										salir = input("Infrese una opcion valida, (S/N): ")
									if salir=="S":
										orden5=0
									elif salir=="N":
										orden5=1

							else:
								clear()
								input("No hay locales creados, presione enter: ")
								orden5=1	

						
						clear()

					elif(orden2=="d"):
						for i in range(1, 49):
							for j in range(i+1,50):
								if (MAPA[i][1]<=MAPA[j][1]):
									aux3 = MAPA[i][0]
									MAPA[i][0] = MAPA[j][0]
									MAPA[j][0] = aux3
									aux4 = MAPA[i][1]
									MAPA[i][1] = MAPA[j][1]
									MAPA[j][1] = aux4


						clear()
						print("Mapa de locales")
						print("")
						
						print("+-+-+-+-+-+-+-+-+-+-+")
						print("|",MAPA[1][0],"|",MAPA[2][0],"|",MAPA[3][0],"|",MAPA[4][0],"|",MAPA[5][0],"|")
						print("+-+-+-+-+-+-+-+-+-+-+")
						print("|",MAPA[6][0],"|",MAPA[7][0],"|",MAPA[8][0],"|",MAPA[9][0],"|",MAPA[10][0],"|")
						print("+-+-+-+-+-+-+-+-+-+-+")
						print("|",MAPA[11][0],"|",MAPA[12][0],"|",MAPA[13][0],"|",MAPA[14][0],"|",MAPA[15][0],"|")
						print("+-+-+-+-+-+-+-+-+-+-+")
						print("|",MAPA[16][0],"|",MAPA[17][0],"|",MAPA[18][0],"|",MAPA[19][0],"|",MAPA[20][0],"|")
						print("+-+-+-+-+-+-+-+-+-+-+")
						print("|",MAPA[21][0],"|",MAPA[22][0],"|",MAPA[23][0],"|",MAPA[24][0],"|",MAPA[25][0],"|")
						print("+-+-+-+-+-+-+-+-+-+-+")
						print("|",MAPA[26][0],"|",MAPA[27][0],"|",MAPA[28][0],"|",MAPA[29][0],"|",MAPA[30][0],"|")
						print("+-+-+-+-+-+-+-+-+-+-+")
						print("|",MAPA[31][0],"|",MAPA[32][0],"|",MAPA[33][0],"|",MAPA[34][0],"|",MAPA[35][0],"|")
						print("+-+-+-+-+-+-+-+-+-+-+")
						print("|",MAPA[36][0],"|",MAPA[37][0],"|",MAPA[38][0],"|",MAPA[39][0],"|",MAPA[40][0],"|")
						print("+-+-+-+-+-+-+-+-+-+-+")
						print("|",MAPA[41][0],"|",MAPA[42][0],"|",MAPA[43][0],"|",MAPA[44][0],"|",MAPA[45][0],"|")
						print("+-+-+-+-+-+-+-+-+-+-+")
						print("|",MAPA[46][0],"|",MAPA[47][0],"|",MAPA[48][0],"|",MAPA[49][0],"|",MAPA[50][0],"|")
						print("+-+-+-+-+-+-+-+-+-+-+")
						print("")

						input("Presione enter para volver: ")
						clear()    

					elif(orden2=="e"):
						clear()


			elif(orden=="2"):
				construc()

			elif(orden=="3"):
				construc()

			elif(orden=="4"):
				clear()
				orden3 = 0 
				while orden3 != "e":
					print("4. Gestión de locales")
					print("     a. Crear novedades")
					print("     b. Modificar novedad")
					print("     c. Eliminar novedad")
					print("     d. Ver Reporte de novedad")
					print("     e. Volver al menu principal")
					print("")

					orden3 = str(input("Digite el menu deseado: "))
					while orden3 !="a" and orden3 !="b" and orden3 !="c" and orden3 !="d" and orden3 !="e":
						orden3 = str(input("Digite el menu deseado: "))
						
					if(orden3=="a"):
						construc()
					elif(orden3=="b"):
						construc()
						
					elif(orden3=="c"):
						construc()

					elif(orden3=="d"):
						construc()

					elif(orden3=="e"):
						clear()
				
			elif(orden=="5"):
				construc()
			
			else:
				clear()
				input("Saliendo...")





else:
	print("")
	print("Superaste 3 intentos, presione enter para salir")
	input("")

