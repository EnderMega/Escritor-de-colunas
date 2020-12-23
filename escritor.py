import pyautogui
import time

f = input("Insira os números: ")                      # Inserir números, pode ter espaço ou virgulas entre eles
c = int(input("Número de colunas: "))                 # Entra quantas colunas ele vai percorrer antes de descer uma
tempo = 0
print("*Tudo pronto*")                                # Aparece '*Tudo pronto*' na tela

s = f.replace(',', ' ')                               # Substitui as vírgulas por espaços

time.sleep(3)

for n in s:
    if n == ' ':                                      # Da o espaço de colunas
        pyautogui.press("right")
        tempo = tempo + 1
    if tempo == c:                                    # Desce  uma coluna e volta para a primeira coluna
        pyautogui.press("down")
        for i in range(c):                            # Volta para a primeira coluna
            pyautogui.press("left")
        tempo = 0
    else:
        pyautogui.typewrite(n)                        # Escreve o valor
