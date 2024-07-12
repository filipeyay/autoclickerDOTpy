import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

btn = Button.right
delay = 0.001
key_iniciar_parar = KeyCode(
    char="a"
)  # letra 'a' do teclado tanto inicia quanto para o clicker
key_parar = KeyCode(
    char="b"
)  # letra 'b' do teclado serve como uma tecla alternativa para parar o script


class Click(threading.Thread):
    def __init__(self, delay, btn):
        super(Click, self).__init__()
        self.delay = delay
        self.btn = btn
        self.rodando = False
        self.programaRodando = True

    def click_inicar(self):
        self.rodando = True

    def click_parar(self):
        self.rodando = False

    def exit(self):
        self.click_parar()
        self.programaRodando = False

    def run(self):
        while self.programaRodando:
            while self.rodando:
                mouse.click(self.btn)
                time.sleep(self.delay)
            time.sleep(0.1)


mouse = Controller()
click_thread = Click(delay, btn)
click_thread.start()


def on_press(key):
    if key == key_iniciar_parar:
        if click_thread.rodando:
            click_thread.click_parar()
        else:
            click_thread.click_inicar()

    elif key == key_parar:
        click_thread.exit()
        listener.stop()


with Listener(on_press=on_press) as listener:
    listener.join()
