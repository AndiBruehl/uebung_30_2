import random

print()
print("Hangman")
print("=======")
print()

# Liste mit Wörtern für das Spiel
words = ["python", "programmierung", "computer", "hangman", "spiel"]

# Zufälliges Wort auswählen
word = random.choice(words)

# Anzahl der Versuche
attempts = 20

# Bisher erratene Buchstaben (initial leer)
guessed_letters = []

# Bisher korrekt geratene Buchstaben (initial nur Unterstriche)
correct_letters = ["_"] * len(word)

# Haupt-Schleife des Spiels
while attempts > 0 and "_" in correct_letters:
    # Aktuellen Stand ausgeben
    print(" ".join(correct_letters))

    # Buchstaben-Eingabe des Spielers
    print()
    letter = input("Rate einen Buchstaben: ").lower()

    # Überprüfen, ob der Buchstabe im Wort vorkommt
    if letter in guessed_letters:
        print()
        print("Du hast diesen Buchstaben bereits geraten!")
    elif letter in word:
        print()
        print("Richtig geraten!")
        guessed_letters.append(letter)
        # Alle Vorkommen des Buchstabens im Wort eintragen
        for i in range(len(word)):
            if word[i] == letter:
                correct_letters[i] = letter
    else:
        print()
        print("Falsch geraten!")
        guessed_letters.append(letter)
        attempts -= 1

# Spiel ist beendet, Ausgabe des Ergebnisses
if "_" not in correct_letters:
    print()
    print("Du hast das Wort erraten: " + word)
else:
    print()
    print("Leider hast du das Wort nicht erraten. Es war: " + word)

print()
print("Spielende")
print()
input("Zum beenden beliebige Taste drücken.")