full_dot = '●'
empty_dot = '○'

def create_character(char_name, strength, intelligence, charisma):

    if not isinstance(char_name, str):
        return "The character name should be a string"
    elif char_name == "":
        return "The character should have a name"
    elif len(char_name) > 10:
        return "The character name is too long"
    elif " " in char_name:
        return "The character name should not contain spaces"
        
    if not isinstance(strength, int) or not isinstance(intelligence, int) or not isinstance(charisma, int):
        return "All stats should be integers"
    elif strength < 1 or intelligence < 1 or charisma < 1:
        return "All stats should be no less than 1"
    elif strength > 4 or intelligence > 4 or charisma > 4:
        return "All stats should be no more than 4"
    elif (strength + intelligence + charisma) != 7:
        return "The character should start with 7 points"
        
    str_dots = full_dot * strength + empty_dot * (10 - strength)
    int_dots = full_dot * intelligence + empty_dot * (10 - intelligence)
    cha_dots = full_dot * charisma + empty_dot * (10 - charisma)
    
    return f"{char_name}\nSTR {str_dots}\nINT {int_dots}\nCHA {cha_dots}"

print(create_character('ren', 4, 2, 1))