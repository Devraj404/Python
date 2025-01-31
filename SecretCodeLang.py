import random

def coding(word):
    secret_word = ""
    if len(word) <= 2:
        word = word[::-1]
        return word
        
    random_chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    word += word[0]
    word = word[1::]
    
    for x in range(3):
        secret_word += random.choice(random_chars)
    
    secret_word += word
    for i in range(3):
        secret_word += random.choice(random_chars)


    return secret_word 




def decoding(secret_code):

    if len(secret_code) <= 2:
        secret_code = secret_code[::-1]
        return secret_code

    real_msg = secret_code[3:-3]
    f_char = real_msg[-1]
    f_char += real_msg
    real_msg = f_char[0:-1]

    return real_msg


message = input("Enter message to send to Agent : ")

secret_code = coding(message)
print("Secret Code : ", secret_code)

decoded_word = decoding(secret_code)
print("Decoded word : ", decoded_word)
