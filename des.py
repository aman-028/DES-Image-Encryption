from tables import IP

def permute(block, table):
    permuted = ""

    for position in table:
        permuted += block[position - 1]

    return permuted

def shift_left(block, shifts):
    return block[shifts:] + block[:shifts]


def xor(a, b):
    result = ""

    for i in range(len(a)):
        if a[i] == b[i]:
            result += "0"
        else:
            result += "1"

    return result

from tables import S_BOXES

def sbox_substitution(bits):

    output = ""

    # Split into 8 groups of 6 bits
    for i in range(8):

        block = bits[i*6:(i+1)*6]

        row = int(block[0] + block[5], 2)

        column = int(block[1:5], 2)

        value = S_BOXES[i][row][column]

        output += format(value, '04b')

    return output

from tables import PC1, PC2, SHIFT_SCHEDULE

def generate_round_keys(key):

    round_keys = []

    # Apply PC1
    permuted_key = permute(key, PC1)

    # Split into halves
    left = permuted_key[:28]
    right = permuted_key[28:]

    # Generate 16 keys
    for shift in SHIFT_SCHEDULE:

        left = shift_left(left, shift)
        right = shift_left(right, shift)

        combined = left + right

        round_key = permute(combined, PC2)

        round_keys.append(round_key)

    return round_keys

from tables import E, P

def des_round(left, right, round_key):

    # Expansion
    expanded = permute(right, E)

    # XOR with round key
    xored = xor(expanded, round_key)

    # S-box substitution
    sbox_output = sbox_substitution(xored)

    # P permutation
    p_output = permute(sbox_output, P)

    # Generate new right
    new_right = xor(left, p_output)

    # New left becomes old right
    new_left = right

    return new_left, new_right

from tables import IP, FP

def encrypt_block(block, round_keys):

    # Initial Permutation
    block = permute(block, IP)

    # Split into halves
    left = block[:32]
    right = block[32:]

    # 16 rounds
    for i in range(16):
        left, right = des_round(left, right, round_keys[i])

    # Final swap
    combined = right + left

    # Final Permutation
    ciphertext = permute(combined, FP)

    return ciphertext