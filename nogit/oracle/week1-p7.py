def matchingStrings(strings, queries):
    queries_coincidence = []
    counter = 0
    for querie in queries:
        counter = 0
        for string in strings:
            if querie == string:
                counter +=1
        queries_coincidence.append(counter)
    return queries_coincidence


strings = ['abcde', 'sdaklfj', 'asdjf', 'na', 'basdn', 'sdaklfj', 'asdjf', 'na', 'asdjf', 'na', 'basdn', 'sdaklfj', 'asdjf']
queries = ['abcde', 'sdaklfj', 'asdjf', 'na', 'basdn']
a = matchingStrings(strings,queries)
print(a)


def matchingStrings2(strings:list, queries):
    queries_coincidence = []
    for q in queries:
        a = strings.count(q)
        queries_coincidence.append(a)
    return queries_coincidence

b = matchingStrings2(strings,queries)
print(b)