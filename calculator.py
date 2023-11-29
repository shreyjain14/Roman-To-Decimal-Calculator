def convert(roman):
    roman = roman.upper()
    if checkValidRoman(roman) is not True:
        return "ERROR: Enter a valid roman number"

    hashmap = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    decimal = 0

    for index in range(len(roman) - 1):
        if hashmap[roman[index]] < hashmap[roman[index + 1]]:
            decimal -= hashmap[roman[index]]
        else:
            decimal += hashmap[roman[index]]

    return "Decimal: " + str(decimal + hashmap[roman[-1]])


def checkValidRoman(roman):
    for i in roman:
        if i not in ['I', 'V', 'X', 'L', 'C', 'D', 'M']:
            return False
    for i in range(len(roman) - 3):
        if roman[i] == roman[i+1] == roman[i+2] == roman[i+3]:
            return False
    return True


if __name__ == "__main__":
    print(convert('CMXXIV'))
