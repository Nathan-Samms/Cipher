from collections import Counter

import numpy as np
from classicCiphers import classicalCipher


class analyze():
    def __init__(self):
        self.alpha = classicalCipher().alpha
        self.ENGLISH_FREQ = np.array([0.0817, 0.0150, 0.0278, 0.0425, 0.1270, 0.0223, 0.0202, 0.0609,
                                      0.0697, 0.0015, 0.0077, 0.0403, 0.0241, 0.0675, 0.0751, 0.0193,
                                      0.0010, 0.0599, 0.0633, 0.0906, 0.0276, 0.0098, 0.0236, 0.0015,
                                      0.0197, 0.0007, 0.0817, 0.0150, 0.0278, 0.0425, 0.1270, 0.0223, 0.0202, 0.0609,
                                      0.0697, 0.0015, 0.0077, 0.0403, 0.0241, 0.0675, 0.0751, 0.0193,
                                      0.0010, 0.0599, 0.0633, 0.0906, 0.0276, 0.0098, 0.0236, 0.0015,
                                      0.0197, 0.0007, 0.1300])
    
    def returnAlpha(self):
        return self.ENGLISH_FREQ
    
    def scoreText(self, txt:str) -> np.ndarray:
        dec_alpha = [letter for letter in self.alpha]
        adj_letters = [letter for letter in txt]
        n = len(dec_alpha)

        total = len(adj_letters)
        counts = Counter(adj_letters)
        observed = np.array([counts.get(ch,0) for ch in dec_alpha]) / total

        allShifts = np.stack([np.roll(observed, shift) for shift in range(n)])

        scores = np.sum((allShifts - self.ENGLISH_FREQ) **2 / self.ENGLISH_FREQ, axis=1)

        return scores

    def breakCaesar(self,txt, top_n:int = 3):
        scores = self.scoreText(txt)
        bestShifts = np.argsort(scores)

        print(f'Top {top_n} Scores')
        for shift in bestShifts[:top_n:]:
            shift = int(shift)
            print(f'Shift: {shift:.2f} | Score: {scores[shift]:.4f}')

print(analyze().breakCaesar('mBytWBCtMKOuLytNyMNtIztCHxyJyHxyHwytwBywEMtQByNByLtNQItPuLCuvFyMtuLytFCEyFStNItvytLyFuNyxtILtHINtpytBuPytwIOHNMtzILtNQItwuNyAILCwuFtILtHIGCHuFtPuLCuvFyMtpytuFMItBuPytuHtCxyutNBuNtNBytNQItPuLCuvFyMtuLytHINtLyFuNyxtmBytNyMNtACPyMtOMtutQuStNItxywCxytCztIOLtCxyutCMtJFuOMCvFytILtHIN'))