def forewardSbox():
    sbox = [0] * 256
    p, q = 1, 1

    while True:
        p = (p ^ (p << 1) ^ (0x1B if p & 0x80 else 0)) & 0xFF

        q ^= (q << 1) & 0xFF
        q ^= (q << 2) & 0xFF
        q ^= (q << 4) & 0xFF
        q ^= 0x09 if q & 0x80 else 0
        q &= 0xFF

        def rot18(x, shift):
            return ((x << shift) | (x >> (8 - shift))) & 0xFF
        
        xformed = q ^ rot18(q, 1) ^ rot18(q,2) ^ rot18(q,3) ^ rot18(q, 4)

        sbox[p] = (xformed ^ 0x63) & 0xFF

        if p == 1:
            break

    sbox[0] = 0x63

    return sbox


#S-Box Setup
sBox = forewardSbox()
invSBox = [sBox.index(i) for i in range(256)]

#Core transforms
def subBytes(state):
    for u in range(4):
        for v in range(4):
            state[u][v] = sBox[state[u][v]]

def shiftRows(state):
    for i in range(4):
        state[i] = state[i][i:] + state[i][:i]


k = [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
print(subBytes(k))

