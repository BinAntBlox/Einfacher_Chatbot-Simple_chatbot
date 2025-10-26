import webbrowser
import random
import time
import sys
import os
import json
import cv2
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

try:
    import msvcrt  # Windows für Passwort
except ImportError:
    msvcrt = None

# Farben
ORANGE = "\033[38;5;208m"
PURPLE = "\033[95m"
RESET = "\033[0m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RED = "\033[91m"
BOLD = "\033[1m"

# Benutzer & Passwort
BENUTZERNAME = "Admin"
PASSWORT = "Secret"

KONTEXT_DATEI = "ki2_kontext.json"

# --- Type Print Funktionen ---
def type_print(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def type_print_natural(text):
    for char in text:
        if random.random() < 0.02 and char.isalpha():
            sys.stdout.write(random.choice("abcdefghijklmnopqrstuvwxyz"))
            sys.stdout.flush()
            time.sleep(random.uniform(0.05, 0.15))
            sys.stdout.write("\b \b")
            sys.stdout.flush()
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(random.uniform(0.02, 0.07))
        if char in ".!?":
            time.sleep(0.3 + random.random() * 0.2)
        elif char in ",;:":
            time.sleep(0.15 + random.random() * 0.1)
    print()

def type_print_calc(text):
    for char in str(text):
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(random.uniform(0.02, 0.07))
    print()

def type_print_menu(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(random.uniform(0.02, 0.06))
    print()

# --- Hilfsfunktionen ---
def clear():
    os.system("cls" if os.name == "nt" else "clear")

def frage_ja_nein(prompt):
    while True:
        antwort = input(YELLOW + prompt + RESET).strip().lower()
        if antwort in ["j", "n"]:
            return antwort == "j"
        type_print(RED + "Bitte 'j' für ja oder 'n' für nein eingeben." + RESET)

# --- Ladebalken ---
def ladebalken(text="Ladevorgang"):
    sys.stdout.write(text)
    sys.stdout.flush()
    for _ in range(10):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(random.uniform(0.15, 0.25))
    print(" Fertig!\n")
    time.sleep(0.3)

# --- Start-Logo ---
def start_logo():
    os.system("cls" if os.name == "nt" else "clear")
    logo_static = """
   ____          _           ____        _   
  / ___|___   __| | ___  ___| __ )  ___ | |_ 
 | |   / _ \ / _` |/ _ \/ _ \  _ \ / _ \| __|
 | |__| (_) | (_| |  __/| __/ |_) | (_) | |_ 
  \____\___/ \__,_|\___|\___|____/ \___/ \__|
                     v18.9
"""
    type_print_natural(CYAN + "Starte CodeeBot..." + RESET)
    blink_state = True
    start_time = time.time()
    while time.time() - start_time < 3:
        color = ORANGE if blink_state else YELLOW
        sys.stdout.write("\033[H\033[J")
        print(BOLD + color + logo_static + RESET)
        print(CYAN + "Willkommen bei Codee" + color + BOLD + "Bot!" + RESET)
        blink_state = not blink_state
        time.sleep(0.4)
    os.system("cls" if os.name == "nt" else "clear")

# --- Passwort-Eingabe ---
def passwort_eingabe(prompt="Passwort: "):
    eingabe = ""
    sys.stdout.write(prompt)
    sys.stdout.flush()
    if msvcrt:
        while True:
            key = msvcrt.getch()
            if key in [b'\r', b'\n']:
                print()
                break
            elif key == b'\x08':
                if eingabe:
                    eingabe = eingabe[:-1]
                    sys.stdout.write("\b \b")
                    sys.stdout.flush()
            elif key == b'#':
                sys.stdout.write("\r" + prompt + eingabe)
                sys.stdout.flush()
                time.sleep(1)
                sys.stdout.write("\r" + prompt + "*" * len(eingabe))
                sys.stdout.flush()
            else:
                try:
                    char = key.decode()
                    eingabe += char
                    sys.stdout.write("*")
                    sys.stdout.flush()
                except:
                    continue
    else:
        import getpass
        eingabe = getpass.getpass(prompt)
    print()
    return eingabe

# --- Login ---
def login():
    attempts = 3
    while attempts > 0:
        benutzer = input("Benutzername: ")
        pw = passwort_eingabe()
        if benutzer == BENUTZERNAME and pw == PASSWORT:
            ladebalken("Zugriff wird geprüft")
            type_print_natural(GREEN + "Login erfolgreich!" + RESET)
            return True
        else:
            attempts -= 1
            type_print_natural(RED + f"Falscher Benutzername oder Passwort! Versuche übrig: {attempts}" + RESET)
    type_print_natural(RED + "Zu viele Fehlversuche. Programm wird beendet." + RESET)
    return False

# --- Shutdown ---
def shutdown():
    ladebalken("System wird heruntergefahren")
    type_print_natural(CYAN + "Auf Wiedersehen!" + RESET)
    sys.exit(0)

# --- Basisfunktionen ---
def open_google():
    print("Search...")
    time.sleep(1)
    ladebalken("Google wird geöffnet")
    webbrowser.open("https://google.com")
    type_print_natural(GREEN + "Google geöffnet!" + RESET)

def open_codinggiants():
    print("Search...")
    time.sleep(1)
    ladebalken("CodingGiants wird geöffnet")
    webbrowser.open("https://codinggiants.de")
    type_print_natural(GREEN + "CodingGiants geöffnet!" + RESET)

def kopieren():
    text = input("Bitte Text eingeben: ")
    type_print_natural(CYAN + f"Kopie: {text}" + RESET)

def witz():
    witze = [
        "Zwei Zahnstocher gehen durch den Wald. Kommt ein Igel vorbei: 'Ich wusste gar nicht, dass hier ein Bus fährt!'",
        "Warum können Geister nicht lügen? – Man sieht direkt durch sie hindurch!",
        "Was machen Piraten am Computer? – Sie drücken die Enter-Taste.",
        "Was ist orange und läuft durch den Wald? – Eine Wanderine!",
        "Einer schießt aus Versehen auf den anderen und ruft die Polizei...",
        "In einem Haus wohnten drei Leute: Keiner, Niemand und Blöd..."
    ]
    while True:
        type_print_calc(random.choice(witze))
        if input("Noch ein Witz? (j/n): ").lower() != "j":
            break

def volumen_wuerfel():
    while True:
        try:
            s = float(input("Seitenlänge des Würfels: "))
            type_print_calc(GREEN + f"Volumen: {s ** 3}" + RESET)
        except ValueError:
            type_print_natural(RED + "Ungültige Eingabe!" + RESET)
        if input("Noch ein Volumen berechnen? (j/n): ").lower() != "j":
            break

def durchschnittsgeschwindigkeit():
    while True:
        try:
            strecke = float(input("Strecke in km: "))
            zeit = float(input("Zeit in Minuten: "))
            if zeit == 0:
                type_print_natural(RED + "Zeit darf nicht 0 sein!" + RESET)
                continue
            kmh = strecke / (zeit / 60)
            type_print_calc(GREEN + f"Durchschnittsgeschwindigkeit: {round(kmh, 2)} km/h" + RESET)
        except ValueError:
            type_print_natural(RED + "Ungültige Eingabe!" + RESET)
        if input("Noch eine Berechnung? (j/n): ").lower() != "j":
            break

def taschenrechner():
    while True:
        try:
            num1 = float(input("Erste Zahl: "))
            while True:
                op = input("Operation (+,-,*,/): ")
                num2 = float(input("Zweite Zahl: "))
                if op == "+": ergebnis = num1 + num2
                elif op == "-": ergebnis = num1 - num2
                elif op == "*": ergebnis = num1 * num2
                elif op == "/":
                    if num2 == 0:
                        type_print_natural(RED + "Division durch 0 nicht erlaubt!" + RESET)
                        continue
                    ergebnis = num1 / num2
                else:
                    type_print_natural(RED + "Ungültige Operation!" + RESET)
                    continue
                type_print_calc(GREEN + f"Ergebnis: {ergebnis}" + RESET)
                if input("Mit Ergebnis weiterrechnen? (j/n): ").lower() != "j": break
                num1 = ergebnis
        except ValueError:
            type_print_natural(RED + "Ungültige Eingabe!" + RESET)
        if input("Neue Berechnung? (j/n): ").lower() != "j": break

def prozentsatz():
    while True:
        try:
            gesamt = float(input("Gib die Gesamtzahl ein: "))
            teil = float(input("Gib den Teilwert ein: "))
            if gesamt == 0:
                type_print_natural(RED + "Die Gesamtzahl darf nicht 0 sein!" + RESET)
                continue
            prozent = (teil / gesamt) * 100
            type_print_calc(GREEN + f"{teil} von {gesamt} sind {prozent:.2f}%" + RESET)
        except ValueError:
            type_print_natural(RED + "Ungültige Eingabe!" + RESET)
            continue
        if input("Noch etwas berechnen? (j/n): ").strip().lower() != "j":
            break

# --- Kontext-Chatbot ---
def lade_kontext():
    if os.path.exists(KONTEXT_DATEI):
        with open(KONTEXT_DATEI, "r") as f:
            return json.load(f)
    return {
        "name": "", 
        "hobbys": [], 
        "plaene": [], 
        "gefuehle": [],
        "lieblingsdinge": [],
        "routine": [],
        "erinnerungen": [],
        "gesprochen": []
    }

def speichere_kontext(kontext):
    with open(KONTEXT_DATEI, "w") as f:
        json.dump(kontext, f, indent=2)

def begruessung(kontext):
    if kontext["name"]:
        name = kontext["name"]
        type_print(CYAN + f"Willkommen zurück, {name}!" + RESET)
    else:
        type_print(CYAN + BOLD + "Hallo! Wie darf ich dich nennen?" + RESET)
        name = input("> ").strip().capitalize() or "Freund"
        kontext["name"] = name
        speichere_kontext(kontext)
        type_print(GREEN + f"Freut mich, dich zu treffen, {name}!" + RESET)
    return name

def stimmung_analyse(text):
    text = text.lower()
    positiv = ["gut", "super", "toll", "prima", "klasse", "fantastisch", "genial", "mega"]
    negativ = ["schlecht", "traurig", "mies", "blöd", "kaputt", "gestresst", "doof", "nicht gut"]
    neutral = ["ok", "geht so", "naja", "mittel", "so lala"]

    if any(w in text for w in positiv):
        return "gut"
    elif any(w in text for w in negativ):
        return "schlecht"
    elif any(w in text for w in neutral):
        return "neutral"
    else:
        return "unbekannt"

def motivierende_sprueche():
    sprueche = [
        "Du schaffst alles, was du willst!",
        "Jeder Tag bietet neue Chancen.",
        "Auch kleine Schritte führen zum Ziel.",
        "Manchmal hilft einfach tief durchzuatmen.",
        "Selbst Sterne brauchen Dunkelheit, um zu leuchten."
    ]
    return random.choice(sprueche)

def witz_des_tages():
    witze = [
        "Was macht ein Pirat am Computer? – Er drückt die Enter-Taste.",
        "Warum können Geister keine Lügen erzählen? – Man sieht direkt durch sie hindurch.",
        "Wie nennt man eine Gruppe von Wolfen, die Poker spielt? – Ein Full Howl.",
        "Was ist orange und läuft durch den Wald? – Eine Wanderine.",
        "Warum steht ein Pilz immer im Mittelpunkt? – Weil er ein Champignon ist."
    ]
    return random.choice(witze)

def plaudern(text, kontext):
    if not text.strip():
        return "Schreib doch etwas, damit wir reden können."
    text_lower = text.lower()
    kategorien = ["hobbys", "plaene", "gefuehle", "lieblingsdinge", "routine", "erinnerungen"]
    for kategorie in kategorien:
        for item in kontext[kategorie]:
            if item.lower() in text_lower and item not in kontext["gesprochen"]:
                kontext["gesprochen"].append(item)
                speichere_kontext(kontext)
                return f"Ah, du hast {item} erwähnt. Magst du mir mehr darüber erzählen?"
    followups = [
        "Interessant, erzähl mir mehr.",
        "Hm, wirklich? Wie fühlst du dich dabei?",
        "Das klingt spannend. Was denkst du darüber?",
        "Kannst du mir noch mehr dazu erzählen?",
        "Aha, ich verstehe. Willst du noch etwas dazu sagen?",
        "Wie würdest du das beschreiben, wenn dich jemand fragt?",
        "Was würdest du als nächstes tun?",
        "Hast du das schon öfter gemacht?"
    ]
    return random.choice(followups)

def neues_thema(kontext):
    optionen = []
    for kategorie in ["hobbys", "plaene", "gefuehle", "lieblingsdinge", "routine", "erinnerungen"]:
        if kontext[kategorie] and kategorie not in kontext["gesprochen"]:
            optionen.append(kategorie)
    optionen.extend(["Witz", "Motivation"])
    return random.choice(optionen) if optionen else None

def chat_loop(name, kontext):
    while True:
        print()
        type_print(CYAN + "Schreib mir etwas, ich antworte oder wir wechseln das Thema!" + RESET)
        text = input("> ").strip()
        if text.lower() in ["ende", "exit", "quit"]:
            break
        stimmung = stimmung_analyse(text)
        if stimmung == "schlecht":
            type_print(GREEN + motivierende_sprueche() + RESET)
        type_print(GREEN + plaudern(text, kontext) + RESET)
        thema = neues_thema(kontext)
        if thema:
            if thema == "Witz":
                type_print(GREEN + witz_des_tages() + RESET)
            elif thema == "Motivation":
                type_print(GREEN + motivierende_sprueche() + RESET)

# --- Modern Video Player ---
class ModernVideoPlayer:
    def __init__(self, root, video_path):
        self.root = root
        self.cap = cv2.VideoCapture(video_path)
        if not self.cap or not self.cap.isOpened():
            raise FileNotFoundError(f"Video konnte nicht geöffnet werden: {video_path}")
        self.playing = False
        self.total_frames = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
        self.fps = self.cap.get(cv2.CAP_PROP_FPS) or 30
        self.total_seconds = int(self.total_frames / self.fps)
        self.current_frame = 0
        self.bg_color = "#1e1e1e"
        self.fg_color = "#ffffff"
        self.accent_color = "#4a90e2"
        root.configure(bg=self.bg_color)
        root.title("🎬 Modern Video Player")
        self.video_frame = tk.Frame(root, bg=self.bg_color, bd=2, relief=tk.RIDGE)
        self.video_frame.pack(padx=20, pady=20)
        self.label = tk.Label(self.video_frame, bg=self.bg_color)
        self.label.pack()
        control_frame = tk.Frame(root, bg=self.bg_color)
        control_frame.pack(pady=10)
        self.play_button = tk.Button(control_frame, text="▶", command=self.play, bg=self.accent_color, fg=self.fg_color, width=4)
        self.play_button.pack(side=tk.LEFT, padx=8)
        self.pause_button = tk.Button(control_frame, text="⏸", command=self.pause, bg=self.accent_color, fg=self.fg_color, width=4)
        self.pause_button.pack(side=tk.LEFT, padx=8)
        self.stop_button = tk.Button(control_frame, text="⏹", command=self.stop, bg=self.accent_color, fg=self.fg_color, width=4)
        self.stop_button.pack(side=tk.LEFT, padx=8)
        self.slider = ttk.Scale(root, from_=0, to=max(0, self.total_frames-1), orient=tk.HORIZONTAL, length=500)
        self.slider.pack(pady=10)
        self.slider.bind("<ButtonRelease-1>", self.on_slider_release)
        self.time_label = tk.Label(root, text="00:00 / 00:00", bg=self.bg_color, fg=self.fg_color, font=("Arial", 12))
        self.time_label.pack()
        self.update_frame()

    def play(self):
        self.playing = True
        self.play_video()

    def pause(self):
        self.playing = False

    def stop(self):
        self.playing = False
        self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        self.slider.set(0)
        self.update_time_label(0)
        self.update_frame()

    def on_slider_release(self, event):
        frame_num = int(self.slider.get())
        self.cap.set(cv2.CAP_PROP_POS_FRAMES, frame_num)
        self.update_time_label(frame_num / self.fps)
        self.update_frame()

    def update_frame(self):
        if self.cap.isOpened():
            ret, frame = self.cap.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame = cv2.resize(frame, (640, 360))
                image = ImageTk.PhotoImage(Image.fromarray(frame))
                self.label.configure(image=image)
                self.label.image = image
                self.current_frame = int(self.cap.get(cv2.CAP_PROP_POS_FRAMES))
                self.slider.set(self.current_frame)
                self.update_time_label(self.current_frame / self.fps)
        if self.playing:
            self.root.after(int(1000/self.fps), self.play_video)

    def play_video(self):
        if not self.playing:
            return
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.resize(frame, (640, 360))
            image = ImageTk.PhotoImage(Image.fromarray(frame))
            self.label.configure(image=image)
            self.label.image = image
            self.current_frame = int(self.cap.get(cv2.CAP_PROP_POS_FRAMES))
            self.slider.set(self.current_frame)
            self.update_time_label(self.current_frame / self.fps)
            self.root.after(int(1000/self.fps), self.play_video)
        else:
            self.stop()

    def update_time_label(self, current_sec):
        total_min, total_sec = divmod(self.total_seconds, 60)
        curr_min, curr_sec = divmod(int(current_sec), 60)
        self.time_label.config(text=f"{curr_min:02}:{curr_sec:02} / {total_min:02}:{total_sec:02}")

# --- Menü ---
def hauptmenue():
    while True:
        print(BOLD + CYAN + "\n==== Hauptmenü ====" + RESET)
        print("1. Google öffnen")
        print("2. Coding Giants öffnen")
        print("3. Text kopieren")
        print("4. Witz des Tages")
        print("5. Würfelvolumen berechnen")
        print("6. Durchschnittsgeschwindigkeit")
        print("7. Taschenrechner")
        print("8. Prozentsatz")
        print("9. KI-Chat")
        print("10. Video-Player")
        print("0. Beenden")

        wahl = input("Auswahl: ").strip()
        if wahl == "1": open_google()
        elif wahl == "2": open_codinggiants()
        elif wahl == "3": kopieren()
        elif wahl == "4": witz()
        elif wahl == "5": volumen_wuerfel()
        elif wahl == "6": durchschnittsgeschwindigkeit()
        elif wahl == "7": taschenrechner()
        elif wahl == "8": prozentsatz()
        elif wahl == "9":
            kontext = lade_kontext()
            name = begruessung(kontext)
            chat_loop(name, kontext)
        elif wahl == "10":
            pfad = input("Pfad zum Video: ").strip()
            if os.path.exists(pfad):
                root = tk.Tk()
                ModernVideoPlayer(root, pfad)
                root.mainloop()
            else:
                type_print_natural(RED + "Datei nicht gefunden!" + RESET)
        elif wahl == "0":
            shutdown()
        else:
            type_print_natural(RED + "Ungültige Auswahl!" + RESET)

# --- MAIN ---
def main():
    start_logo()
    if login():
        hauptmenue()

if __name__ == "__main__":
    main()