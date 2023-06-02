from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)

def caesar(direction, text, shift):
    if direction == "decode":
        shift *= -1
    secret_message = []
    for i in text:
        if i in alphabet:   
            secret_message.append(alphabet[alphabet.index(i)+shift])
        else:
            secret_message.append(i)
    print(f"The {direction}d text is {''.join(secret_message)}\n")

still_playing = True
while still_playing:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift %= 26
    caesar(direction, text, shift)
    still_playing = input("Type 'yes' if you'd like to go again.  Otherwise type 'no'.\n")
    if still_playing == 'no':
        still_playing = False
        print("Goodbye.")