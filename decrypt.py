from des import generate_round_keys, encrypt_block


# =========================
# STEP 1: READ ENCRYPTED FILE
# =========================

file = open("encrypted.des", "rb")

# Read original file size (first 8 bytes)
original_size_bytes = file.read(8)

original_size = int.from_bytes(original_size_bytes, 'big')

# Read remaining encrypted data
encrypted_bytes = file.read()

file.close()

print("Encrypted file loaded successfully!")

print("Original File Size:", original_size, "bytes")


# =========================
# STEP 2: CONVERT ENCRYPTED BYTES TO BINARY
# =========================

binary_data = ""

for byte in encrypted_bytes:

    binary_data += format(byte, '08b')

print("Binary conversion completed!")


# =========================
# STEP 3: SPLIT INTO 64-BIT BLOCKS
# =========================

blocks = []

for i in range(0, len(binary_data), 64):

    block = binary_data[i:i+64]

    # Ensure full 64-bit block
    if len(block) == 64:

        blocks.append(block)

print("Total encrypted blocks:", len(blocks))


# =========================
# STEP 4: CREATE SAME DES KEY
# =========================

key = "1010101010111011000010010001100000100111001101101100110011011101"

print("DES Key Loaded!")


# =========================
# STEP 5: GENERATE ROUND KEYS
# =========================

round_keys = generate_round_keys(key)

print("16 Round Keys Generated!")


# =========================
# STEP 6: REVERSE ROUND KEYS
# =========================

round_keys = round_keys[::-1]

print("Round Keys Reversed!")


# =========================
# STEP 7: DECRYPT ALL BLOCKS
# =========================

decrypted_blocks = []

for block in blocks:

    decrypted_block = encrypt_block(block, round_keys)

    decrypted_blocks.append(decrypted_block)

print("All blocks decrypted successfully!")


# =========================
# STEP 8: COMBINE DECRYPTED BLOCKS
# =========================

decrypted_data = ""

for block in decrypted_blocks:

    decrypted_data += block

print("Decrypted data combined!")


# =========================
# STEP 9: CONVERT BINARY TO BYTES
# =========================

decrypted_bytes = bytearray()

for i in range(0, len(decrypted_data), 8):

    byte = decrypted_data[i:i+8]

    decrypted_bytes.append(int(byte, 2))

print("Binary converted to bytes!")


# =========================
# STEP 10: REMOVE EXTRA PADDING
# =========================

decrypted_bytes = decrypted_bytes[:original_size]

print("Padding removed!")


# =========================
# STEP 11: SAVE DECRYPTED IMAGE
# =========================

output_file = open("decrypted.jpg", "wb")

output_file.write(decrypted_bytes)

output_file.close()

print("\nDecrypted image saved successfully!")

print("\nOutput File Generated:")
print("decrypted.jpg")