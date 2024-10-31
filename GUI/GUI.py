import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# BASE_PATH = os.path.dirname(os.path.abspath(__file__))
# JSON_PATH = os.path.join(BASE_PATH, "controller")
# sys.path.append(JSON_PATH)
import pygame
from controller import user_repository
from pygame import *
# from controller.user_repository import load_users

pygame.init()

ancho = 1000
altura = 800  
screen = pygame.display.set_mode((ancho, altura))

DarkBlue = (46, 134, 193)
LightGreen = (88, 214, 141)
White = (255, 255, 255)
Black = (0, 0, 0)

calibri = pygame.font.SysFont("Calibri", 40)
Fuente = pygame.font.SysFont('Arial', 30)
FuenteP = pygame.font.SysFont('Arial', 15)

Button1 = pygame.Rect(220, 600, 200, 100)

logged_in = False
input_active_user = False
input_active_password = False
username_input = ''
password_input = ''
mostrar_error_login = False

valid_username = "usuario"
valid_password = "contraseña"

input_box_user = pygame.Rect(400, 300, 140, 40)
input_box_password = pygame.Rect(400, 400, 140, 40)

color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color_user = color_inactive
color_password = color_inactive

input_active_peso = False
input_active_altura = False
input_active_rutinas = False
peso_input = ''
altura_input = ''
rutinas_input = ''
mostrar_resultado = False
resultado = ""
etapa = ""
dieta = []
rutinas = []

verdadero = True

input_box_peso = pygame.Rect(200, 200, 140, 40)
input_box_altura = pygame.Rect(200, 300, 140, 40)
input_box_rutinas = pygame.Rect(200, 500, 140, 40)  

color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color_peso = color_inactive
color_altura = color_inactive
color_rutinas = color_inactive

# Pecho=pygame.image.load(r'C:\Users\ASUS\Downloads\pecho.png')
# Bicep=pygame.image.load(r'C:\Users\ASUS\Downloads\bicep.png')
# Espalda=pygame.image.load(r'C:\Users\ASUS\Downloads\espalda.png')
# Hombro=pygame.image.load(r'C:\Users\ASUS\Downloads\hombro.png')
# Tricep=pygame.image.load(r'C:\Users\ASUS\Downloads\triceps.png')
# Abdomen=pygame.image.load(r'C:\Users\ASUS\Downloads\abdomen.png')
# Cardio=pygame.image.load(r'C:\Users\ASUS\Downloads\cardio.png')

# Npecho=pygame.transform.scale(Pecho,(75,75))
# Nbicep=pygame.transform.scale(Bicep,(75,75))
# Nespalda=pygame.transform.scale(Espalda,(75,75))
# Nhombro=pygame.transform.scale(Hombro,(75,75))
# Ntricep=pygame.transform.scale(Tricep,(75,75))
# Nabdomen=pygame.transform.scale(Abdomen,(75,75))
# Ncardio=pygame.transform.scale(Cardio,(75,75))

Ar_imagenes=[]

def login_screen():
    global logged_in, username_input, password_input, mostrar_error_login
    screen.fill(DarkBlue)

    pygame.draw.rect(screen, color_user, input_box_user, 2)
    pygame.draw.rect(screen, color_password, input_box_password, 2)

    user_text = Fuente.render(username_input, True, White)
    password_text = Fuente.render('*' * len(password_input), True, White)
    screen.blit(user_text, (input_box_user.x + 5, input_box_user.y + 5))
    screen.blit(password_text, (input_box_password.x + 5, input_box_password.y + 5))

    MensajeLogin = "Login"
    NmensajeLogin = Fuente.render(MensajeLogin, True, White)
    screen.blit(NmensajeLogin, (450, 200))

    pygame.draw.rect(screen, LightGreen, Button1)
    siguiente = calibri.render("Iniciar Sesión", True, (50, 100, 100))
    screen.blit(siguiente, (250, 620))

    if mostrar_error_login:
        error_msg = FuenteP.render("Usuario o contraseña incorrectos", True, White)
        screen.blit(error_msg, (350, 500))

    pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if not logged_in:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box_user.collidepoint(event.pos):
                    input_active_user = True
                    input_active_password = False
                elif input_box_password.collidepoint(event.pos):
                    input_active_password = True
                    input_active_user = False
                else:
                    input_active_user = False
                    input_active_password = False

                if Button1.collidepoint(event.pos):
                    dataUsers = user_repository.load_users()
                    for key,value in dataUsers.items():
                        if username_input == value["name"] and password_input == value["password"]:
                            logged_in = True
                            mostrar_error_login = False
                        else:
                            mostrar_error_login = True
                    # if username_input == valid_username and password_input == valid_password:
                    #     logged_in = True
                    #     mostrar_error_login = False
                    # else:
                    #     mostrar_error_login = True

            if event.type == pygame.KEYDOWN:
                if input_active_user:
                    if event.key == pygame.K_BACKSPACE:
                        username_input = username_input[:-1]
                    else:
                        username_input += event.unicode
                elif input_active_password:
                    if event.key == pygame.K_BACKSPACE:
                        password_input = password_input[:-1]
                    else:
                        password_input += event.unicode

            color_user = color_active if input_active_user else color_inactive
            color_password = color_active if input_active_password else color_inactive

            login_screen()
        
        else:
            def proceso():
                global resultado, etapa, dieta
                try:
                    Peso = int(peso_input)
                    Altura = float(altura_input)
                    IMC = Peso / (Altura ** 2)

                    if IMC < 18.5:
                        resultado = "Usted necesita una etapa de aumento de peso."
                        etapa = "volumen"
                        dieta = DietaVolumen()
                    elif IMC > 24.9:
                        resultado = "Usted necesita una etapa de déficit calórico."
                        etapa = "deficit"
                        dieta = DietaDeficitCalorico()
                    else:
                        resultado = "Su peso es ideal según la altura ingresada."
                        etapa = "ideal"
                        dieta = []
                except ValueError:
                    resultado = "Por favor, ingrese valores válidos."
                    dieta = []

            def DietaVolumen():
                return [
                    "4 huevos y una arepa desayuno",
                    "1 batido de proteina por la mañana y banano",
                    "150 gr de pescado/carnes/pollo y arroz al almuerzo",
                    "100 gr de pasta por la tarde",
                    "150 gr de pescado/carnes/pollo y aguacate en la cena"
                ]

            def DietaDeficitCalorico():
                return [
                    "4 huevos desayuno",
                    "1 batido de proteina por la mañana",
                    "150 gr de pescado/carnes/pollo y ensalada al almuerzo",
                    "Yogurt griego por la tarde",
                    "150 gr de pescado/carnes/pollo y aguacate en la cena"
                ]

            def RutinasSeleccionadas():
                global rutinas, Ar_imagenes
                rutinas = []
                Ar_imagenes=[]
                opciones = rutinas_input.split()
                for opcion in opciones:
                    try:
                        opcion = int(opcion)
                        if opcion == 1:
                            rutinas.append("Pecho: 4x12 press banca, inclinado, declinado, apertura, lagartijas")
                            # Ar_imagenes.append(Npecho)
                        elif opcion == 2:
                            rutinas.append("Biceps: 4x12 curl mancuerna, barra, martillo, negativas, polea")
                            # Ar_imagenes.append(Nbicep)
                        elif opcion == 3:
                            rutinas.append("Triceps: 4x15 fondos, 4x10 press frances, fallo en polea y barra")
                            # Ar_imagenes.append(Ntricep)
                        elif opcion == 4:
                            rutinas.append("Espalda: 4x12 barras, jalon mancuerna, remo unilateral y barra")
                            # Ar_imagenes.append(Nespalda)
                        elif opcion == 5:
                            rutinas.append("Hombro: 4x15 elevaciones laterales, frontales, press militar")
                            # Ar_imagenes.append(Nhombro)
                        elif opcion == 6:
                            rutinas.append("Abdomen: 4x12 rueda, abdominales bicicleta, tijeras")
                            # Ar_imagenes.append(Nabdomen)    
                        elif opcion == 7:
                            rutinas.append("Cardio: Trote 20 minutos, 4x10 burpees")
                            # Ar_imagenes.append(Ncardio)
                        else:
                            rutinas.append(f"Rutina inválida: {opcion}")
                    except ValueError:
                        rutinas.append(f"Entrada inválida: {opcion}")

            while verdadero:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        verdadero = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if input_box_peso.collidepoint(event.pos):
                            input_active_peso = True
                            input_active_altura = False
                            input_active_rutinas = False
                        elif input_box_altura.collidepoint(event.pos):
                            input_active_altura = True
                            input_active_peso = False
                            input_active_rutinas = False
                        elif input_box_rutinas.collidepoint(event.pos):
                            input_active_rutinas = True
                            input_active_peso = False
                            input_active_altura = False
                        else:
                            input_active_peso = False
                            input_active_altura = False
                            input_active_rutinas = False

                        if Button1.collidepoint(event.pos):
                            proceso()
                            RutinasSeleccionadas()
                            mostrar_resultado = True

                    if event.type == pygame.KEYDOWN:
                        if input_active_peso:
                            if event.key == pygame.K_BACKSPACE:
                                peso_input = peso_input[:-1]
                            else:
                                peso_input += event.unicode
                        elif input_active_altura:
                            if event.key == pygame.K_BACKSPACE:
                                altura_input = altura_input[:-1]
                            else:
                                altura_input += event.unicode
                        elif input_active_rutinas:
                            if event.key == pygame.K_BACKSPACE:
                                rutinas_input = rutinas_input[:-1]
                            else:
                                rutinas_input += event.unicode

                color_peso = color_active if input_active_peso else color_inactive
                color_altura = color_active if input_active_altura else color_inactive
                color_rutinas = color_active if input_active_rutinas else color_inactive

                screen.fill(DarkBlue)

                pygame.draw.rect(screen, color_peso, input_box_peso, 2)
                pygame.draw.rect(screen, color_altura, input_box_altura, 2)
                pygame.draw.rect(screen, color_rutinas, input_box_rutinas, 2)

                texto_peso = Fuente.render(peso_input, True, White)
                texto_altura = Fuente.render(altura_input, True, White)
                texto_rutinas = Fuente.render(rutinas_input, True, White)
                screen.blit(texto_peso, (input_box_peso.x + 5, input_box_peso.y + 5))
                screen.blit(texto_altura, (input_box_altura.x + 5, input_box_altura.y + 5))
                screen.blit(texto_rutinas, (input_box_rutinas.x + 5, input_box_rutinas.y + 5))

                pygame.draw.rect(screen, LightGreen, Button1)

                Mensaje = "Bienvenido al bodybuilder virtual"
                Nmensaje = Fuente.render(Mensaje, True, White)
                screen.blit(Nmensaje, (320, 25))

                text1 = "Ingrese su peso en kg"
                Ntext1 = FuenteP.render(text1, True, White)
                screen.blit(Ntext1, (20, 200))

                text2 = "Ingrese su altura en metros"
                Ntext2 = FuenteP.render(text2, True, White)
                screen.blit(Ntext2, (20, 300))

                text3 = "Ingrese su rutina"
                Ntext3 = FuenteP.render(text3, True, White)
                screen.blit(Ntext3, (20, 500))

                text4 = "Rutinas: 1.pecho, 2.Bicep, 3.bicep"
                Ntext4 = FuenteP.render(text4, True, White)
                screen.blit(Ntext4, (20, 430))

                text5 = "4.espalda, 5.hombro, 6.abdomen, 7.cardio"
                Ntext5 = FuenteP.render(text5, True, White)
                screen.blit(Ntext5, (20, 445))

                text6 = "si quiere 2 o mas rutinas separe los numeros por espacios"
                Ntext6 = FuenteP.render(text6, True, White)
                screen.blit(Ntext6, (20, 460))
                
                siguiente = calibri.render("siguiente", True, (50, 100, 100))
                screen.blit(siguiente, (250, 620))

                if mostrar_resultado:
                    ResultadoTexto = Fuente.render(resultado, True, White)
                    screen.blit(ResultadoTexto, (350, 150))
                    y=200
                    if dieta:
                            
                        for linea in dieta:
                            DietaTexto = FuenteP.render(linea, True, White)
                            screen.blit(DietaTexto, (500, y))
                            y += 30

                    if rutinas:
                        for i, rutina in enumerate(rutinas):
                            RutinaTexto = FuenteP.render(rutina, True, White)
                            screen.blit(RutinaTexto, (500, y+50))
                            y += 30
                            screen.blit(Ar_imagenes[i],(500, y+50))
                            y +=85

                pygame.display.update()

            pygame.quit()
            sys.exit()