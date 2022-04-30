from string import ascii_letters, ascii_uppercase, ascii_lowercase, digits, punctuation
from random import choice, shuffle

class RandomPasswordGenerator:
    def __init__(self, password_length):
        self.password_length = password_length

        if self.length_checker():
            self.password = self.generate()
        else:
            self.password = "Must be 4-16 symbols!"

    def generate(self):
        characters = [choice(ascii_lowercase), choice(ascii_uppercase), choice(digits), choice(punctuation)]
        
        for i in range(self.password_length - 4):
            characters.append(choice(ascii_letters + digits + punctuation))

        shuffle(characters)

        return "".join(characters)

    def length_checker(self):
        if self.password_length < 4 or self.password_length > 16:
            return False
        return True

    def __str__(self):
        return f"{self.password}"

