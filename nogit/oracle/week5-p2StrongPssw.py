numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"
missing = [False,False,False,False]
password = "#HackerRank"
for n in password:
    if n in numbers:
        missing[0] = True
    elif n in lower_case:
        missing[1] = True
    elif n in upper_case:
        missing[2] = True
    elif n in special_characters:
        missing[3] = True
pas_len = len(password)
mis_len = 0 if pas_len >= 6 else 6-pas_len
mis_rules = 4 - missing.count(True)
if mis_rules >= mis_len:
    print(mis_rules)
else:
    print(mis_len)
breakpoint()
