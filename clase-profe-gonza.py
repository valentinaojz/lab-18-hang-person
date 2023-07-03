letras = []
palabra = "rana"

palabra_mostrada = "_ " * len(palabra)
print(palabra_mostrada)

letra_usuario = input("Ingrese una letra \n")
 
if(letra_usuario in palabra):
 print("Adivinaste una letra")
 for letra in palabra:
  if (letra == palabra):
   palabra_mostrada +=letra_usuario
  else: 
     palabra_mostrada += letra_usuario
else:      
 print("No adivinaste")
  