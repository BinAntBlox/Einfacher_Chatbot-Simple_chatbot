import time
import random
import sys
import os
import json

# --- Farben ---
RESET = "\033[0m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RED = "\033[91m"
BOLD = "\033[1m"

KONTEXT_DATEI = "ki_kontext.json"

# --- Hilfsfunktionen ---
def type_print(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def frage_ja_nein(prompt):
    while True:
        antwort = input(YELLOW + prompt + RESET).strip().lower()
        if antwort in ["j", "n"]:
            return antwort == "j"
        type_print(RED + "Bitte 'j' für ja oder 'n' für nein eingeben." + RESET)

# --- Witze & Sprüche ---
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

# --- Kontext speichern/laden ---
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

# --- Begrüßung ---
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

# --- Stimmung erkennen & reagieren ---
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

def reagiere_auf_stimmung(text, stimmung):
    if stimmung == "gut":
        return "Aha." if not text.strip() else f"Oh, {text}? Schön zu hören."
    elif stimmung in ["schlecht", "neutral"]:
        return "Ist okay." if not text.strip() else f"Verstehe... {text}."
    else:
        return "Danke fürs Teilen."

# --- Plaudern ---
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

# --- Neues Thema vorschlagen ---
def neues_thema(kontext):
    optionen = []
    for kategorie in ["hobbys", "plaene", "gefuehle", "lieblingsdinge", "routine", "erinnerungen"]:
        if kontext[kategorie] and kategorie not in kontext["gesprochen"]:
            optionen.append(kategorie)
    optionen.extend(["Witz", "Motivation"])
    return random.choice(optionen) if optionen else None

# --- Chat Loop ---
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
            if thema == "hobbys":
                type_print(YELLOW + "Erzähl mir von einem deiner Hobbys." + RESET)
                hobby = input("> ").strip()
                if hobby:
                    kontext["hobbys"].append(hobby)
                    kontext["gesprochen"].append("hobbys")
                    speichere_kontext(kontext)
            elif thema == "plaene":
                type_print(YELLOW + "Was sind deine aktuellen Pläne oder Ziele?" + RESET)
                plan = input("> ").strip()
                if plan:
                    kontext["plaene"].append(plan)
                    kontext["gesprochen"].append("plaene")
                    speichere_kontext(kontext)
            elif thema == "gefuehle":
                type_print(YELLOW + "Wie fühlst du dich gerade?" + RESET)
                gefuehl = input("> ").strip()
                if gefuehl:
                    kontext["gefuehle"].append(gefuehl)
                    kontext["gesprochen"].append("gefuehle")
                    speichere_kontext(kontext)
            elif thema == "lieblingsdinge":
                type_print(YELLOW + "Was sind deine Lieblingsdinge?" + RESET)
                lieblings = input("> ").strip()
                if lieblings:
                    kontext["lieblingsdinge"].append(lieblings)
                    kontext["gesprochen"].append("lieblingsdinge")
                    speichere_kontext(kontext)
            elif thema == "routine":
                type_print(YELLOW + "Erzähl mir von deiner täglichen Routine." + RESET)
                routine = input("> ").strip()
                if routine:
                    kontext["routine"].append(routine)
                    kontext["gesprochen"].append("routine")
                    speichere_kontext(kontext)
            elif thema == "erinnerungen":
                type_print(YELLOW + "Welche Erinnerungen möchtest du teilen?" + RESET)
                erinnerung = input("> ").strip()
                if erinnerung:
                    kontext["erinnerungen"].append(erinnerung)
                    kontext["gesprochen"].append("erinnerungen")
                    speichere_kontext(kontext)
            elif thema == "Witz":
                type_print(GREEN + witz_des_tages() + RESET)
            elif thema == "Motivation":
                type_print(GREEN + motivierende_sprueche() + RESET)

# --- Hauptprogramm ---
def main():
    clear()
    kontext = lade_kontext()
    name = begruessung(kontext)

    type_print(YELLOW + "Wie fühlst du dich heute?" + RESET)
    gefuehl = input("> ").strip()
    stimmung = stimmung_analyse(gefuehl)
    kontext["gefuehle"].append(gefuehl if gefuehl else "unbekannt")
    speichere_kontext(kontext)

    type_print(GREEN + reagiere_auf_stimmung(gefuehl, stimmung) + RESET)
    if stimmung == "schlecht":
        type_print(GREEN + motivierende_sprueche() + RESET)

    chat_loop(name, kontext)

    print()
    type_print(CYAN + f"Es war schön, mit dir zu reden, {name}." + RESET)
    if kontext["hobbys"]:
        type_print(GREEN + f"Ich erinnere mich an deine Hobbys: {', '.join(kontext['hobbys'])}." + RESET)
    if kontext["plaene"]:
        type_print(GREEN + f"Und deine Pläne: {', '.join(kontext['plaene'])}." + RESET)
    if kontext["lieblingsdinge"]:
        type_print(GREEN + f"Deine Lieblingsdinge sind: {', '.join(kontext['lieblingsdinge'])}." + RESET)
    type_print(GREEN + "Hab einen wunderbaren Tag!" + RESET)

if __name__ == "__main__":
    main()