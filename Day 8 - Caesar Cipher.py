import string

print("Welcome to Ceasar Cipher")
end = False
alphabet = list(string.ascii_lowercase)


def caesar(start_text, shift_amount, cipher_direction):
    output = []
    if cipher_direction == 'encode':
        for character in start_text:
            if character in alphabet:
                position = alphabet.index(character)
                new_position = (position + shift_amount)%26
                output.append(alphabet[new_position])
            else:
                output.append(character)
        final = ''
        final = final.join(output)
        return(f"Here is your encoded result: {final}")
    elif command == 'decode':
        for character in start_text:
            if character in alphabet:
                position = alphabet.index(character)
                new_position = position - shift_amount
                output.append(alphabet[new_position])
            else:
                output.append(character)
        final = ''
        final = final.join(output)
        return(f"Here is your decoded result: {final}")

while end == False:
    command = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    message = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))%26
    print(caesar(message, shift, command))

    repeat = input("Type 'yes' if you want to go again. Otherwise type 'no'. \n")
    if repeat == 'no':
        print("Goodbye")
        end = True
