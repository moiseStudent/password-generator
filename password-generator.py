import random
import os
from colorama import Fore as f_, init, Back
from constants import *

### Initiation colorama ###
init(autoreset=True)

class Password_Generator:
    #* class variables
    list_lowercase = ALPHABET_LOWER
    list_uppercase = ALPHABET_UPPER
    list_specialC = SPECIAL

    def __init__(self, password_length: int, uppercase: bool, special: bool, numbers: bool):

        self.uppercase = uppercase
        self.special = special
        self.numbers = numbers

        if password_length < 10:

            print(f"{f_.RED}Error: Las claves deben ser de un minimo de 10 digitos !!!{f_.RESET}")
            print(f"{f_.CYAN}Igualmente te genere una clave, tiene 10 digitos de minimo.{f_.RESET}")

            self.password_length = 10

        else:
            self.password_length = password_length
    
    def password_creator(self):
        password_list = []

        i = 0
        while i < self.password_length:
            
            """
            La funcion len no empieza a contar desde el numero cero "0", por
            ende se le resta uno "1" a las variables para poder generar un numero
            con "random.randint()" desde cero "0" hasta el limite de la lista.
            """
            
            letter_lower = len(self.list_lowercase) - 1
            letter_lower = random.randint(0, letter_lower)
            
            letter_upper = len(self.list_uppercase) - 1
            letter_upper = random.randint(0, letter_upper)
            
            special_character = len(self.list_specialC) - 1
            special_character = random.randint(0, special_character)

            num_list = random.randint(1, 4)
            
            ### Elije el caracter a agregar de forma aleatoria ###
            if num_list == 1:
                password_list.append(self.list_lowercase[letter_lower])
            
            elif num_list == 2 and self.uppercase:
                password_list.append(self.list_uppercase[letter_upper])
            
            elif num_list == 3 and self.special:
                password_list.append(self.list_specialC[special_character])
                
            elif num_list == 4 and self.numbers:    
                password_list.append(random.randint(0,9))
                
            else:
                password_list.append(self.list_lowercase[letter_lower])
            i += 1
        
        return f"\nClave: {f_.CYAN}{self.password_format(password_list)}{f_.RESET}"  
    
    def password_format(self, password):

        password = str(password).replace('[',"").replace("'","").replace(",","")      
        password = password.replace(" ","").replace("]","")

        return password






def clear_screen():
### check operative system ###
    if os.name == 'nt':
        os.system('cls')
    
    else:
        os.system('clear')

def check_response(variable:str, character:str):
    if variable.lower() == "si":
        variable = True
        return variable
    
    elif variable.lower() == "no":
        variable = False
        return variable
    else:
        input(f"""{f_.RED}respuesta no valida, intenta de nuevo respondiendo si o no. (si quieres salir presiona ctrl + C)
                {f_.BLUE}presiona enter para continuar\n{f_.RESET}""")
        variable = input(f"Quieres que la contraseña contenga {character} ?\n") 
        return check_response(variable,character) 
def main():
    
    clear_screen()

    while True:
        print(f"\n{Back.RED}.:Bienvenid@ a \"Generator password\":.{Back.RESET}\n")
        print(f"Presion {f_.MAGENTA}CTRL + C{f_.RESET} para salir del programa")
        
        try:
            #* Request Data
            length_password = int(input("Ingresa la longitud que quieres para la password: "))

            uppercase = input("Quieres que la contraseña tenga mayusculas ? \n")
            uppercase = check_response(uppercase, "letras mayusculas")
            
            special = input("Quieres que la contraseña tenga caracteres especiales ? \n")
            special = check_response(special,"caracteres especiales")

            numbers = input("Quieres que la contraseña tenga numeros ? \n")
            numbers = check_response(numbers, "numeros")
            
            #*## Creation object ###
            generator = Password_Generator(length_password, uppercase, special, numbers)
            print(generator.password_creator())

        except ValueError:
            print(f"{f_.RED}Error: Caracter invalido !!!{f_.RESET}\n")
        
        input(f"{f_.BLUE}Al continuar se reiniciara la pantalla ...{f_.RESET}")
        clear_screen()
            
        
    


try:
    main()

except KeyboardInterrupt:
    print(f"\n{f_.CYAN}Gracias por usar 'Generator password'{f_.RESET}")
        

