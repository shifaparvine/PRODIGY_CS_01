def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
  
    if mode == 'decrypt':
        shift = -shift

    for char in text:
        
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        
        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        
        else:
            result += char

    return result


def main():
    print("Caesar Cipher Program")
    mode = input("Choose mode (encrypt/decrypt): ").strip().lower()

    if mode not in ['encrypt', 'decrypt']:
        print("Invalid mode! Please choose either 'encrypt' or 'decrypt'.")
        return

    text = input("Enter your message: ")
    shift = int(input("Enter the shift value (1-25): "))

    result = caesar_cipher(text, shift, mode)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
