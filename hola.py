nombre = input("¿Cómo te llamás? ")
edad = int(input("¿Cuántos años tenés? "))

if edad >= 65:
    mensaje = f"¡Hola, {nombre}! Con {edad} años, eres una persona muy experimentada."
elif edad >= 18:
    mensaje = f"¡Hola, {nombre}! Con {edad} años, eres un adulto."
else:
    mensaje = f"Wow, sos muy joven! {nombre}"
print(mensaje)
