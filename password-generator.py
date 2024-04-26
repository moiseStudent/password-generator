import random

class Password_Generator:

    def __init__(self, password_length: int, list_lowercase: list, list_uppercase: list, asci: list):

        if password_length < 10:
            print("He generado una contrasena con 10 caracteres de minimo.")
            self.password_length = 10

        else:
            self.password_length = password_length

        self.lower_case = list_lowercase
        self.upper_case = list_uppercase
        self.special_characters = asci
    
    def password_creator(self):
        password_list = []

        i = 0
        while i < self.password_length:
            
            """
            La funcion len no empieza a contar desde el numero cero "0", por
            ende se le resta uno "1" a las variables para poder generar un numero
            con "random.randint()" desde cero "0" hasta el limite de la lista.
            """
            letter_lower = len(self.lower_case) - 1
            letter_lower = random.randint(0, letter_lower)

            letter_upper = len(self.upper_case) - 1
            letter_upper = random.randint(0, letter_upper)

            special_character = len(self.special_characters) - 1
            special_character = random.randint(0, special_character)

            num_list = random.randint(1, 4)

            ### Elije el caracter a agregar de forma aleatoria ###
            if num_list == 1:
                password_list.append(self.lower_case[letter_lower])
            
            elif num_list == 2:
                password_list.append(self.upper_case[letter_upper])
            
            elif num_list == 3:
                password_list.append(self.special_characters[special_character])

            elif num_list == 4:    
                password_list.append(random.randint(0,9))

            i += 1
        
        return self._password_reset(password_list)
    
    def _password_reset(self, password):

        password = str(password).replace('[',"").replace("'","").replace(",","")
        password = password.replace(" ","").replace("]","")

        return password

alphabet_lower = [
    'a','b','c','d','e','f','g',
    'h','i','j','k','l','m','n','o','p',
    'q','r','s','t','u','v','w','x','y','z'
    ]

alphabet_upper = [
    'A','B','C','D','E','F','G',
    'H','I','J','K','L','M','N','O','P',
    'Q','R','S','T','U','V','W','X','Y','Z'
    ]

special = [
    '!','@','#',
    '$','%','&',
    '*','(',')',
    '-','_','=',
    '+','{','}',
    '|',';',':',
    '"','<','>',
    '.','?','/',
    '`','~','#'
]

length_password = int(input("Ingresa la longitud que quieres para la password: "))

### Creation object ###
generator = Password_Generator(length_password, alphabet_lower, alphabet_upper, special)

### Generando una contrasena ###
print(generator.password_creator())
