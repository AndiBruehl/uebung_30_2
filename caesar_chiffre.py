print()
print("Caesar Chiffre")
print("==============")
print()


def caesar_cipher(message, key, operation):
    
    if operation == "encrypt":
        result = ""
        for letter in message:
            if letter.isalpha():
                shift = (ord(letter.lower()) - 97 + key) % 26
                result += chr(shift + 97).upper() if letter.isupper() else chr(shift + 97)
            else:
                result += letter
    elif operation == "decrypt":
        result = ""
        for letter in message:
            if letter.isalpha():
                shift = (ord(letter.lower()) - 97 - key) % 26
                result += chr(shift + 97).upper() if letter.isupper() else chr(shift + 97)
            else:
                result += letter
    else:
        result = "Unbekannte Option"
    return result

# Frage nach User-Input
filename = input("Dateinamen eingeben: ")
operation = input("Option angeben (encrypt/decrypt): ")
key = int(input("Verschlüsselungskey: "))

# Lesen der Quelldatei
with open(filename, "r") as file:
    message = file.read()

# Ver- oder entschlüsseln der Quelldatei
result = caesar_cipher(message, key, operation)

# Ergebnis auf dem Terminal ausgeben
print(result)

# ERgebnis in neuer Datei speichern
new_filename = input("Gib den neuen Dateinamen an: ")
with open(new_filename, "w") as new_file:
    new_file.write(result)

print()
print("Programmende")
print()