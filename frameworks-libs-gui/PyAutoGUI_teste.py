# Permite desenvolver aplicações python que controlem o mouse e o teclado para automatizar as interações com outros aplicativos.
# Uma das situações em que essa característica pode ser muito interessante é na implementação de testes que simulem a interação do usuário com o sistema.

# PyAutoGUI funciona no Windows, macOS e Linux e é executado no python.

import pyautogui

screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()
pyautogui.moveTo(100, 150)
pyautogui.click()
pyautogui.click(100, 200)
pyautogui.move(0, 10)
pyautogui.doubleClick()
pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad)
pyautogui.write('Ola, Mundo!', interval=0.25)
pyautogui.press('esc')
pyautogui.keyDown('shift')
pyautogui.press(['left', 'left', 'left', 'left'])
pyautogui.keyUp('shift')
pyautogui.hotkey('ctrl', 'c')
pyautogui.alert('Esta é a mensagem para Tela.')