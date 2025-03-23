# GRUPO 15
# Santiago Dedich - Bruno Galvani - Ivan Sanchez - Lautaro Ariel Caceres (K102)
from colorama import Fore,Back,Style,init
from datetime import date
from datetime import datetime
import pwinput
import os 
import pickle
import os.path

init(autoreset=True)

class Usuarios:
	def __init__(self):  
		self.codUsuario = 0
		self.nombreUsuario = ""
		self.claveUsuario = ""
		self.tipoUsuario = ""  

class Promociones:
	def __init__(self):  
		self.codPromo = 0
		self.textoPromo = ""
		self.fechaDesdePromo = ""
		self.fechaHastaPromo = ""
		self.diasSemana = [0]*7
		self.estado = ""
		self.codLocal = 0  

class Locales:
	def __init__(self):  
		self.codLocal = 0
		self.nombreLocal = ""
		self.ubicacionLocal = ""
		self.rubroLocal = ""
		self.codUsuario = 0
		self.estado = ""
		
class Mapa:
	def __init__(self):
		self.mapa = 0 
		self.nombreLocal = ""
					
class UsoPromociones:
	def __init__(self):  
		self.codPromo = 0
		self.codCliente = 0
		self.fechaUsoPromo = ""

class Novedades:
	def __init__(self):  
		self.codNovedad = 0
		self.textoNovedad = ""
		self.fechaDesdeNovedad = ""
		self.fechaHastaNovedad = ""
		self.tipoUsuario = ""
		self.estado = ""
  
global AFU, ALU, AFP, ALP, AFN, ALN, ALL, AFL, RU, RL, RN, RUP, RP, ALUP, AFUP, aux, j

RM = Mapa()
RU = Usuarios()
RL = Locales()
RN = Novedades()
RUP = UsoPromociones()
RP = Promociones()
aux= Locales()
def formatearRU():
	RU.codUsuario = str(RU.codUsuario)
	RU.codUsuario = RU.codUsuario.ljust(10, ' ')
	RU.nombreUsuario = RU.nombreUsuario.ljust(100, ' ')
	RU.claveUsuario = RU.claveUsuario.ljust(8, ' ')
	RU.tipoUsuario = RU.tipoUsuario.ljust(20, ' ')

def formatearRP():
	RP.codPromo = str(RP.codPromo)
	RP.codPromo = RP.codPromo.ljust(10, ' ')
	RP.textoPromo = RP.textoPromo.ljust(200, ' ')
	RP.estado = RP.estado.ljust(10, ' ')
	RP.codLocal = str(RP.codLocal)
	RP.codLocal = RP.codLocal.ljust(10, ' ')

def formatearRL():
	RL.codLocal = str(RL.codLocal)
	RL.codLocal = RL.codLocal.ljust(10, ' ')
	RL.nombreLocal = RL.nombreLocal.ljust(50, ' ')
	RL.ubicacionLocal = RL.ubicacionLocal.ljust(50, ' ')
	RL.rubroLocal = RL.rubroLocal.ljust(50, ' ')
	RL.codUsuario = str(RL.codUsuario)
	RL.codUsuario = RL.codUsuario.ljust(10, ' ')

def formatearRUP():
	RUP.codCliente = str(RUP.codCliente)
	RUP.codCliente = RUP.codCliente.ljust(10, ' ')
	RUP.codPromo = str(RUP.codPromo)
	RUP.codPromo = RUP.codPromo.ljust(10, ' ')

def formatearRN():
	RN.codNovedad = str(RN.codNovedad)
	RN.codNovedad = RN.codNovedad.ljust(10, ' ')
	RN.textoNovedad = RN.textoNovedad.ljust(200, ' ')
	RN.tipoUsuario = RN.tipoUsuario.ljust(20, ' ')

AFU ="c:\\tp3\\usuarios.dat"
if not os.path.exists(AFU):   
	ALU = open(AFU, "w+b")  	
	ALU.seek(0,0)
	RU.codUsuario = 1   
	RU.nombreUsuario = "admin@shopping.com" 
	RU.claveUsuario = "12345"   
	RU.tipoUsuario = "administrador"    
	formatearRU()
	pickle.dump(RU,ALU)
	ALU.flush()
	

else:
	ALU = open(AFU, "r+b")

AFP = "c:\\tp3\\promociones.dat"

if not os.path.exists(AFP):   
	ALP = open(AFP, "w+b")   
else:
	ALP = open(AFP, "r+b")

AFL = "c:\\tp3\\locales.dat"

if not os.path.exists(AFL):   
	ALL = open(AFL, "w+b")   
else:
	ALL = open(AFL, "r+b")

AFUP = "c:\\tp3\\uso_promociones.dat"

if not os.path.exists(AFUP):   
	ALUP = open(AFUP, "w+b")   
else:
	ALUP = open(AFUP, "r+b")

AFN = "c:\\tp3\\novedades.dat"          
if not os.path.exists(AFN):   
	ALN = open(AFN, "w+b")   
else:
	ALN = open(AFN, "r+b")   

def ordenamiento():
	t = os.path.getsize(AFL)
	if t!=0:
		ALL.seek (0, 0)
		aux = pickle.load(ALL)
		tamReg = ALL.tell() 
		tamArch = os.path.getsize(AFL)
		cantReg = int(tamArch / tamReg)  
		for i in range(0, cantReg-1):
			for j in range (i+1, cantReg):
				ALL.seek (i*tamReg, 0)
				auxi = pickle.load(ALL)
				ALL.seek (j*tamReg, 0)
				auxj = pickle.load(ALL)
				if (auxi.nombreLocal > auxj.nombreLocal):
					ALL.seek (i*tamReg, 0)
					pickle.dump(auxj, ALL)
					ALL.seek (j*tamReg, 0)
					pickle.dump(auxi,ALL)
					ALL.flush()
	
def busqdico(L):

	t = os.path.getsize(AFL)
	if t!=0:
		ALL.seek (0,0)
		aux = pickle.load(ALL)
		tamReg = ALL.tell() 
		cantReg = t // tamReg
		desde = 0
		hasta = cantReg-1
		encontrado = False                  
		while not encontrado and desde <= hasta:
			medio = (desde + hasta) // 2 
			ALL.seek(medio*tamReg, 0)
			RL= pickle.load(ALL)
			if (RL.nombreLocal).strip() == L:
				encontrado = True
			else:
				if L < (RL.nombreLocal).strip():
					hasta = medio - 1
				else:
					desde = medio + 1
			
		if (RL.nombreLocal).strip() == L:                       
			return (medio*tamReg)                           
		else:
			return -1
	else:
		return -1   

def validar_fecha(test_str):
	try:
		return datetime.strptime(test_str, "%Y-%m-%d")
	except ValueError:
		return ("0")

def cerrar():
	ALU.close()
	ALP.close()
	ALL.close()
	ALUP.close()
	ALN.close()


def  construc():
	clear()
	print(Fore.LIGHTBLUE_EX+"...En construccion...")
	print("")
	input(Back.LIGHTBLUE_EX+"Presione enter para volver: ")
	clear()

def clear():
	print(Back.RESET+"")
	if os.name == "posix":
		os.system ("clear")
	elif os.name == "ce" or os.name == "nt" or os.name == "dos":
		os.system ("cls")

# RUBROS:rub                  rub: array de [0..2] de str
TIPORUB=[""]*3

TIPORUB[0]="PERFUMERIA"
TIPORUB[1]="COMIDA"
TIPORUB[2]="INDUMENTARIA"

RUBROS=[0]*3


orden1 = "1"
while orden1 != "3":
	print(Fore.BLACK+Back.WHITE+"                Menu de Inicio de Sesion y Creacion de cuenta                ")
	print("")
	print(Fore.LIGHTBLUE_EX+"1. Ingresar con usuario registrado")
	print(Fore.LIGHTBLUE_EX+"2. Registrarse como cliente")
	print(Fore.LIGHTBLUE_EX+"3. Salir")
	print("")
	orden1 = str(input(Fore.BLACK+Back.WHITE+"Digite el menu deseado: "))
	while orden1 !="3" and orden1 != "2" and orden1 != "1":
		orden1=str(input(Fore.RED+"Digite un menu valido: "))
	print(Back.RESET+"")

	if(orden1 == "1"):
		clear()
		cont = 0
		valid = 0

		user = input(Fore.LIGHTBLUE_EX+"                 Ingresar usuario: ")
		password = pwinput.pwinput(prompt= Fore.LIGHTBLUE_EX+"                 Ingresar contraseña: ")
		while (cont<2):
			t=os.path.getsize(AFU)
			ALU.seek(0,0)
			while (ALU.tell()+1<=t) and (password != (RU.claveUsuario).strip() or user != (RU.nombreUsuario).strip()): 
				RU = pickle.load(ALU)
	
			cont = cont+1
			
			if (password == (RU.claveUsuario).strip() and user == (RU.nombreUsuario).strip()):
				cont = 3
				valid = 1
			
			else:
				print("")
				print(Fore.RED+                "Usuario y/o Contrasena incorrecta..."                )
				print("")
				user = input(Fore.LIGHTBLUE_EX+"                Ingresar usuario: ")
				password = pwinput.pwinput(prompt=Fore.LIGHTBLUE_EX+"                Ingresar contraseña: ")
				ALU.seek(0,0)
				RU = pickle.load(ALU)
				while (ALU.tell()+1<=t) and (password != (RU.claveUsuario).strip() or user != (RU.nombreUsuario).strip()): 
					RU = pickle.load(ALU)
				
				if (password == (RU.claveUsuario).strip() and user == (RU.nombreUsuario).strip()):
					cont = 3
					valid = 1
			

		if (valid==1):
			
			if (RU.tipoUsuario).strip() == "cliente":
				codClienteActual = RU.codUsuario
				ordenc = "1"
				while ordenc != "0":    
					clear()
					print(Fore.BLACK+Back.WHITE+"                Menu Principal                ")
					print("")
					print(Fore.LIGHTBLUE_EX+"1. Buscar promociones")
					print(Fore.LIGHTBLUE_EX+"2. Solicitar descuentos")
					print(Fore.LIGHTBLUE_EX+"3. Ver novedades")
					print(Fore.LIGHTBLUE_EX+"0. Salir")
					print("")

					ordenc = str(input(Fore.BLACK+Back.WHITE+"Digite el menu deseado: "))
					while ordenc !="0" and ordenc !="2" and ordenc !="3" and ordenc !="1":
						ordenc = str(input(Fore.BLACK+Back.WHITE+"Digite el menu deseado: "))

					if(ordenc=="1"):
						clear()
						print(Fore.BLACK+Back.WHITE+"Busqueda de promociones")
						print(Back.RESET+"")
						p = os.path.getsize(AFP)
						if p!=0:
							t = os.path.getsize(AFP)
							if t!=0:
								valid="0"
								fecha = validar_fecha(str(input(Fore.LIGHTBLUE_EX+"Introduzca la fecha de promo (YYYY-MM-DD): ")))
								hoy = datetime.today()
								print("")
								valid2 = "0"
								while valid2=="0":	
									while valid=="0":
										if fecha is None:
											fecha = validar_fecha(str(input(Fore.RED+"Introduzca una fecha valida (YYYY-MM-DD): ")))
											print("")
											hoy = datetime.today()
											valid="0"
										else:
											valid="1"
									if fecha<hoy:
										fecha = validar_fecha(str(input(Fore.RED+"Introduzca una fecha valida (YYYY-MM-DD): ")))
										print("")
										hoy = datetime.today()
										valid="0"
									else:
										valid="1"
										valid2="2"

								valid="0"
								codLocal = (input(Fore.LIGHTBLUE_EX+"Ingresar código de local: "))
								while valid=="0":
									t=os.path.getsize(AFL)
									ALL.seek(0,0)
									pos = ALL.tell()
									codCheck = "0"
									while (ALL.tell()+1<=t) and (codLocal != codCheck or aux.estado=="B"): 
										pos = ALL.tell()
										aux = pickle.load(ALL)
										codCheck = (str(aux.codLocal)).strip()
									if (codLocal == codCheck and aux.estado=="A"):
										valid="1"
									else:
										print("")
										codLocal = (input(Fore.RED+"Ingresar código de local activo y existente: "))
										print(Fore.RESET+"")

								ALP.seek(0,0)
								print("")
								print(Fore.LIGHTBLUE_EX+"Promos disponibles")
								print("")
								print(Back.CYAN+"{:<20} {:<50} {:<20} {:<20}".format("Codigo Promo", "Texto Promo", "Desde", "Hasta"))
								while (ALP.tell()+1<=t): 
									RP = pickle.load(ALP)
									RP.codLocal = (str(RP.codLocal)).strip()
									if ((codLocal == RP.codLocal) and (RP.fechaDesdePromo <= fecha <= RP.fechaHastaPromo) and (RP.estado).strip()=="Aprobada") and (RP.diasSemana[fecha.weekday()]==1):
										RP.fechaDesdePromo = RP.fechaDesdePromo.strftime("%Y-%m-%d")
										RP.fechaHastaPromo = RP.fechaHastaPromo.strftime("%Y-%m-%d")
										print("{:<20} {:<50} {:<20} {:<20}".format((RP.codPromo).strip(), (RP.textoPromo).strip(), RP.fechaDesdePromo, RP.fechaHastaPromo))
								print("")
								input(Fore.BLACK+Back.WHITE+"Presione enter para continuar: ")
							
							else:
								print(Back.RESET+"")
								input(Back.WHITE+Fore.BLACK+"No hay promociones creadas, presione enter para volver: ")
						else:
							print(Back.RESET+"")
							input(Back.WHITE+Fore.BLACK+"No hay locales creados, presione enter para volver: ")

						


					elif(ordenc=="2"):
						clear()
						print(Fore.BLACK+Back.WHITE+"Solicitud de Promociones")
						print(Back.RESET+"")

						t = os.path.getsize(AFP)
						if t!=0:
							orden5=1
							while orden5==1:
								valid="0"
								codPromo = str(input(Fore.LIGHTBLUE_EX+"Ingresar código de promo: "))
								while valid=="0":
									t=os.path.getsize(AFP)
									ALP.seek(0,0)
									codCheck = "0"
									hoy = datetime.today()
									hoys = hoy.strftime("%Y-%m-%d")
									while (ALP.tell()+1<=t) and ((codPromo != codCheck) or ((aux.estado).strip()=="Denegada") or (aux.diasSemana[hoy.weekday()]==0) or (aux.fechaHastaPromo < hoys) or (aux.fechaDesdePromo >hoys)): 
										aux = pickle.load(ALP)
										codCheck = (str(aux.codPromo)).strip()  
										aux.fechaDesdePromo = aux.fechaDesdePromo.strftime("%Y-%m-%d")
										aux.fechaHastaPromo = aux.fechaHastaPromo.strftime("%Y-%m-%d")   
									if (codPromo == codCheck and (aux.estado).strip()=="Aprobada"  and (aux.diasSemana[hoy.weekday()]==1) and ((aux.fechaHastaPromo >= hoys) and (aux.fechaDesdePromo <= hoys))):
										valid="1"

									else:
										print("")
										codPromo = (input(Fore.RED+"Ingresar código de promo activo y existente: "))
										print(Fore.RESET+"")

								RUP.codCliente = codClienteActual
								RUP.fechaUsoPromo = hoy
								RUP.codPromo = codPromo
								formatearRUP()
								ALUP.seek(0,2)
								pickle.dump(RUP,ALUP)
								ALUP.flush()

								
								print("")
								salir = input(Fore.BLACK+Back.WHITE+"Desea usar otra promo? (S/N): ")
								print(Back.RESET+"")
								salir = salir.upper()
								while(salir!="S" and salir!="N"):
									salir = input(Fore.RED+"Ingrese una opcion valida, (S/N): ")
								if salir=="S":
									orden5=1
								elif salir=="N":
									orden5=0

						else:
							print(Back.RESET+"")
							input(Back.WHITE+Fore.BLACK+"No hay promociones creadas, presione enter para volver: ")	
							print(Back.RESET+"")



					elif(ordenc=="3"):
						clear()
						print(Fore.GREEN+"Proceso desarrollado en Diagrama de Chapin")
						print("")
						input(Back.WHITE+Fore.BLACK+"Presione enter para continuar: ")
						print(Back.RESET+"")

					elif(ordenc=="0"):
						clear()
					

			elif (RU.tipoUsuario).strip() =="dueñoLocal":
				codUsuarioActual = (RU.codUsuario).strip() 
				ordenc = "1"
				while ordenc != "0":   
 
					clear()
					print(Fore.BLACK+Back.WHITE+"               Menu Principal               ")
					print("")
					print(Fore.LIGHTBLUE_EX+"1. Crear promociones")
					print(Fore.LIGHTBLUE_EX+"2. Reporte de uso de promociones")
					print(Fore.LIGHTBLUE_EX+"3. Ver novedades")
					print(Fore.LIGHTBLUE_EX+"0. Salir")
					print("")

					ordenc = str(input(Fore.BLACK+Back.WHITE+"Digite el menu deseado: "))
					while ordenc !="0" and ordenc !="2" and ordenc !="3" and ordenc !="1":
						ordenc = str(input(Fore.BLACK+Back.WHITE+"Digite el menu deseado: "))

					if(ordenc=="1"):
						clear()
						print(Back.WHITE+Fore.BLACK+"Creador de promociones")
						print("")
									
						t=os.path.getsize(AFL)
						ALL.seek(0,0)
						while (ALL.tell()+1<=t) and ("A" != RL.estado or (str(RL.codUsuario)).strip() != codUsuarioActual): 
							RL = pickle.load(ALL)

						if (ALL.tell()+1<=t):
							t=os.path.getsize(AFP)
							if t!=0:
								ALP.seek(0,0)
								print (Back.CYAN+"{:<20} {:<20} {:<20} {:<20} {:<20}".format("Codigo Promo","Desde" ,"Hasta" , "Estado","Texto Promo" ))
								while (ALP.tell()+1<=t):
									ALL.seek(0,0)
									RP = pickle.load(ALP)
									codCheck1 = (str(RP.codLocal)).strip()
									RL = pickle.load(ALL)
									codCheck2 = (str(RL.codLocal)).strip()
									while (ALL.tell()+1<=t) and ((codCheck1 != codCheck2) or ((RL.codUsuario).strip() != codUsuarioActual)):
										RL = pickle.load(ALL)
										codCheck2 = (str(RL.codLocal)).strip()
					
									if (((RP.codLocal).strip() == (RL.codLocal).strip()) and ((RL.codUsuario).strip() == codUsuarioActual)):
										RP.fechaDesdePromo = RP.fechaDesdePromo.strftime("%Y-%m-%d")
										RP.fechaHastaPromo = RP.fechaHastaPromo.strftime("%Y-%m-%d")
										print("{:<20} {:<20} {:<20} {:<20} {:<200}".format((RP.codPromo).strip(), RP.fechaDesdePromo, RP.fechaHastaPromo, (RP.estado).strip(), (RP.textoPromo).strip()))

							else: 
								print(Back.WHITE+Fore.BLACK+"No hay promociones creadas")
								print(Back.RESET+"")

							t=os.path.getsize(AFP)
							if t==0:
								codPromo=1
							else:
								ALP.seek(0,0)
								RP = pickle.load(ALP)
								TamRP = ALP.tell()
								codPromo = (t//TamRP)+1

							valid="0"
							codLocal = (input(Fore.LIGHTBLUE_EX+"Ingresar código de local: "))
							while valid=="0":
								t=os.path.getsize(AFL)
								ALL.seek(0,0)
								pos = ALL.tell()
								codCheck = "0"
								while (ALL.tell()+1<=t) and (codLocal != codCheck or aux.estado=="B"): 
									pos = ALL.tell()
									aux = pickle.load(ALL)
									codCheck = (str(aux.codLocal)).strip()
								if (codLocal == codCheck and aux.estado=="A"):
									valid="1"
								else:
									print("")
									codLocal = (input(Fore.RED+"Ingresar código de local activo y existente: "))
									print(Fore.RESET+"")

							print("")
							textoPromo = str(input(Fore.LIGHTBLUE_EX+"Ingresar texto descriptivo: "))
							while(len(textoPromo)>=200):
								print("")	
								textoPromo = str(input(Fore.RED+"Ingresar texto descriptivo valido: "))
							
							print("")
							valid = "0"
							while valid != "1":
								dia = input(Fore.LIGHTBLUE_EX+"Ingresar dia de la semana en que la prom. sera efectiva: ")
								dia = dia.upper()
								
								while (dia!="LUNES" and dia!="MARTES" and dia!="MIERCOLES" and dia!="JUEVES" and dia!="VIERNES" and dia!="SABADO" and dia!="DOMINGO"):
									print("")
									dia = input(Fore.RED+"Ingresar un dia valido de la semana en que la prom. sera efectiva: ")
									dia = dia.upper()
									
								if dia=="LUNES":
									RP.diasSemana[0] = 1
								if dia=="MARTES":
									RP.diasSemana[1] = 1
								if dia=="MIERCOLES":
									RP.diasSemana[2] = 1
								if dia=="JUEVES":
									RP.diasSemana[3] = 1
								if dia=="VIERNES":
									RP.diasSemana[4] = 1
								if dia=="SABADO":
									RP.diasSemana[5] = 1
								if dia=="DOMINGO":
									RP.diasSemana[6] = 1

								print(Back.RESET+"")
								print(Fore.LIGHTBLUE_EX+"1. Ingresar otro dia")
								print(Fore.LIGHTBLUE_EX+"0. Continuar")
								print(Back.RESET+"")
								orden4 = str(input(Fore.BLACK+Back.WHITE+"Digite el menu deseado: "))
								print(Back.RESET+"")
								while orden4 != "0" and orden4 != "1":
									orden4 = str(input(Fore.RED+Back.WHITE+"Digite un menu valido: "))
									print(Back.RESET+"")
								if orden4 == "0":
									valid = "1"
								print(Back.RESET+"")

							valid = "0"

							ini = validar_fecha(str(input(Fore.LIGHTBLUE_EX+"Introduzca la fecha de inicio (YYYY-MM-DD): ")))
							print("")
							end = validar_fecha(str(input(Fore.LIGHTBLUE_EX+"Introduzca la fecha de finalización (YYYY-MM-DD): ")))							
							hoy = datetime.today()
							
							while ini>=end or end<=hoy:
								print("")
								print(Fore.RED+"Las fechas tienen que tener un formato lógico (Desde <= Hasta | Hasta >= Hoy)")
								print("")
								ini = validar_fecha(str(input(Fore.LIGHTBLUE_EX+"Introduzca la fecha de inicio (YYYY-MM-DD): ")))
								print("")
								end = validar_fecha(str(input(Fore.LIGHTBLUE_EX+"Introduzca la fecha de finalización (YYYY-MM-DD): ")))
								hoy = datetime.today()
									
							RP.estado = "Pendiente"
							RP.textoPromo = textoPromo
							RP.fechaDesdePromo = ini
							RP.fechaHastaPromo = end
							RP.codPromo = codPromo
							RP.codLocal = codLocal
							
							ALP.seek(0,2)
							formatearRP()
							pickle.dump(RP,ALP)
							ALP.flush()

							print("")
							print(Fore.GREEN+"Promocion creada correctamente")
							print("")
							input(Fore.BLACK+Back.WHITE+"Presione enter para continuar: ")
							print(Back.RESET+"")

						else:
							clear()
							print(Fore.RED+"No hay locales creados")
							print("")
							input(Fore.BLACK+Back.WHITE+"Presione enter para continuar: ")

					elif(ordenc=="2"):
						clear()
						print(Back.WHITE+Fore.BLACK+"Reporte de utilizacion de descuentos")
						print(Back.RESET+"")

						t=os.path.getsize(AFP)
						if t!=0:

							ini = validar_fecha(str(input(Fore.LIGHTBLUE_EX+"Introduzca la fecha de inicio (YYYY-MM-DD): ")))
							print("")
							end = validar_fecha(str(input(Fore.LIGHTBLUE_EX+"Introduzca la fecha de finalización (YYYY-MM-DD): ")))							
							hoy = datetime.today()
							
							while ini>=end or end<=hoy:
								print("")
								print(Fore.RED+"Las fechas tienen que tener un formato lógico (Desde <= Hasta | Hasta >= Hoy)")
								print("")
								ini = validar_fecha(str(input(Fore.LIGHTBLUE_EX+"Introduzca la fecha de inicio (YYYY-MM-DD): ")))
								print("")
								end = validar_fecha(str(input(Fore.LIGHTBLUE_EX+"Introduzca la fecha de finalización (YYYY-MM-DD): ")))
								hoy = datetime.today()

							ALP.seek(0,0)
							aux = pickle.load(ALP)
							TamRP = ALP.tell()
							CantRP = (t//TamRP)
							i=1
							v = os.path.getsize(AFL)
							ALL.seek(0,0)
							i=0
							while(ALL.tell()+1<=v):
								print("")
								i=i+1
								RL = pickle.load(ALL)
								if (RL.codUsuario).strip() == codUsuarioActual:
									RL.codLocal = (str(RL.codLocal)).strip()
									print("Local",i,":", (RL.nombreLocal).strip())
									ALP.seek(0,0)
									print("")
									print(Back.CYAN+"{:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format("Codigo Promo", "Codigo Local", "Desde", "Hasta", "Cantidad de Usos","Texto Promo" ))
									while(ALP.tell()+1<=t):
										cont=0
										RP = pickle.load(ALP)
										RP.codLocal = (str(RP.codLocal)).strip()
										if(RP.fechaDesdePromo >= ini and RP.fechaHastaPromo <= end and (RP.estado).strip()=="Aprobada" and RP.codLocal == RL.codLocal):
											ALUP.seek(0,0)
											u=os.path.getsize(AFUP)
											while (ALUP.tell()+1<=u):
												RUP = pickle.load(ALUP)
												if (RUP.codPromo==RP.codPromo and ini<=RUP.fechaUsoPromo<=end):
													cont=cont+1
											RP.fechaDesdePromo = RP.fechaDesdePromo.strftime("%Y-%m-%d")
											RP.fechaHastaPromo = RP.fechaHastaPromo.strftime("%Y-%m-%d")
											print("{:<20} {:<20} {:<20} {:<20} {:<20} {:<200}".format((RP.codPromo).strip(), (RP.codLocal).strip(), RP.fechaDesdePromo, RP.fechaHastaPromo, cont, (RP.textoPromo).strip()))			
										
							print("")
							input(Fore.BLACK+Back.WHITE+"Presione enter para volver: ")
							print(Back.RESET+"")
							clear()



					elif(ordenc=="3"):
						clear()
						print(Fore.GREEN+"Diagramado en Chapin")
						print("")
						input(Fore.BLACK+Back.WHITE+"Presione enter para continuar: ")

					elif(ordenc=="0"):
						clear()
				


			elif (RU.tipoUsuario).strip() == "administrador":
				clear()
				orden = "1"
				while orden != "0": 
					
					print(Fore.BLACK+Back.WHITE+"Menu Principal")
					print("")
					print(Fore.LIGHTBLUE_EX+"1. Gestión de locales")
					print(Fore.LIGHTBLUE_EX+"2. Crear cuentas de dueños de locales")
					print(Fore.LIGHTBLUE_EX+"3. Aprobar / Denegar solicitud de descuento")
					print(Fore.LIGHTBLUE_EX+"4. Gestión de Novedades")
					print(Fore.LIGHTBLUE_EX+"5. Reporte de utilización de descuentos")
					print(Fore.LIGHTBLUE_EX+"0. Salir")
					print("")

					orden = str(input(Fore.BLACK+Back.WHITE+"Digite el menu deseado: "))
					while orden !="0" and orden !="1" and orden !="2" and orden !="3" and orden !="4" and orden !="5":
						orden = str(input(Fore.BLACK+Back.WHITE+"Digite el menu deseado: "))


					if(orden=="1"):
						clear()

						orden2 = 0 
						while orden2 != "e":

							clear()
							ordenamiento()
							print(Back.WHITE+Fore.BLACK+"1.   Gestión de locales               ")
							print(Back.RESET+"")
							print(Fore.LIGHTBLUE_EX+"     a. Crear locales")
							print(Fore.LIGHTBLUE_EX+"     b. Modificar local")
							print(Fore.LIGHTBLUE_EX+"     c. Eliminar o reactivar local")
							print(Fore.LIGHTBLUE_EX+"     d. Mapa de locales")
							print(Fore.LIGHTBLUE_EX+"     e. Volver al menu principal")
							print("")

							orden2 = str(input(Fore.BLACK+Back.WHITE+"Digite el menu deseado: "))
							while orden2 != "a" and orden2 != "b" and orden2 != "c" and orden2 != "d" and orden2 != "e":
								orden2 = str(input(Fore.BLACK+Back.WHITE+"Digite el menu deseado: "))

							if(orden2=="a"):
								orden4 = 2    
								while orden4 != "0":
									clear()
									print(Back.WHITE+Fore.BLACK+"Creador de Locales")
									print(Back.RESET+"")
									ordenamiento()
									
									t=os.path.getsize(AFL)
									if t!=0:
										ALL.seek(0,0)
										print (Back.CYAN+"{:<20} {:<20} {:<20} {:<20} {:<20}".format("Codigo Local","Nombre Local","Ubicacion","Estado","Codigo de Dueño"))
										
										while (ALL.tell()+1<=t): 
											RL = pickle.load(ALL)
											print("")
											print ("{:<20} {:<20} {:<20} {:<20} {:<20}".format((RL.codLocal).strip(),(RL.nombreLocal).strip(),(RL.ubicacionLocal).strip(),RL.estado,(RL.codUsuario).strip()))
											print("")
									else: 
										print(Fore.RED+"No hay locales creados")
										print("")

									t=os.path.getsize(AFU)
									ALU.seek(0,0)
									while (ALU.tell()+1<=t) and ((RU.tipoUsuario).strip() != "dueñoLocal"): 
										RU = pickle.load(ALU)
									if ((RU.tipoUsuario).strip() == "dueñoLocal"):
										nombre = str(input(Fore.LIGHTBLUE_EX+"Ingresar nombre de local a crear: "))
										t=os.path.getsize(AFL)
										if t!=0:
											valid="0"
											while valid!="1":
												pos = busqdico(nombre)
												if (pos != -1):
													print("")
													nombre = str(input(Fore.LIGHTBLUE_EX+"Nombre en uso, ingresar uno nuevo: "))  
													valid="0"
												else:
													valid="1"
											print("")
										else:
											print("")


										
										ubicacionLocal = str(input(Fore.LIGHTBLUE_EX+"Ingresar ubicación del local: "))
										while len(ubicacionLocal)>=50:
											ubicacionLocal = str(input(Fore.RED+"Ingresar ubicación del local valida: "))

										print("")

										rubro = str(input(Fore.LIGHTBLUE_EX+"Ingresar el rubro del local (Perfumeria, Indumentaria, Comida): "))
										rubro = rubro.upper() 
										while rubro != "PERFUMERIA" and rubro != "INDUMENTARIA" and rubro != "COMIDA":
											rubro = str(input(Fore.LIGHTBLUE_EX+"Ingresar un rubro del local válido (Perfumeria, Indumentaria, Comida): "))
											rubro = rubro.upper()
										

										print("")                           
										
										
										codigo = input(Fore.LIGHTBLUE_EX+"Ingresar código del dueño: ") 
										valid = 0
										t = os.path.getsize(AFU)
										while valid==0: 
											ALU.seek(0,0)   
											while (ALU.tell()+1<=t):
												RU = pickle.load(ALU)
												if (codigo == (RU.codUsuario).strip() and RU.tipoUsuario.strip() == "dueñoLocal"):
													valid = 1
											if valid==1:
												print("")
												input(Fore.GREEN+"Código válido.")
											else:
												print("")
												codigo = input(Fore.RED+"Ingresar código del dueño valido: ")


										t=os.path.getsize(AFL)
										if t==0:
											codLocal=1
										else:
											ALL.seek(0,0)
											RL = pickle.load(ALL)
											TamRL = ALL.tell()
											codLocal = (t//TamRL)+1

										RL.nombreLocal = nombre
										RL.codUsuario = codigo
										RL.codLocal = codLocal
										RL.estado = "A"
										RL.rubroLocal = rubro
										RL.ubicacionLocal = ubicacionLocal

										ALL.seek(0,2)
										formatearRL()
										pickle.dump(RL,ALL)
										ALL.flush()

										ALL.seek(0,0)
										for i in range(0,2):
											RUBROS[i]=0
										t=os.path.getsize(AFL)
										while (ALL.tell()+1<=t): 
											RL = pickle.load(ALL)
											i=0
											while i<=2:
												if ((RL.rubroLocal).strip() == TIPORUB[i]):
													RUBROS[i]=RUBROS[i]+1
												i=i+1
										
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
										ALL.seek(0,0)

										print("")
										print(Fore.LIGHTBLUE_EX+"1. Crear nuevo local")
										print(Fore.LIGHTBLUE_EX+"0. Salir del creador")
										print("")
										
										orden4 = str(input(Fore.BLACK+Back.WHITE+"Digite el menu deseado: "))
										while orden4 != "0" and orden4 != "1":
											orden4 = str(input(Fore.RED+"Digite un menu valido: "))

									else:
										print(Fore.LIGHTBLUE_EX+"No hay Usuarios dueños de locales para crear uno")
										print("")
										input(Back.LIGHTBLUE_EX+"Presione enter para volver: ")
										orden4 = "0" 

								
							elif(orden2=="b"):
								orden5=0
								clear()
								print(Back.WHITE+Fore.BLACK+"Modificador de Locales")
								print(Back.RESET+"")
								
								while(orden5!=1):
									
									t=os.path.getsize(AFL)
									ALL.seek(0,0)
									while (ALL.tell()+1<=t) and ("A" != (RL.estado).strip()): 
										RL = pickle.load(ALL)

									
									if (ALL.tell()+1<=t):
										ordenamiento()
										t=os.path.getsize(AFL)
										if t!=0:
											ALL.seek(0,0)
											print (Back.CYAN+"{:<20} {:<20} {:<20} {:<20} {:<20}".format("Codigo Local","Nombre Local","Ubicacion","Estado","Codigo de Dueño"))
											
											while (ALL.tell()+1<=t): 
												RL = pickle.load(ALL)
												print("")
												print ("{:<20} {:<20} {:<20} {:<20} {:<20}".format((RL.codLocal).strip(),(RL.nombreLocal).strip(),(RL.ubicacionLocal).strip(),RL.estado,(RL.codUsuario).strip()))
												print("")
										else: 
											print(Fore.RED+"No hay locales creados")
											print("")

										codLocal = (input(Fore.LIGHTBLUE_EX+"Ingresar código de local: "))
										t=os.path.getsize(AFL)
										ALL.seek(0,0)
										pos = ALL.tell()
										codCheck = "0"
										while (ALL.tell()+1<=t) and (codLocal != codCheck or aux.estado=="B"): 
											pos = ALL.tell()
											aux = pickle.load(ALL)
											codCheck = (str(aux.codLocal)).strip()
										
										if (codLocal == codCheck and aux.estado=="A"):           
											codLocal = codCheck
											print("")                                   
											nombre = str(input(Fore.LIGHTBLUE_EX+"Ingresar nuevo nombre del local: "))
											while valid=="0":
												posi = busqdico(nombre)
												if posi!=-1:
													print("")
													nombre = str(input(Fore.LIGHTBLUE_EX+"Nombre en uso, ingresar uno nuevo: "))  
													valid="0"
												else:
													valid="1"   

											print("")
											ubicacionLocal = str(input(Fore.LIGHTBLUE_EX+"Ingresar ubicación del local: "))
											print("")

											rubro = str(input(Fore.LIGHTBLUE_EX+"Ingresar el rubro del local (Perfumeria, Indumentaria, Comida): "))
											rubro = rubro.upper() 
											while rubro != "PERFUMERIA" and rubro != "INDUMENTARIA" and rubro != "COMIDA":
												rubro = str(input(Fore.LIGHTBLUE_EX+"Ingresar un rubro del local válido (Perfumeria, Indumentaria, Comida): "))
												rubro = rubro.upper()

											print("")                           
											
											codigo = input(Fore.LIGHTBLUE_EX+"Ingresar código del dueño: ") 
											valid = 0
											t = os.path.getsize(AFU)
											ALU.seek(0,0)   
											while valid==0: 
												ALU.seek(0,0)
												while (ALU.tell()+1<=t):
													RU = pickle.load(ALU)
													if (codigo == (RU.codUsuario).strip() and RU.tipoUsuario.strip() == "dueñoLocal"):
														valid = 1
												if valid==1:
													print("")
													input(Fore.GREEN+"Código válido.")
												else:
													print("")
													codigo = input(Fore.RED+"Ingresar código del dueño valido: ")
											
											
											ALL.seek(pos,0)

											RL.codLocal = codLocal 
											RL.codUsuario = codigo
											RL.nombreLocal = nombre
											RL.ubicacionLocal = ubicacionLocal
											RL.rubroLocal = rubro

											formatearRL()

											pickle.dump(RL,ALL)

											ALL.flush()

											ALL.seek(0,0)
											for i in range(0,3):
												RUBROS[i]=0
											t=os.path.getsize(AFL)
											while (ALL.tell()+1<=t): 
												RL = pickle.load(ALL)
												i=0
												while i<=2:
													if ((RL.rubroLocal).strip() == TIPORUB[i]):
														RUBROS[i]=RUBROS[i]+1
													i=i+1
											
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
												print(Fore.LIGHTBLUE_EX+TIPORUB[o],":", RUBROS[o], "locales")

										else:
											print("")
											input(Fore.RED+"No hay locales disponibles, presione enter para continuar: ")
											print("")


										print("")
										confirm = input(Back.WHITE+Fore.BLACK+"Desea modificar otro local? (S/N): ")
										confirm=confirm.upper()
										while(confirm!="S" and confirm!="N"):
											print(Back.RESET+"")
											confirm = input(Fore.RED+"Ingrese una opcion valida, (S/N): ")
											confirm=confirm.upper()
										if confirm=="S":
											orden5=0
											clear()
										elif confirm=="N":
											orden5=1


									else:
										input(Back.WHITE+Fore.BLACK+"No hay locales creados, presione enter: ")   
										print(Back.RESET+"")
										orden5=1



							elif(orden2=="c"):
								orden5=0
								while(orden5!=1):
									clear()
									print(Back.WHITE+Fore.BLACK+"Eliminador de locales")
									print(Back.RESET+"")
									
									ordenamiento()
									t=os.path.getsize(AFL)
									if (t!=0):
										t=os.path.getsize(AFL)
										if t!=0:
											ALL.seek(0,0)
											print (Back.CYAN+"{:<20} {:<20} {:<20} {:<20} {:<20}".format("Codigo Local","Nombre Local","Ubicacion","Estado","Codigo de Dueño"))
											
											while (ALL.tell()+1<=t): 
												RL = pickle.load(ALL)
												print("")
												print ("{:<20} {:<20} {:<20} {:<20} {:<20}".format((RL.codLocal).strip(),(RL.nombreLocal).strip(),(RL.ubicacionLocal).strip(),RL.estado,(RL.codUsuario).strip()))
												print("")
										else: 
											print(Fore.RED+"No hay locales creados")
											print("")

										codigo = (input(Fore.LIGHTBLUE_EX+"Ingresar código de local: "))
										t=os.path.getsize(AFL)
										ALL.seek(0,0)
										codCheck = "0"
										while (ALL.tell()+1<=t) and (codigo != codCheck): 
											pos = ALL.tell()
											RL = pickle.load(ALL)
											codCheck = (str(RL.codLocal)).strip()

										if (codigo == codCheck):
											if RL.estado == "A":
												print("")
												confirm = input(Fore.BLACK+Back.WHITE+"Desea definitivamente eliminar este local? (S/N): ")
												confirm=confirm.upper()
												while(confirm!="S" and confirm!="N"):
													print("")
													confirm = input(Fore.RED+"Ingrese una opcion valida, (S/N): ")
												if confirm=="S":
													print(Back.RESET+"")
													input(Fore.GREEN+"Local modificado")
													ALL.seek(pos,0)
													RL.estado ="B"
													formatearRL()
													pickle.dump(RL,ALL)
													ALL.flush()

													print("")
													salir = input(Fore.BLACK+Back.WHITE+"Desea eliminar o reactivar otro local? (S/N): ")
													salir = salir.upper()
													while(salir!="S" and salir!="N"):
														print("")
														salir = input(Fore.RED+"Ingrese una opcion valida, (S/N): ")
													if salir=="S":
														orden5=0
													elif salir=="N":
														orden5=1
												else:
													print("")
													salir = input(Fore.BLACK+Back.WHITE+"Desea eliminar o reactivar otro local? (S/N): ")
													print(Back.RESET+"")
													salir = salir.upper()
													while(salir!="S" and salir!="N"):
														print("")
														salir = input(Fore.RED+"Ingrese una opcion valida, (S/N): ")
													if salir=="S":
														orden5=0
													elif salir=="N":
														orden5=1
											elif RL.estado == "B":
												print("")
												confirm = input(Fore.BLACK+Back.WHITE+"Desea reactivar este local? (S/N): ")
												print(Back.RESET+"")
												confirm=confirm.upper()
												while(confirm!="S" and confirm!="N"):
													print("")
													confirm = input(Fore.RED+"Ingrese una opcion valida, (S/N): ")
												if confirm=="S":
													input(Fore.GREEN+"Local modificado")
													ALL.seek(pos,0)
													RL.estado ="A"
													formatearRL()
													pickle.dump(RL,ALL)
													ALL.flush()

													print("")
													salir = input(Fore.BLACK+Back.WHITE+"Desea eliminar o reactivar otro local? (S/N): ")
													print(Back.RESET+"")
													salir = salir.upper()
													while(salir!="S" and salir!="N"):
														print("")
														salir = input(Fore.RED+"Ingrese una opcion valida, (S/N): ")
													if salir=="S":
														orden5=0
													elif salir=="N":
														orden5=1
												else:
													print("")
													salir = input(Fore.BLACK+Back.WHITE+"Desea eliminar o reactivar otro local? (S/N): ")
													print(Back.RESET+"")
													salir = salir.upper()
													while(salir!="S" and salir!="N"):
														print("")
														salir = input(Fore.RED+"Ingrese una opcion valida, (S/N): ")
													if salir=="S":
														orden5=0
													elif salir=="N":
														orden5=1
										else:
											print("")
											print(Fore.RED+"Codigo de local no encontrado")
											print("")
											salir = input(Fore.BLACK+Back.WHITE+"Desea eliminar otro local? (S/N): ")
											print(Back.RESET+"")
											salir = salir.upper()
											while(salir!="S" and salir!="N"):
												print("")
												salir = input(Fore.RED+"Ingrese una opcion valida, (S/N): ")
												salir = salir.upper()
											if salir=="S":
												orden5=0
											elif salir=="N":
												orden5=1

									else:
										input(Back.WHITE+Fore.BLACK+"No hay locales creados, presione enter: ")
										print(Back.RESET+"")
										orden5=1    

								
								clear()

							elif(orden2=="d"):

								clear()
								print(Back.WHITE+Fore.BLACK+"Mapa de locales")
								print(Back.RESET+"")
								
								j=0

								def m(i):
									global j
									t=os.path.getsize(AFL)
									if t!=0:
										ALL.seek(0,0)
										RL = pickle.load(ALL)
										TamRL = ALL.tell()
										CantRL = (t)//TamRL 
										if (CantRL>=i):
											ALL.seek((i-1)*TamRL,0)
											RL = pickle.load(ALL)
											if RL.estado=="A":
												codLocal = (str(RL.codLocal)).strip()
												j=j+1
												return(codLocal)
											else:
												j=j+1
												return("B")		
										else:
											return("0")
									else:
										return("0") 
									
								print(Back.BLUE+Fore.BLACK+"+-+-+-+-+-+-+-+-+-+-+")
								print(Back.BLUE+Fore.BLACK+"{:<1} {:<1} {:<1} {:<1} {:<1} {:<1} {:<1} {:<1} {:<1} {:<1} {:<1}".format("|",m(1),"|",m(2),"|",m(3),"|",m(4),"|",m(5),"|"))
								print(Back.BLUE+Fore.BLACK+"+-+-+-+-+-+-+-+-+-+-+")
								print(Back.BLUE+Fore.BLACK+"{:<1} {:<1} {:<1} {:<1} {:<1} {:<1} {:<1} {:<1} {:<1} {:<1} {:<1}".format("|",m(6),"|",m(7),"|",m(8),"|",m(9),"|",m(10),"|"))
								print(Back.BLUE+Fore.BLACK+"+-+-+-+-+-+-+-+-+-+-+")
								print(Back.BLUE+Fore.BLACK+"{:<1} {:<1} {:<1} {:<1} {:<1} {:<1} {:<1} {:<1} {:<1} {:<1} {:<1}".format("|",m(11),"|",m(12),"|",m(13),"|",m(14),"|",m(15),"|"))
								print(Back.YELLOW+Fore.BLACK+"+-+-+-+-+-+-+-+-+-+-+")
								print(Back.YELLOW+Fore.BLACK+"{:<1} {:<1} {:<1} {:<1} {:<1} {:<1} {:<1} {:<1} {:<1} {:<1} {:<1}".format("|",m(16),"|",m(17),"|",m(18),"|",m(19),"|",m(20),"|"))
								print(Back.YELLOW+Fore.BLACK+"+-+-+-+-+-+-+-+-+-+-+")
								print(Back.YELLOW+Fore.BLACK+"{:<1} {:<1} {:<1} {:<1} {:<1} {:<1} {:<1} {:<1} {:<1} {:<1} {:<1}".format("|",m(21),"|",m(22),"|",m(23),"|",m(24),"|",m(25),"|"))
								print(Back.YELLOW+Fore.BLACK+"+-+-+-+-+-+-+-+-+-+-+")
								print(Back.YELLOW+Fore.BLACK+"{:<1} {:<1} {:<1} {:<1} {:<1} {:<1} {:<1} {:<1} {:<1} {:<1} {:<1}".format("|",m(26),"|",m(27),"|",m(28),"|",m(29),"|",m(30),"|"))
								print(Back.YELLOW+Fore.BLACK+"+-+-+-+-+-+-+-+-+-+-+")
								print(Back.YELLOW+Fore.BLACK+"{:<1} {:<1} {:<1} {:<1} {:<1} {:<1} {:<1} {:<1} {:<1} {:<1} {:<1}".format("|",m(31),"|",m(32),"|",m(33),"|",m(34),"|",m(35),"|"))
								print(Back.YELLOW+Fore.BLACK+"+-+-+-+-+-+-+-+-+-+-+")
								print(Back.BLUE+Fore.BLACK+"{:<1} {:<1} {:<1} {:<1} {:<1} {:<1} {:<1} {:<1} {:<1} {:<1} {:<1}".format("|",m(36),"|",m(37),"|",m(38),"|",m(39),"|",m(40),"|"))
								print(Back.BLUE+Fore.BLACK+"+-+-+-+-+-+-+-+-+-+-+")
								print(Back.BLUE+Fore.BLACK+"{:<1} {:<1} {:<1} {:<1} {:<1} {:<1} {:<1} {:<1} {:<1} {:<1} {:<1}".format("|",m(41),"|",m(42),"|",m(43),"|",m(44),"|",m(45),"|"))
								print(Back.BLUE+Fore.BLACK+"+-+-+-+-+-+-+-+-+-+-+")
								print(Back.BLUE+Fore.BLACK+"{:<1} {:<1} {:<1} {:<1} {:<1} {:<1} {:<1} {:<1} {:<1} {:<1} {:<1}".format("|",m(46),"|",m(47),"|",m(48),"|",m(49),"|",m(50),"|"))
								print(Back.BLUE+Fore.BLACK+"+-+-+-+-+-+-+-+-+-+-+")
								print(Back.RESET+"")

								if j>50:
									print(Fore.GREEN+"Se superan los 50 locales, próximamente se habilitará un mapa con los demás locales")
									print("")
									input(Back.WHITE+Fore.BLACK+"Presione enter para volver: ")			
									print(Back.RESET+"")						
									clear()
								else:
									input(Back.WHITE+Fore.BLACK+"Presione enter para volver: ")
									print(Back.RESET+"")
									clear()    

							elif(orden2=="e"):
								clear()


					elif(orden=="2"):
						
						clear()
						print(Back.WHITE+Fore.BLACK+"Creacion de cuentas de Dueños")
						print(Back.RESET+"")
						
						t = os.path.getsize(AFU)
						ALU.seek(0,0)
						RU = pickle.load(ALU)
						Tam = ALU.tell()
						n = (t//Tam)
						codUsuario = n+1
						
						nomv = "0"

						nombreUsuario = input(Fore.LIGHTBLUE_EX+"Ingresar cuenta de Mail: ")
						while nomv == "0":
							t=os.path.getsize(AFU)
							ALU.seek(0,0)
							while ((ALU.tell()+1)<=t) and (nombreUsuario != (RU.nombreUsuario).strip()): 
									RU = pickle.load(ALU)
							if (nombreUsuario == (RU.nombreUsuario).strip() or (len(nombreUsuario)>100)):
								print("")
								nombreUsuario = input(Fore.RED+"Ingresar cuenta de Mail valida: ")
							else:
								nomv = "1"      
						print("")
						claveUsuario = pwinput.pwinput(Fore.LIGHTBLUE_EX+"Ingresar contraseña (8 caracteres): ")
						while ((len(claveUsuario)!=8)):
							print("")
							claveUsuario = pwinput.pwinput(Fore.RED+"Ingresar contraseña valida: ")        

						RU.nombreUsuario = nombreUsuario

						RU.claveUsuario = claveUsuario

						RU.tipoUsuario = "dueñoLocal"

						RU.codUsuario = codUsuario
						
						print("")
						print(Fore.GREEN+"Se le asigna el codigo de Usuario N°: ", codUsuario)
						print("")
						input(Fore.BLACK+Back.WHITE+"Presione enter para continuar: ")

						ALU.seek(0,2)

						formatearRU()

						pickle.dump(RU,ALU)

						ALU.flush()

						clear()

					elif(orden=="3"):
						print(Back.RESET+"")
						clear()
						print(Back.WHITE+Fore.BLACK+"Aceptar o denegar promociones pendientes")
						print(Back.RESET+"")
						t=os.path.getsize(AFP)
						if t!=0:
							codPromo = input(Fore.BLACK+Back.WHITE+"Insertar codigo de promo a aprobar: ")
							print(Back.RESET+"")
							ALP.seek(0,0)
							RP=pickle.load(ALP)
							TamR = ALP.tell()
							ALP.seek(0,0)
							codCheck = "0"
							while (ALP.tell()+1<=t and codCheck!=codPromo): 
								RP = pickle.load(ALP)
								codCheck = (str(RP.codPromo)).strip()
								p = os.path.getsize(AFP)
								ALL.seek(0,0)
								while(ALL.tell()+1<=p and RP.codLocal != RL.codLocal):
									RL = pickle.load(ALL)		
							if ("Pendiente" == (RP.estado).strip() and codCheck==codPromo):
								print(Back.RESET+"")
								print (Back.CYAN+"{:<20} {:<20} {:<20} {:<20}".format("Codigo Promo", "Codigo Local", "Nombre Local", "Texto Promo"))
								print(Back.RESET+"")
								print("{:<20} {:<20} {:<20} {:<200}".format((RP.codPromo).strip(), (RP.codLocal).strip(), (RL.nombreLocal).strip(), (RP.textoPromo).strip()))
								print(Back.RESET+"")
								
								decis = str(input("Desea aprobar o denegar la promoción? (A/D): "))
								decis = decis.upper()
								while decis!="A" and decis!="D":
									print("")
									decis = str(input("Ingrese una opcion valida (A/D): "))
									decis = decis.upper()
								ALP.seek(-TamR,1)
								if decis=="A":
									RP.estado = "Aprobada"
									print("")
									print(Fore.GREEN+"Promocion Aprobada")
								else:
									RP.estado = "Denegada"
									print("")
									print(Fore.RED+"Promocion Denegada")
								formatearRP()
								pickle.dump(RP,ALP)
								ALP.flush()
							else:
								input(Fore.RED+"Codigo de promocion no encontrado")

							print("")
							input(Fore.BLACK+Back.WHITE+"Presione enter para volver: ")
							print(Back.RESET+"")
							clear()


						else:
							print(Fore.RED+"No hay promociones creadas/pendientes")
							print("")
							input(Fore.BLACK+Back.WHITE+"Presione enter para volver: ")
						
						clear()

					elif(orden=="4"):
						clear()
						print(Fore.GREEN+"Proceso desarrollado en Diagrama de Chapin")
						print("")
						input(Back.WHITE+Fore.BLACK+"Presione enter para continuar: ")
						print(Back.RESET+"")
						clear()
						
						
					elif(orden=="5"):
						clear()
						print(Back.WHITE+Fore.BLACK+"Reporte de utilizacion de descuentos")
						print(Back.RESET+"")

						t=os.path.getsize(AFP)
						if t!=0:
							ini = validar_fecha(str(input(Fore.LIGHTBLUE_EX+"Introduzca la fecha de inicio (YYYY-MM-DD): ")))
							print("")
							end = validar_fecha(str(input(Fore.LIGHTBLUE_EX+"Introduzca la fecha de finalización (YYYY-MM-DD): ")))							
							hoy = datetime.today()

							while ini>=end or end<=hoy:
								print("")
								print(Fore.RED+"Las fechas tienen que tener un formato lógico (Desde <= Hasta | Hasta >= Hoy)")
								print("")
								ini = validar_fecha(str(input(Fore.LIGHTBLUE_EX+"Introduzca la fecha de inicio (YYYY-MM-DD): ")))
								print("")
								end = validar_fecha(str(input(Fore.LIGHTBLUE_EX+"Introduzca la fecha de finalización (YYYY-MM-DD): ")))
								hoy = datetime.today()

							ALP.seek(0,0)
							print("")
							print(Back.CYAN+"{:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format("Codigo Promo", "Codigo Local", "Desde", "Hasta", "Cantidad de Usos","Texto Promo" ))
							while (ALP.tell()+1<=t):
								cont=0
								RP = pickle.load(ALP)
								if(RP.fechaDesdePromo >= ini and RP.fechaHastaPromo <= end and (RP.estado).strip()=="Aprobada"):
									ALUP.seek(0,0)
									u=os.path.getsize(AFUP)
									while (ALUP.tell()+1<=u):
										RUP = pickle.load(ALUP)
										if (RUP.codPromo==RP.codPromo and ini<=RUP.fechaUsoPromo<=end):
											cont=cont+1
									RP.fechaDesdePromo = RP.fechaDesdePromo.strftime("%Y-%m-%d")
									RP.fechaHastaPromo = RP.fechaHastaPromo.strftime("%Y-%m-%d")
									print("{:<20} {:<20} {:<20} {:<20} {:<20} {:<200}".format((RP.codPromo).strip(), (RP.codLocal).strip(), RP.fechaDesdePromo, RP.fechaHastaPromo, cont, (RP.textoPromo).strip()))
							
							print("")
							input(Fore.BLACK+Back.WHITE+"Presione enter para volver: ")
							print(Back.RESET+"")
							clear()
						
						else:
							input(Fore.BLACK+Back.WHITE+"No hay descuentos creados, presione enter para continuar: ")
							print(Back.RESET+"")
							clear()


					else:
						clear()
						input(Fore.BLACK+Back.WHITE+"Saliendo...")
						print(Back.RESET+"")
						clear()





		else:
			print("")
			print(Back.RED+"Superaste 3 intentos, presione enter para salir")
			print(Back.RESET+"")
			input("")
			clear()

	elif(orden1 == "2"):
		clear()
		print(Fore.BLACK+Back.WHITE+"Creacion de cuentas")
		print(Back.RESET+"")
		
		t = os.path.getsize(AFU)
		ALU.seek(0,0)
		RU = pickle.load(ALU)
		Tam = ALU.tell()
		n = (t//Tam)
		codUsuario = n+1

		nomv = "0"

		nombreUsuario = input(Fore.LIGHTBLUE_EX+"Ingresar nombre de usuario: ")
		while nomv == "0":
			t=os.path.getsize(AFU)
			ALU.seek(0,0)
			while ((ALU.tell()+1)<=t) and (nombreUsuario != (RU.nombreUsuario).strip()): 
					RU = pickle.load(ALU)
			if (nombreUsuario == (RU.nombreUsuario).strip() or len(nombreUsuario)>100):
				print("")
				nombreUsuario = input(Fore.RED+"Ingresar nombre de usuario no existente: ")
			else:
				nomv = "1"   

		print("")
		claveUsuario = pwinput.pwinput(prompt= Fore.LIGHTBLUE_EX+"Ingresar contraseña (8 caracteres): ")
		while ((ALU.tell()+1)<=t or (len(claveUsuario)!=8)):
			print("")
			claveUsuario = pwinput.pwinput(prompt=Fore.RED+"Ingresar contraseña valida: ")
			
		RU.nombreUsuario = nombreUsuario

		RU.claveUsuario = claveUsuario

		RU.tipoUsuario = "cliente"

		RU.codUsuario = codUsuario
		
		print("")
		print(Fore.GREEN+"Se le asigna el codigo de Usuario N°: ", codUsuario)
		print("")
		input(Back.WHITE+Fore.BLACK+"Presione enter para continuar: ")
		print(Back.RESET+"")

		ALU.seek(0,2)

		formatearRU()

		pickle.dump(RU,ALU)

		ALU.flush()

		clear()




	elif(orden1 == "3"):
		clear()
		cerrar()
		input(Fore.BLACK+Back.WHITE+"Saliendo... ")
		print(Back.RESET+"")