import re
def formatMethods(mode:str,word:str):
    if mode == "S":
        return word.replace("()","")
    else:
        return word+"()"

def formatStrings(string:str):
    array = string.split(";")
    if array[0] == "S":
        mayus = re.findall(r"[A-Z]",array[2])
        for letter in mayus:
            array[2] = array[2].replace(letter,f" {letter.lower()}")
        formatted_word = array[2]
        if array[1] == "M":
            formatted_word=formatMethods("S",formatted_word)
    else:

        formatted_words = array[2].split(" ")
        start = 0
        formatted_word = ""
        for word in formatted_words:

            start += 1
            if start >1:
                word = word.capitalize()
            formatted_word += word
        if array[1] == "C":
            first_letter = formatted_word[0]
            formatted_word = formatted_word.replace(first_letter,first_letter.upper())
        elif array[1] == "M":
            formatted_word = formatMethods("C",formatted_word)
    formatted_word = formatted_word.strip()
    print(formatted_word)

    return formatted_word
if __name__ == '__main__':
    #string = input()
    problems =[
        "S;V;iPad",
        "C;M;mouse pad",
        "C;C;code swarm",
        "S;C;OrangeHighlighter",
    ]
    solution = [
        "i pad",
        "mousePad()",
        "CodeSwarm",
        "orange highlighter",
    ]
    for problem in problems:
        elindex = problems.index(problem)
        result = formatStrings(problem)
        print(result == solution[elindex])
        if not result == solution[elindex]:
            breakpoint()
    
