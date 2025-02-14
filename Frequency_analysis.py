import matplotlib.pyplot as plt
from collections import OrderedDict

ENGLISH_FREQUENCY_DICTIONARY = {
    "A": 8.12, "B": 1.49, "C": 2.71, "D": 4.32, "E": 12.02, "F": 2.30, "G": 2.03,
    "H": 5.92, 'I': 7.31, "J": 0.10, "K": 0.69, "L": 3.98, "M": 2.61, "N": 6.95, "O": 7.68, "P": 1.82,
    "Q": 0.11, "R": 6.02, "S": 6.28, "T": 9.10, "U": 2.88, "V": 1.11, "W": 2.09, "X": 0.17, "Y": 2.11, "Z": 0.07
}
DECRYPT_KEY_DICTIONARY = {}

ENGLISH_FREQUENCY_ORDERED_LIST = [letter for letter, _ in sorted(ENGLISH_FREQUENCY_DICTIONARY.items(), key=lambda item: item[1], reverse=True)]

def frequency_analysis(encrypted_message: str) -> dict:
    '''
    Gets the frequency of letters in the encrypted message and assigns it to a dictionary.
    '''

    frequency_dictionary = {letter: 0 for letter in ENGLISH_FREQUENCY_DICTIONARY}
    encrypted_message = format_encrypted_message(encrypted_message, "2")
    text_length = len(encrypted_message)
    for character in encrypted_message:
        frequency_dictionary[character] += 1 / text_length

    return frequency_dictionary

def plot_frequency_dictionary(frequency_dictionary: dict) -> None:
    '''
    Plots the frequecny of letters in the encrypted messag and returns ordered frequency dictionary.
    The plot pop up must be closed for the code to continue.
    '''

    frequency_ordered = OrderedDict(sorted(frequency_dictionary.items(), key = lambda item: item[1], reverse = True))
    letters = frequency_ordered.keys()
    frequency = frequency_ordered.values()
    plt.bar(letters, frequency, color='red')
    plt.title("Frequency Analysis")
    plt.show()

    return frequency_ordered

def format_encrypted_message(encrypted_message: str, option: str) -> str:
    '''
    Fomrats the encrypted message for a given option.

    Option 1 will uppercase the encrypted message.

    Option 2 will uppercase the encrypted message and remove the spaces.
    '''

    if(option == '1'):
        return encrypted_message.upper()
    
    if(option == "2"):
        return ''.join(filter(str.isalpha, encrypted_message.upper()))

    return encrypted_message

def auto_decrypt(encrypted_message: str, frequency_ordered: dict) -> str:
    '''
    Does a single pass over of the string replacing the letters using a dictionary 
    matching the highest frequency letters in message and highest frequency letters in the englis language. 
    '''

    encrypted_message = format_encrypted_message(encrypted_message, "1")
    decrypted_message = ""
    decrypt_key_dictionary = frequency_ordered
    #print(decrypt_key_dictionary)
    for index, key in enumerate(decrypt_key_dictionary.keys()):
        DECRYPT_KEY_DICTIONARY[key] = ENGLISH_FREQUENCY_ORDERED_LIST[index]
    #print(decrypt_key_dictionary)
    for character in encrypted_message:
        if not character.isalpha():
            decrypted_message += character
            continue
        decrypted_message += DECRYPT_KEY_DICTIONARY[character]

    return decrypted_message


def replace_letter(encrypted_message, cipher_letter, new_letter):
    '''
    Replaces cipher letter in dictionary with suggested new letter
    '''
    encrypted_message = format_encrypted_message(encrypted_message, "1")
    decrypted_message = ""
    DECRYPT_KEY_DICTIONARY[cipher_letter] = new_letter
    for character in encrypted_message:
        if not character.isalpha():
            decrypted_message += character
            continue
        decrypted_message += DECRYPT_KEY_DICTIONARY[character]

    return decrypted_message



if __name__ == "__main__":
    while True:
        encrypted_message = input('Enter encrypted message(Enter .. to exit): \n')
        if  encrypted_message == "..":
           break
        frequency_dictionary = frequency_analysis(encrypted_message)
        #print(f"Inputted message: {encrypted_message}")
        #print(f"The frequency dictionary is {frequency_dictionary}")
        frequency_ordered = plot_frequency_dictionary(frequency_dictionary)
        decrypted_message = auto_decrypt(encrypted_message, frequency_ordered)
        print(f"Inputted message: \n{encrypted_message}")
        print(f"The decrypted message is:\n{decrypted_message}")
        cipher_letter = input('Enter cipher letter to replace(Enter .. to exit): ')
        if cipher_letter == "..":
            break
        while cipher_letter != "..":
            new_letter= input('Enter new letter to replace with:')
            decrypted_message=replace_letter(encrypted_message, cipher_letter.upper(), new_letter.upper())
            print(f"Inputted message: \n{encrypted_message}")
            print(f"The decrypted message is:\n{decrypted_message}")
            cipher_letter = input('\nEnter cipher letter to replace(Enter .. to exit): ')
