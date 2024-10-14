import pyautogui
import time

print("Pressione 'Ctrl + C' para interromper a captura das coordenadas.")

try:
    while True:
        x, y = pyautogui.position()
        print(f"Posição atual do mouse: X={x}, Y={y}")
        time.sleep(1)
except KeyboardInterrupt:
    print("\nCaptura de posição interrompida.")
