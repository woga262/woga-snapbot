try:
   from colorama import Fore
   import ctypes, pyautogui, keyboard, os, time, platform
   from datetime import datetime
except ImportError:
    input("Modülleri içe aktarırken hata oluştu. Lütfen şu modülleri kurun, requirements.txt")


ascii_text = """
░██╗░░░░░░░██╗░█████╗░░██████╗░░█████╗░  ░██████╗███╗░░██╗░█████╗░██████╗░  ██████╗░░█████╗░████████╗
░██║░░██╗░░██║██╔══██╗██╔════╝░██╔══██╗  ██╔════╝████╗░██║██╔══██╗██╔══██╗  ██╔══██╗██╔══██╗╚══██╔══╝
░╚██╗████╗██╔╝██║░░██║██║░░██╗░███████║  ╚█████╗░██╔██╗██║███████║██████╔╝  ██████╦╝██║░░██║░░░██║░░░
░░████╔═████║░██║░░██║██║░░╚██╗██╔══██║  ░╚═══██╗██║╚████║██╔══██║██╔═══╝░  ██╔══██╗██║░░██║░░░██║░░░
░░╚██╔╝░╚██╔╝░╚█████╔╝╚██████╔╝██║░░██║  ██████╔╝██║░╚███║██║░░██║██║░░░░░  ██████╦╝╚█████╔╝░░░██║░░░
░░░╚═╝░░░╚═╝░░░╚════╝░░╚═════╝░╚═╝░░╚═╝  ╚═════╝░╚═╝░░╚══╝╚═╝░░╚═╝╚═╝░░░░░  ╚═════╝░░╚════╝░░░░╚═╝░░░"""
                       
def onLinux():
    if platform.system() == "Linux":
        return True
    else:
        return False

class snapchat:

    def __init__(self):
        self.sent_snaps = 0
        self.delay = 1.3

    def get_positions(self):
        self.print_console("Farenizi kamera düğmesine getirin, Sonra 'F' tuşuna basınız.")
        while True:
            if keyboard.is_pressed("f"):
                self.switch_to_camera = pyautogui.position()
                break
        time.sleep(0.5)
        self.print_console("Farenizi fotoğraf çek düğmesine getirin, Sonra 'F' tuşuna basınız.")
        while True:
            if keyboard.is_pressed("f"):
                self.take_picture = pyautogui.position()
                break
        time.sleep(0.5)
        self.print_console("Farenizi aşağı ok düğmesine getirin, Sonra 'F' tuşuna basınız.")
        while True:
            if keyboard.is_pressed("f"):
                self.arrow_down = pyautogui.position()
                break
        time.sleep(0.5)
        self.print_console("Farenizi Çoklu Snap düğmesine getirin, Sonra 'F' tuşuna basınız.")
        while True:
            if keyboard.is_pressed("f"):
                self.multi_snap = pyautogui.position()
                break
        time.sleep(0.5)
        self.print_console("Farenizi Düzenle & Gönder düğmesine getirin, Sonra 'F' tuşuna basınız.")
        while True:
            if keyboard.is_pressed("f"):
                self.edit_send = pyautogui.position()
                break
        time.sleep(0.5)
        self.print_console("Farenizi Gönder düğmesine getirin, Sonra 'F' tuşuna basınız.")
        while True:
            if keyboard.is_pressed("f"):
                self.send_to = pyautogui.position()
                break
        time.sleep(0.5)
        self.print_console("Farenizi kısayolunuza taşıyın, Sonra 'F' tuşuna basınız.")
        while True:
            if keyboard.is_pressed("f"):
                self.shortcut = pyautogui.position()
                break
        time.sleep(0.5)
        self.print_console("Kısayolda tümünü seçmek için farenizi hareket ettirin, Sonra 'F' tuşuna basınız.")
        while True:
            if keyboard.is_pressed("f"):
                self.select_all = pyautogui.position()
                break
        time.sleep(0.5)
        self.print_console("Ek düğme göndermek için farenizi hareket ettirin, Sonra 'F' tuşuna basınız.")
        while True:
            if keyboard.is_pressed("f"):
                self.send_snap_button = pyautogui.position()
                break
    
    def send_snap(self, shortcut_users):
        self.update_title(shortcut_users)
        pyautogui.moveTo(self.switch_to_camera)
        pyautogui.click()
        time.sleep(self.delay)
        pyautogui.moveTo(self.take_picture)
        for i in range(7):
            pyautogui.click()
            time.sleep(self.delay)
        pyautogui.moveTo(self.edit_send)
        time.sleep(self.delay)
        pyautogui.click()
        pyautogui.moveTo(self.send_to)
        pyautogui.click()
        time.sleep(self.delay)
        pyautogui.moveTo(self.shortcut)
        pyautogui.click()
        time.sleep(self.delay)
        pyautogui.moveTo(self.select_all)
        pyautogui.click()
        pyautogui.moveTo(self.send_snap_button)
        pyautogui.click()
        self.sent_snaps += 7
        self.update_title(shortcut_users)
    
    def update_title(self, shortcut_users):
        now = time.time()
        elapsed = str(now - self.started_time).split(".")[0]
        sent_snaps = self.sent_snaps * shortcut_users
        if onLinux() == False:
            ctypes.windll.kernel32.SetConsoleTitleW(f"Woga Snapchat Score Botter | Gönderilen Snapler: {sent_snaps} | Elapsed: {elapsed}s | Developed by woga")

    def print_console(self, arg, status = "Console"):
        print(f"\n       {Fore.WHITE}[{Fore.RED}{status}{Fore.WHITE}] {arg}")
    
    def main(self):
        if onLinux() == False:
            os.system("cls")
            ctypes.windll.kernel32.SetConsoleTitleW("Woga Snapchat Score Botter | Developed by woga")
        else:
            os.system("clear")

        print(Fore.RED + ascii_text)

        self.get_positions()

        # Sometimes ran into "ValueError: invalid literal for int() with base 10: 'fffffffff2'"
        # There should be a better solution for this but I am not a python dev - woga
        while True:
            try:
                shortcut_users = int(input(f"\n       {Fore.WHITE}[{Fore.RED}Console{Fore.WHITE}] Bu kısayolda kaç kişi var?: "))
                break
            except ValueError:
                print(f"\n       {Fore.WHITE}[{Fore.RED}Console{Fore.WHITE}] Bu girişle ilgili bir hata oluştu, lütfen tekrar deneyin:) ")

        self.print_console("Yavaş Bilgisayar", "1")
        self.print_console("Hızlı Bilgisayar", "2")
        options = int(input(f"\n       {Fore.WHITE}[{Fore.RED}Console{Fore.WHITE}] Ayar: "))
        if options == 1:
            self.delay = 2
        self.print_console("Sohbetlerinize gidin, ardından okunduğunuzda F tuşuna basınız.")
         
        while True:
            if keyboard.is_pressed("f"):
                break
        if onLinux() == False:
            os.system("cls")
        else:
            os.system("clear")
        print(Fore.RED + ascii_text)
        self.print_console("Snapler gönderiliyor...")
        self.started_time = time.time()
        while True:
            if keyboard.is_pressed("F4"):
                break
            self.send_snap(shortcut_users)
            time.sleep(4)
        self.print_console(f"Toplamda {self.sent_snaps} adet snap gönderildi.")

obj = snapchat()
obj.main()
