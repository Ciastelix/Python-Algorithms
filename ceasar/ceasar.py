from string import ascii_lowercase as alphabet

alphabet = [letter for letter in alphabet]


class Ceasar:
    @staticmethod
    def encrypt(text: int, key: int) -> str:
        encrypted_text = ""
        text = text.lower()
        for letter in text:
            if letter in alphabet:
                encrypted_text += alphabet[
                    (alphabet.index(letter) + key) % len(alphabet)
                ]
            else:
                encrypted_text += letter
        return encrypted_text

    @staticmethod
    def decrypt(text: str, key: int) -> str:
        text = text.lower()
        return Ceasar.encrypt(text, -key)

    @staticmethod
    def brute_force(text: str) -> None:
        text = text.lower()
        for key in range(len(alphabet)):
            print(f"Key: {key} - {Ceasar.decrypt(text, key)}")
