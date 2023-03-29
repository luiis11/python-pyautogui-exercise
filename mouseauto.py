import pyautogui
import random
import time
import sys

print("Programa Iniciado. Presione \"Q\" para salir")

# Definimos los límites del área en la que queremos mover el mouse
# en este caso, lo limitamos a la mitad de la pantalla
x_min, y_min, x_max, y_max = pyautogui.size()[0]//4, pyautogui.size()[1]//4, pyautogui.size()[0]//2, pyautogui.size()[1]//2

while True:
	# Generamos coordenadas aleatorias dentro del área definida
	x = random.randint(x_min, x_max)
	y = random.randint(y_min, y_max)

	# Movemos el mouse a las coordenadas aleatorias
	pyautogui.moveTo(x, y, duration=0.1)

	# Enviamos una pulsacion a una tecla cualquiera. En este caso a Bloq Num (para evitar que se suspenda el equipo)
	pyautogui.press('numlock')
	# Enviamos una segunda pulsacion para volver al estado original del NumLock
	pyautogui.press('numlock')

	# Esperamos un tiempo aleatorio entre 10 a 60 segundos antes de mover el mouse nuevamente
	time.sleep(random.randint(10, 60))

print("Programa terminado.")
