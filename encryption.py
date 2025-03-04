import random

# Seed the random number generator for reproducibility
random.seed(42)

# Encryption function
def encrypt(data, key):
    """Encrypt the data by scrambling its bytes based on a permutation derived from the key."""
    # Generate a permutation based on the key
    perm = list(range(len(data)))
    random.Random(key).shuffle(perm)

    # Apply the permutation to the data
    encrypted_data = bytearray(len(data))
    for i, j in enumerate(perm):
        encrypted_data[j] = data[i]

    return bytes(encrypted_data)

# Decryption function
def decrypt(encrypted_data, key):
    """Decrypt the data by reversing the scrambling based on the permutation derived from the key."""
    # Generate the same permutation based on the key
    perm = list(range(len(encrypted_data)))
    random.Random(key).shuffle(perm)

    # Apply the inverse permutation to the encrypted data
    decrypted_data = bytearray(len(encrypted_data))
    for i, j in enumerate(perm):
        decrypted_data[i] = encrypted_data[j]

    return bytes(decrypted_data)

# Function to load data from a file
def load_data(file_path):
    with open(file_path, 'rb') as file:
        return file.read()

# Function to save data to a file
def save_data(file_path, data):
    with open(file_path, 'wb') as file:
        file.write(data)

# Test application
def main():
    choice = input("Do you want to (e)ncrypt or (d)ecrypt a file? ").lower()

    if choice == 'e':
        # Load data from a file
        input_file = input("Enter the path of the file to encrypt: ")
        original_data = load_data(input_file)

        # Encryption key
        key = int(input("Enter numerical key: "))

        # Encrypt the original data
        encrypted_data = encrypt(original_data, key)

        # Save the encrypted data to a file
        encrypted_file = input("Enter the path of the file to save encrypted data: ")
        save_data(encrypted_file, encrypted_data)
        print(f"Encrypted data saved to {encrypted_file}")

    elif choice == 'd':
        # Load data from a file
        input_file = input("Enter the path of the file to decrypt: ")
        encrypted_data = load_data(input_file)

        # Decryption key
        key = int(input("Enter numerical key: "))

        # Decrypt the encrypted data
        decrypted_data = decrypt(encrypted_data, key)

        # Save the decrypted data to a file
        decrypted_file = input("Enter the path of the file to save decrypted data: ")
        save_data(decrypted_file, decrypted_data)
        print(f"Decrypted data saved to {decrypted_file}")

    else:
        print("Invalid choice. Please choose 'e' for encryption or 'd' for decryption.")

if __name__ == "__main__":
    main()