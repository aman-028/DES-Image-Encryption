# Read original image

original_file = open("input.jpg", "rb")

original_data = original_file.read()

original_file.close()


# Read decrypted image

decrypted_file = open("decrypted.jpg", "rb")

decrypted_data = decrypted_file.read()

decrypted_file.close()


# Compare both files

if original_data == decrypted_data:

    print("SUCCESS!")
    print("Decryption is correct.")
    print("Original and decrypted images are identical.")

else:

    print("ERROR!")
    print("Images are different.")