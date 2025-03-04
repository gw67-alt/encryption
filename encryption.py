import random

# Seed the random number generator for reproducibility
random.seed(42)

# Encryption function
def encrypt(text, key):
    """Encrypt the text by scrambling its characters based on a permutation derived from the key."""
    # Generate a permutation based on the key
    perm = list(range(len(text)))
    random.Random(key).shuffle(perm)

    # Apply the permutation to the text
    encrypted_text = [''] * len(text)
    for i, j in enumerate(perm):
        encrypted_text[j] = text[i]

    return ''.join(encrypted_text)

# Decryption function
def decrypt(encrypted_text, key):
    """Decrypt the text by reversing the scrambling based on the permutation derived from the key."""
    # Generate the same permutation based on the key
    perm = list(range(len(encrypted_text)))
    random.Random(key).shuffle(perm)

    # Apply the inverse permutation to the encrypted text
    decrypted_text = [''] * len(encrypted_text)
    for i, j in enumerate(perm):
        decrypted_text[i] = encrypted_text[j]

    return ''.join(decrypted_text)

# Function to load text from a file
def load_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Function to save text to a file
def save_text(file_path, text):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(text)

# Test application
def main():
    # Load text from a file
    input_file = input("Enter the path of the file to encrypt: ")
    original_text = load_text(input_file)
    print(f"Original Text: {original_text}")

    # Encryption key
    key = int(input("Enter numerical key: "))

    # Encrypt the original text
    encrypted_text = encrypt(original_text, key)

    # Save the encrypted text to a file
    encrypted_file = input("Enter the path of the file to save encrypted text: ")
    save_text(encrypted_file, encrypted_text)
    print(f"Encrypted text saved to {encrypted_file}")

    # Load the encrypted text from the file
    loaded_encrypted_text = load_text(encrypted_file)
    print(f"Loaded Encrypted Text: {loaded_encrypted_text}")

    # Decrypt the encrypted text
    decrypted_text = decrypt(loaded_encrypted_text, key)

    # Verify that the decrypted text matches the original text
    assert decrypted_text == original_text, "Decryption failed!"
    print("Decryption successful!")

if __name__ == "__main__":
    main()