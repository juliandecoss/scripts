k=87
if k > 26:
    factor = k//26
    k = k - 26*factor
breakpoint()
abecedary = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
abecedary_mayus = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
caesar_cipher = abecedary[k:]+abecedary[:k]
caesar_cipher_mayus = abecedary_mayus[k:]+abecedary_mayus[:k]
s= "www.abc.xy"
s = list(s)
res= []
for str in s:
    if str.lower() not in abecedary:
        res.append(str)
    elif str.isupper():
        index = abecedary_mayus.index(str)
        res.append(caesar_cipher_mayus[index])
    else:
        index = abecedary.index(str)
        res.append(caesar_cipher[index])
rs = "".join(res)
print(rs)
