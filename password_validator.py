def validator(password):

    dict_characters = ["&", "+", "@", "$", "#", "%", "!", "*", "(", ")", "-", "/", "_"]

    letter_counter = 0
    numeric_counter = 0
    special_counter = 0

    password_size = len(password)
    
    for i in password:
        if i.isupper(): 
            letter_counter += 1
        if i.isnumeric():
            numeric_counter += 1
        if i in dict_characters:
            special_counter += 1

    if password_size < 7 or password_size > 15:
        print("Senha deve ter de 7 a 15 caracteres")
        return "invalido"

    if letter_counter < 2:
        print("Senha deve conter 2 letras maiúsculas")
        return "invalido"

    if numeric_counter < 2:
        print("Senha deve conter pelo menos 2 números")
        return "invalido"

    if special_counter < 2:
        print("Senha deve conter pelo menos 2 caracteres especiais")
        return "invalido"

    if " " in password:
        print("Senha não pode conter espaços")
        return "invalido"

    if password[0].isalpha() or password[0].isnumeric():
        return "valido"
    else:
        print("O primeiro caractere deve ser alfabético ou numérico")
        return "invalido"
                    

# print(validator(input("Enter your password: ")))