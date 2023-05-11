from re import findall
string = "last_name1"
string = string.lower() if string.isupper() else string
splitted = findall(r"[A-Za-z][a-z0-9]*", string)
print(splitted)
if splitted and len(splitted) > 1:
    subsequent_words = "_".join(
        sub_string.lower() for sub_string in splitted[1:]
    )
    transformed_string = "_".join([splitted[0].lower(), subsequent_words])
    print(transformed_string)