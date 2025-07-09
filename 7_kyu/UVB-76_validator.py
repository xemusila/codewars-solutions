def validate(message):
    lst = message.split()
    if len(lst) != 8: return False
    return lst[0] == "MDZHB" and all(len(lst[i]) == 2 \
                                 and lst[i].isdigit() for i in (1, 4, 5, 6, 7)) \
           and len(lst[2]) == 3 and lst[3].isupper() and lst[3].isalpha() \
           and lst[2].isdigit()

# another solution
import re
def validate(message):
    return bool(re.fullmatch(r'MDZHB \d{2} \d{3} [A-Z]* \d{2} \d{2} \d{2} \d{2}', message))