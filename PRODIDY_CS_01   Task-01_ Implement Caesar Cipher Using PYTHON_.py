
def caesar_cipher(text, shift, mode="encrypt"):
    result = ""
    for char in text:
        if char.isalpha():
            shift_dir = shift if mode == "encrypt" else -shift
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift_dir) % 26 + base)
        else:
            result += char
    return result

# Example Usage
message = input("Enter your message: ")
shift = int(input("Enter shift value: "))
mode = input("Encrypt or Decrypt (encrypt/decrypt): ").lower()
print(f"Result: {caesar_cipher(message, shift, mode)}")