from des import (
    generate_round_keys,
    encrypt_block
)

# =========================
# STEP 1: READ IMAGE FILE
# =========================

file = open("input.jpg", "rb")

image_bytes = file.read()

file.close()

print("Image loaded successfully!")

# Store original image size
original_size = len(image_bytes)

print("Original File Size:", original_size, "bytes")


# =========================
# STEP 2: CONVERT IMAGE TO BINARY
# =========================

binary_data = ""

for byte in image_bytes:

    binary_data += format(byte, '08b')

print("Binary conversion completed!")


# =========================
# STEP 3: SPLIT INTO 64-BIT BLOCKS
# =========================

blocks = []

for i in range(0, len(binary_data), 64):

    block = binary_data[i:i+64]

    # Padding if block smaller than 64 bits
    if len(block) < 64:

        block = block.ljust(64, '0')

    blocks.append(block)

print("Total blocks:", len(blocks))


# =========================
# STEP 4: CREATE DES KEY
# =========================

key = "1010101010111011000010010001100000100111001101101100110011011101"

print("DES Key Loaded!")


# =========================
# STEP 5: GENERATE ROUND KEYS
# =========================

round_keys = generate_round_keys(key)

print("16 Round Keys Generated!")


# =========================
# STEP 6: ENCRYPT ALL BLOCKS
# =========================

encrypted_blocks = []

for block in blocks:

    encrypted_block = encrypt_block(block, round_keys)

    encrypted_blocks.append(encrypted_block)

print("All blocks encrypted successfully!")


# =========================
# STEP 7: COMBINE ENCRYPTED BLOCKS
# =========================

encrypted_data = ""

for block in encrypted_blocks:

    encrypted_data += block

print("Encrypted data combined!")


# =========================
# STEP 8: CONVERT BINARY TO BYTES
# =========================

encrypted_bytes = bytearray()

for i in range(0, len(encrypted_data), 8):

    byte = encrypted_data[i:i+8]

    encrypted_bytes.append(int(byte, 2))

print("Binary converted to bytes!")


# =========================
# STEP 9: SAVE ENCRYPTED FILE
# =========================

encrypted_file = open("encrypted.des", "wb")

# Save original image size first (8 bytes)
encrypted_file.write(original_size.to_bytes(8, 'big'))

# Save encrypted data
encrypted_file.write(encrypted_bytes)

encrypted_file.close()

print("\nEncrypted file saved successfully!")

print("\nOutput File Generated:")
print("encrypted.des")