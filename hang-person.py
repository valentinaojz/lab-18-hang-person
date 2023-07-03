word_to_guess = "computador"
user_option = " "
display_word = "_ " *len(word_to_guess)
user_chars = [4]
print ("Bienvenido al ahorcadito")
print (display_word)
hang_person = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']
print (hang_person [0])
while user_option != "3":
    print ("Adivina esta palabra si quieres vivir \n")
    print ("1. Adivinar")
    print ("2. Resulatados")
    print ("3. Salir")    
    user_option = input ("Indica una opción\n")    
    if user_option == "1":
        exit_game = False
        while not exit_game:
            print ("Intanta adivinando una letra o la palabra completa: ")
            print ("Escribe salir para volver al menú principal")
            user_guess = input ()
            guess_word = " "            #Si el usuario ingreso una letra
            if len (user_guess) == 1:
                #Si es una letra nueva, se agrega al listado de letras indentadas
                if not user_guess in user_chars:
                    user_chars.append(user_guess)                
                    if (user_guess in word_to_guess):
                        print ("Adivinaste una letra")
                    for char in word_to_guess:
                        if char in user_chars:
                            guess_word += char
                        else:
                            guess_word += "_ "
                    print (guess_word)
                else:
                    print ("Esta letra no está en la palabra")
                    print (hang_person [len(user_chars )])
            #Si el usuario quiere volver al menú principal
            elif user_guess == "salir":
                exit = True
            #Sie el usuario intento una palabra
            else:
                #Si la palabra del usuario es la misma
                if (user_guess == word_to_guess):
                    print ("¡Ganaste!")
                    exit ()
                else:
                    print ("No no no")
                    print ("Perdiste y te quemaras en el infierno")
                    print (hang_person [-1])
                    exit (1)
    elif user_option == "2":
        print (f"Has intentado las siguientes letras:{user_chars}")
    elif user_option == "3" :
        print ("chausito")


