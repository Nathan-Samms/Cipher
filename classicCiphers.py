import string


class classicalCipher():
    def __init__(self):
        #self.alpha = {char: i for i, char in enumerate(string.ascii_lowercase + string.ascii_uppercase + ' ')}
        self.alpha = {char: i for i, char in enumerate(string.printable)}
        self.reversed_alpha = {v:k for k,v in self.alpha.items()}
        self.size = len(self.alpha)

    def _validate(self, text:str, allow_spaces:bool = True): #Toggle allow_spaces if included
        for char in text:
            if char not in self.alpha and not (allow_spaces and char == ' '):
                raise ValueError(f'Unsupported Character in "{text}": {char}')
            
    def vig_enc(self, plainText:str, key:str) -> str:
        cipher = []
        self._validate(key)
        self._validate(plainText)

        for index, letter in enumerate(plainText):
            messageChar = self.alpha[letter]
            keyChar = self.alpha[key[index % len(key)]]

            cipher.append((messageChar + keyChar) % self.size)
        
        return ''.join([self.reversed_alpha[num] for num in cipher])

    def vig_dec(self, cipherText:str, key:str) -> str:
        plain = []
        self._validate(key)
        self._validate(cipherText)

        for index, letter in enumerate(cipherText):
            cipherChar = self.alpha[letter]
            keyChar = self.alpha[key[index % len(key)]]

            plain.append((cipherChar - keyChar) % self.size)

        return ''.join([self.reversed_alpha[num] for num in plain])

    def caesar_enc(self, plainText:str, shift:int) -> str:
        cipher = []
        self._validate(plainText)

        for letter in plainText:
            shifted_letter = (self.alpha[letter] + shift) % self.size
            cipher.append(shifted_letter)
        
        return ''.join([self.reversed_alpha[num] for num in cipher])
    
    def caesar_dec(self, cipherText:str, shift:int) -> str:
        plainText = []
        self._validate(cipherText)

        for letter in cipherText:
            shifted_letter = (self.alpha[letter] - shift) % self.size
            plainText.append(shifted_letter)
        
        return ''.join([self.reversed_alpha[num] for num in plainText])
    
    def rot13_enc(self, plainText:str) -> str:
        self._validate(plainText)

        return self.caesar_enc(plainText, shift=13) #Explicit shift of 13
    
    def rot13_dec(self, cipherText:str) -> str:
        self._validate(cipherText)

        return self.caesar_dec(cipherText, shift=13) #Explicit shift of 13

    def atbash_enc(self, plainText:str) -> str:
        cipherText = []
        self._validate(plainText)

        for letter in plainText:
            enc_letter = self.size - 1 - self.alpha[letter]
            cipherText.append(enc_letter)

        return ''.join([self.reversed_alpha[num] for num in cipherText])
    
    #Redundant for API
    
    def atbash_dec(self, cipherText): 
        return self.atbash_enc(cipherText)
    

if __name__ == "__main__":

    #----------UNIT TESTS----------
    cenc = ''.join(classicalCipher().caesar_enc("The Chi square test of independence checks whether two variables are likely to be related or not We have counts for two categorical or nominal variables We also have an idea that the two variables are not related The test gives us a way to decide if our idea is plausible or not", 20))
    cdec = ''.join(classicalCipher().caesar_dec(cenc, 20))
    print(cenc)
    print(cdec)


    enc = classicalCipher().vig_enc("This is a test of the vigenere cipher", "Test")
    print(enc)
    dec = classicalCipher().vig_dec(enc, "Test")
    print(dec)

    enc = classicalCipher().rot13_enc("This is a test of the vigenere cipher")
    print(''.join(enc))
    dec = classicalCipher().rot13_dec(''.join(enc))
    print(''.join(dec))

    enc = classicalCipher().atbash_enc("test")
    print(''.join(enc))
    dec = classicalCipher().atbash_enc(''.join(enc))
    print(''.join(dec))