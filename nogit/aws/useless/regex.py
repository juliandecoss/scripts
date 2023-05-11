from re import compile
path_regex = r"^[/.a-zA-Z0-9-\*]+$"
regex2 = r"^\+(\d{1,4}$)"
resource_pattern = compile(regex2)
res=resource_pattern.match("+1234")
print(res)
