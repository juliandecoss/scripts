BINARY_VALUE = [1,2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456, 536870912, 1073741824, 2147483648, 4294967296]
def flippingBits(n):
    # Write your code here
    b = bin(n)
    byte = b.split("b")[1]
    flip_byte = ""
    zeros = ""
    decimal = 0
    if len(byte)<34:
        missing = 33-len(byte)
        for miss in range(1,missing):
            zeros += "0"
    byte = zeros + byte
    for bit in byte:
        if bit == "1":
            flip_byte += "0"
        else: 
            flip_byte += "1"
    counter = -1
    for i in range(31,-1,-1):
        value = flip_byte[i]
        counter += 1
        if value == "1":
            decimal += BINARY_VALUE[counter]
    return decimal

flippingBits(1)

d = {}
