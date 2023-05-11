from math import floor

def findMedian(arr:list):
    arr.sort()
    medium = int((len(arr)-1)/2)
    return arr[medium]

if __name__ == '__main__':
    prueba = []
    for i in range(0,10001):
        prueba.append(i)
    print(len(prueba))
    result = findMedian(prueba)
    print(result)