import random

caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
cantidad = int(input("¿Cuantos caracteres quiere que tu contraseña tenga?"))
contra = ""
for i in range(cantidad):
    letra = random.choice(caracteres)
    contra = contra + letra
print("Tu contraseña creada es", contra)
