import pyautogui
import time

print("Posicione o cursor sobre o local desejado.")
time.sleep(5)  # Tempo para você posicionar o cursor
x, y = pyautogui.position()
print(f'Coordenadas: x={x}, y={y}')
