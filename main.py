# STEP 1: Read image

file = open("input.jpg", "rb")
image_bytes = file.read()
file.close()


# STEP 2: Convert bytes to binary

binary_data = ""

for byte in image_bytes:
    binary_byte = format(byte, '08b')
    binary_data += binary_byte


# STEP 3: Split into 64-bit blocks

blocks = []

for i in range(0, len(binary_data), 64):
    block = binary_data[i:i+64]

    if len(block) < 64:
        block = block.ljust(64, '0')

    blocks.append(block)


# STEP 4/5 imports

from des import (
    permute,
    shift_left,
    xor,
    sbox_substitution,
    generate_round_keys,
    des_round,
    encrypt_block
)
from tables import IP,PC1,PC2,E,P,FP


# STEP 6: Apply Initial Permutation

first_block = blocks[0]

permuted_block = permute(first_block, IP)

print("\nOriginal Block:")
print(first_block)

print("\nAfter Initial Permutation:")
print(permuted_block)

print("\nLength:")
print(len(permuted_block))

# STEP 7: Split into Left and Right halves

left = permuted_block[:32]
right = permuted_block[32:]

print("\nLeft Half (L0):")
print(left)

print("\nLength of Left:")
print(len(left))

print("\nRight Half (R0):")
print(right)

print("\nLength of Right:")
print(len(right))

# STEP 8: Create 64-bit DES key

key = "1010101010111011000010010001100000100111001101101100110011011101"

print("\nDES Key:")
print(key)

print("\nKey Length:")
print(len(key))

# STEP 10: Apply PC-1 permutation on key

permuted_key = permute(key, PC1)

print("\nPermuted Key After PC-1:")
print(permuted_key)

print("\nLength of Permuted Key:")
print(len(permuted_key))

# STEP 11: Split key into two halves

C0 = permuted_key[:28]
D0 = permuted_key[28:]

print("\nC0:")
print(C0)

print("\nLength of C0:")
print(len(C0))

print("\nD0:")
print(D0)

print("\nLength of D0:")
print(len(D0))

# STEP 13: Perform left shifts

C1 = shift_left(C0, 1)
D1 = shift_left(D0, 1)

print("\nC1 After Shift:")
print(C1)

print("\nD1 After Shift:")
print(D1)

# STEP 15: Generate Round Key K1

combined_key = C1 + D1

K1 = permute(combined_key, PC2)

print("\nRound Key K1:")
print(K1)

print("\nLength of K1:")
print(len(K1))

# STEP 18: Expand Right Half

expanded_R0 = permute(right, E)

print("\nExpanded R0:")
print(expanded_R0)

print("\nLength of Expanded R0:")
print(len(expanded_R0))


# STEP 20: XOR with Round Key

xor_result = xor(expanded_R0, K1)

print("\nXOR Result:")
print(xor_result)

print("\nLength of XOR Result:")
print(len(xor_result))

# STEP 25: S-Box Test

first_6_bits = xor_result[:6]

print("\nFirst 6 Bits:")
print(first_6_bits)

# STEP 28: Full S-Box Substitution

sbox_output = sbox_substitution(xor_result)

print("\nS-Box Output:")
print(sbox_output)

print("\nLength:")
print(len(sbox_output))

# STEP 30: Apply P Permutation

p_output = permute(sbox_output, P)

print("\nP Permutation Output:")
print(p_output)

print("\nLength:")
print(len(p_output))

# STEP 31: XOR with Left Half

R1 = xor(left, p_output)

print("\nR1:")
print(R1)

print("\nLength of R1:")
print(len(R1))

# STEP 32: Generate L1

L1 = right

print("\nL1:")
print(L1)

print("\nLength of L1:")
print(len(L1))

# STEP 36: Generate All Round Keys

round_keys = generate_round_keys(key)

print("\nTotal Round Keys:")
print(len(round_keys))

print("\nFirst Round Key:")
print(round_keys[0])

print("\nLast Round Key:")
print(round_keys[15])

# STEP 38: Perform 16 DES Rounds

left = permuted_block[:32]
right = permuted_block[32:]

for i in range(16):

    left, right = des_round(left, right, round_keys[i])

    print(f"\nRound {i+1}")
    print("L:", left)
    print("R:", right)

# STEP 41: Final Swap

combined_block = right + left

print("\nCombined Block:")
print(combined_block)

print("\nLength:")
print(len(combined_block))


# STEP 42: Final Permutation

ciphertext = permute(combined_block, FP)

print("\nCiphertext:")
print(ciphertext)

print("\nCiphertext Length:")
print(len(ciphertext))

# STEP 44: Encrypt All Blocks

encrypted_blocks = []

for block in blocks:

    encrypted_block = encrypt_block(block, round_keys)

    encrypted_blocks.append(encrypted_block)

print("\nAll blocks encrypted successfully!")

# STEP 45: Combine encrypted blocks

encrypted_data = ""

for block in encrypted_blocks:

    encrypted_data += block

print("\nEncrypted data combined!")

# STEP 46: Convert binary to bytes

encrypted_bytes = bytearray()

for i in range(0, len(encrypted_data), 8):

    byte = encrypted_data[i:i+8]

    encrypted_bytes.append(int(byte, 2))

print("\nBinary converted to bytes!")

# STEP 47: Save encrypted file

encrypted_file = open("encrypted.des", "wb")

encrypted_file.write(encrypted_bytes)

encrypted_file.close()

print("\nEncrypted file saved successfully!")
