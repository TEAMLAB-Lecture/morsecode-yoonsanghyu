# -*- coding: utf8 -*-


# Help Function - 수정하지 말 것
def get_morse_code_dict():
    morse_code = {
        "A": ".-", "N": "-.", "B": "-...", "O": "---", "C": "-.-.", "P": ".--.", "D": "-..", "Q": "--.-", "E": ".",
        "R": ".-.", "F": "..-.", "S": "...", "G": "--.", "T": "-", "H": "....", "U": "..-", "I": "..", "V": "...-",
        "K": "-.-", "X": "-..-", "J": ".---", "W": ".--", "L": ".-..", "Y": "-.--", "M": "--", "Z": "--.."
    }
    return morse_code


# Help Function - 수정하지 말 것
def get_help_message():
    message = "HELP - International Morse Code List\n"
    morse_code = get_morse_code_dict()

    counter = 0

    for key in sorted(morse_code):
        counter += 1
        message += "%s: %s\t" % (key, morse_code[key])
        if counter % 5 == 0:
            message += "\n"

    return message


def is_help_command(user_input):

    return user_input.lower() == 'help' or user_input.lower() == 'h'


def is_validated_english_sentence(user_input):
    
    user_input = user_input.replace(".","").replace(",","").replace("!","").replace("?","").replace(" ","")
    change_input = [char for char in user_input if char.isalpha()]

    return not len(change_input) == 0 and len(user_input) == len(change_input)


def is_validated_morse_code(user_input):

    morse_dict = get_morse_code_dict()
    user_input = user_input.split()
    for i in user_input:
        if i not in morse_dict.values():
            return False
        
    return True


def get_cleaned_english_sentence(raw_english_sentence):
 
    result = raw_english_sentence.replace(".","").replace(",","").replace("!","").replace("?","")
    return result



def decoding_character(morse_character):
    reverse_dict = dict(map(reversed, get_morse_code_dict().items()))
    return reverse_dict[morse_character]



def encoding_character(english_character):
    morse_code_dict = get_morse_code_dict()
    return morse_code_dict[english_character]



def decoding_sentence(morse_sentence):
    morse_list = morse_sentence.split(" ")
    result = [" " if char == "" else decoding_character(char) for char in morse_list]
    return "".join(result)



def encoding_sentence(english_sentence):

    clean_text = get_cleaned_english_sentence(english_sentence).upper().split()

    result = []
    for word in clean_text:
        for char in word:
            result.append(encoding_character(char))
            result.append(" ")
        result.append(" ")

    return "".join(result)[:-2]



def main():
    print("Morse Code Program!!")
    # ===Modify codes below=============
    exit_program = 0
    while True:
        
        #입력
        while True:
                input_msg = input("Input your message(H - Help, 0 - Exit):")
                if input_msg == '0':
                    exit_program = 1
                    break
                if is_help_command(input_msg):
                    get_help_message()
                if is_validated_english_sentence(str(input_msg)):
                    print(encoding_sentence(str(input_msg)))
                    break
                if is_validated_morse_code(str(input_msg)):
                    print(decoding_sentence(str(input_msg)))
                    break                   
                else:
                    print("Wrong Input")
                    
        if exit_program == 1:
            break



    # ==================================
    print("Good Bye")
    print("Morse Code Program Finished!!")

if __name__ == "__main__":
    main()
