class CaesarCipher(object):
    def __init__(self, shift):
        self.shift = shift

    def encode(self, str):
        array = []
        for letter in str:
            if not (97 <= ord(letter) <= 122 or 65 <= ord(letter) <= 90):
                array.append(letter)
            else:
                if 97 <= ord(letter) <= 122:
                    new_letter = ord(letter) + self.shift
                    if new_letter > 122:
                        new_letter = 96 + (new_letter - 122)
                    array.append(chr(new_letter))
                else:
                    new_letter = ord(letter) + self.shift
                    if new_letter > 90:
                        new_letter = 64 + (new_letter - 90)
                    array.append(chr(new_letter))
        return ''.join(array)


obj = CaesarCipher(5)

print(obj.encode("Codewars"))
