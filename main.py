import pyautogui
import pandas as pd
import time
import keyboard

blacklist = ["INA", "INCOPARTS", "MASTER", "MASTERFLEX", "UNIVERSAL", "VALCLEI", "ZF", "NTK", "NGK", "ZM", "Pérola Automotivo"]
df = pd.read_excel('../file/Molina.xlsx')
sleep = 1

marcas_blacklist = []

iniciar_de_linha_especifica = input("Deseja iniciar a partir de uma linha específica? (S/N): ").strip().upper()

if iniciar_de_linha_especifica == 'S':
    linha_inicial = int(input("Digite o número da linha para começar: "))
else:
    linha_inicial = 0

contador = linha_inicial + 1
item_anterior_blacklist = False

acao_bot = input("Escolha a ação do bot:\n1: Inserir \n2: Revisar \n").strip()

for i in range(3, 0, -1):
    print(f"O script começará em {i} segundos. Prepare o ambiente!")
    time.sleep(1)
#select
pyautogui.click(x=-1361, y=448)
time.sleep(sleep)

for index, row in df.iterrows():
    if index < linha_inicial:
        continue

    if keyboard.is_pressed('esc'):
        print("Bot interrompido pelo usuário!")
        break

    dado = str(row[0])

    if dado in blacklist:
        marcas_blacklist.append(dado)
        print(f"Marca {dado} é blacklist.")
        contador += 1
        if not item_anterior_blacklist:
            time.sleep(3)
        item_anterior_blacklist = True
        continue
    print(f"{contador}: {dado}")

    pyautogui.write(dado)

    #click
    if acao_bot == '1':
      pyautogui.click(x=-1330, y=567)
      time.sleep(sleep)

    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')

    item_anterior_blacklist = False
    contador += 1

print("Ok\n")

if marcas_blacklist:
    print("##################")
    print(f"total de marcas em blacklist para esse catálogo: {len(marcas_blacklist)}\n")
    print("Lista de marcas----------")
    for marca in marcas_blacklist:
        print(marca)
else:
    print("Nenhuma marca foi encontrada no blacklist")
