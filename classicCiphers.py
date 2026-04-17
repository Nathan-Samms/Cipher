import string


class classicalCipher():
    DEFAULTALPHA = {char: i for i, char in enumerate(string.printable)}

    def __init__(self, alpha:dict):
        if alpha is None:
            alpha = self.DEFAULTALPHA
        if not isinstance(alpha,dict):
            raise TypeError("Alphabet must be a dict mapping characters to int")
        if len(alpha) < 2:
            raise ValueError("Alphabet must contain at least two characters")
        if len(set(alpha.values())) != len(alphabet):
            raise ValueError("Alphabet values must be unique (no duplicate values)")

        self.alpha = alpha
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
    alphabet = {char: i for i, char in enumerate(string.printable)}
    testString = "This is a test of cipher functionality."
    encoder = classicalCipher(alphabet)

    print('--------------------TEST CASES--------------------\n')
    #Caesar cipher
    
    print('\033[1mCaesar Cipher\033[0m')
    caesarEnc= encoder.caesar_enc(testString, 10)
    caesarDec = encoder.caesar_dec(caesarEnc, 10)
    print(f'Encoded:\n\t{caesarEnc}\nDecoded:\n\t{caesarDec}')

