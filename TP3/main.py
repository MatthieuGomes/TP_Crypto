ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ALPHABET_SIZE = 26
REF_IC= 0.0778

TEXT = "JRDMCQLEGASNAHSHJEVWAVGJSUDWPNUPELWGUAJFZWQRFXVWMWNNIZZWYFKMCMLIKWVCQUIQWGRGHXBYVAXZMRXILQUMGSXIWFWRFGOZWYAWJOQKTBMVVWLVRLVADSMYJIMIJUHSFLMNSHKEVMRJNAXPZWYIWHEXWVFWZEZSRPWITLWPBYMQCWTBMVDMUSQWVCMEIFKEGMKIPJITJJEIGTOCJZBLVELWXRJQIVSXVGRLIUVLHXOOJECZMEMKXHFERBSRPAINYMMEWQOVLINDENBAUHAXENWPVUMTILMBFWVWMWZSMTZAWRRQAQFXRFENBDIFTESMKHHULINXVREINBVIIAKEVWVRUISGKXREIAMLIVFZEVLINMWEQRMREISQWGYWFRINSCGYRINSVJTEZUIPWQYALIEWPAKJCCLENIDCFWHEUSRQWHETSTNLMEVUISWPIKAXNLMOVKZBMWADWDYWWCWETRLINKWWAWGEAKEVJISXGYEUSNBARHWVDIFWPWXTMNSVWFRINSRFGOZW"

FR_FREQ = dict(
    E=15.87/100,
    N=7.15/100,
    D=3.39/100,
    Q=1.06/100,
    H=0.77/100,
    A=9.42/100,
    R=6.46/100,
    M=3.24/100,
    G=1.04/100,
    Z=0.32/100,
    I=8.41/100,
    U=6.24/100,
    P=2.86/100,
    B=1.02/100,
    X=0.30/100,
    S=7.90/100,
    L=5.34/100,
    C=2.64/100,
    F=0.95/100,
    Y=0.24/100,
    T=7.26/100,
    O=5.14/100,
    V=2.15/100,
    J=0.89/100,
    K=0.00/100,
    W=0.00/100
)


def get_text_IC(text):
    text_length = len(text)
    occ = dict()
    for char in text:
        if char not in occ.keys():
            occ[char] = 1
        else:
            occ[char] += 1
    ic = 0.0
    for letter in ALPHABET:
        if letter in occ.keys():
            ic = ic +  (occ[letter] * (occ[letter] - 1))
    return ic/ (text_length * (text_length - 1))

def slice_text(text, start, key_size):
    sliced = ""
    for i in range(len(text)//key_size):
        if i*key_size + start < len(text):
            sliced += text[i*key_size + start]
    return sliced


        

def get_IC_for_key_size(text, key_size):
    ic_values = []
    if key_size == 1:
        return get_text_IC(text)
    for i in range(key_size-1):
        subtext = slice_text(text, i, key_size)
        ic = get_text_IC(subtext)
        ic_values.append(ic)
    return sum(ic_values) / len(ic_values)

def get_most_probable_language(text, max_keysize):
    best_ic = 0.0
    best_keysize = 0
    for key_size in range(2, max_keysize+1):
        ic = get_IC_for_key_size(text, key_size)
        if abs(ic - REF_IC) < abs(best_ic - REF_IC):
            best_ic = ic
            best_keysize = key_size
    return best_keysize

def get_letter_frequency(text):
    freq = dict()
    text_length = len(text)
    for letter in ALPHABET:
        freq[letter] = 0
    for char in text:
        if char in freq.keys():
            freq[char] += 1
    for letter in ALPHABET:
        freq[letter] = freq[letter] / text_length
    return freq

def get_difference_with_ref_freq(freq):
    diff = 0.0
    for letter in ALPHABET:
        diff += abs(freq[letter] - FR_FREQ[letter])
    return diff/ALPHABET_SIZE

def get_most_probable_shift(subtext):
    shift_index = 0
    for shift in range(ALPHABET_SIZE):
        shifted_text = ""
        for char in subtext:
            shifted_char = chr((ord(char) - ord('A') - shift) % ALPHABET_SIZE + ord('A'))
            shifted_text += shifted_char
        freq = get_letter_frequency(shifted_text)
        diff = get_difference_with_ref_freq(freq)
        if shift_index == 0 or diff < best_diff:
            best_diff = diff
            best_shift = shift
        shift_index += 1
    return best_shift

def get_decrypted_text(text, key):
    decrypted = ""
    key_length = len(key)
    for i in range(len(text)):
        key_char = key[i % key_length]
        shift = ord(key_char) - ord('A')
        decrypted_char = chr((ord(text[i]) - ord('A') - shift) % ALPHABET_SIZE + ord('A'))
        decrypted += decrypted_char
    return decrypted



if __name__ == "__main__":
    
    print("IC for text:", get_text_IC(TEXT))
    print("IC for key size 1:", get_IC_for_key_size(TEXT, 1))
    print("IC for key size 2:", get_IC_for_key_size(TEXT, 2))
    print("IC for key size 3:", get_IC_for_key_size(TEXT, 3))
    print("IC for key size 4:", get_IC_for_key_size(TEXT, 4))
    print("IC for key size 5:", get_IC_for_key_size(TEXT, 5))
    print("IC for key size 6:", get_IC_for_key_size(TEXT, 6))
    print("IC for key size 7:", get_IC_for_key_size(TEXT, 7))
    print("IC for key size 8:", get_IC_for_key_size(TEXT, 8))
    print("IC for key size 9:", get_IC_for_key_size(TEXT, 9))
    print("IC for key size 10:", get_IC_for_key_size(TEXT, 10))
    probable_keysize = get_most_probable_language(TEXT, 10)
    print("Most probable key size:", probable_keysize)
    freq = get_letter_frequency(TEXT)
    print("Letter frequencies in the text:")
    for letter in ALPHABET:
        print(f"{letter}: {freq[letter]:.4f}")
    probable_key = ""
    for i in range(probable_keysize):
        subtext = slice_text(TEXT, i, probable_keysize)
        mostprobable_shift = get_most_probable_shift(subtext)
        print(f"Letter frequencies for subtext {i+1}: {chr(mostprobable_shift + ord('A'))}")
        probable_key += chr(mostprobable_shift + ord('A'))
    print("Most probable key:", probable_key)
    decrypted_text = get_decrypted_text(TEXT, probable_key)
    print("Decrypted text:", decrypted_text)


# TP Crypto --- IGNORE ---
