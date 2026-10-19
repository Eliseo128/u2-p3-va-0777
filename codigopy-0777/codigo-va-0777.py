# Importamos las librerias
import cv2
import matplotlib.pyplot as plt
import os
#ruta de la imagen
ruta_imagen = os.path.join(
    "img-original-0777",
    "mochila.jpg"
)
# Imagen
# Vamos a crear nuestra matriz principal
mochila = cv2.imread(ruta_imagen)
# print(mochila) mustra las matrices de la imagen
# # Convertir de BGR a RGB  color rojo COLOR_BGR2RGB
mochi = cv2.cvtColor(mochila, cv2.COLOR_BGR2RGB)
#cv2.imshow("mochila original 0777",mochila )
cv2.imshow("mochila color0777",mochi )
cv2.waitKey(0) # tiempo de espera
cv2.destroyAllWindows() # destruye todas la ventanas en memoria