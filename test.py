import decimal
# def method(value):
#     print(value[1:])
#     print(len(value))
#     print(value[-4:-1])
#     print(f'modulus {420%10}')
#     print(f'modulus {420//10}')
#     print(decimal.Decimal(0.1  + 0.2))pr
#     print(",".join(['1','3']))
#     for i in range(6):
#         print(i)
#         if(i==3):
#             break

#method("-+12")


def intToRoman(num: int) -> str:
        array_numeral = []
        while num > 0:
            if(num >= 1 and num < 4):
                num -= 1
                array_numeral.append('I')
            elif(num >= 4 and num < 5):
                num -= 4
                array_numeral.append('IV')
            elif(num >= 5 and num <= 8):
                num -= 5
                array_numeral.append('V')
            elif(num > 8 and num < 10):
                num -= 9
                array_numeral.append('IX')
            elif(num >=10 and num < 40):
                num -= 10
                array_numeral.append('X')
            elif(num >=40 and num < 50):
                num -= 40
                array_numeral.append('XL')
            elif(num >=50 and num < 90):
                num -= 50
                array_numeral.append('L')
            elif(num >=90 and num < 100):
                num -= 90
                array_numeral.append('XC')
            elif(num >=100 and num < 400):
                num -= 100
                array_numeral.append('C')
            elif(num >=400 and num < 500):
                num -= 400
                array_numeral.append('CD')
            elif(num >=500 and num < 900):
                num -= 500
                array_numeral.append('D')
            elif(num >=900 and num < 1000):
                num -= 900
                array_numeral.append('CM')
            elif(num >=1000 ):
                num -= 1000
                array_numeral.append('M')
        print('hee')
        print("".join(array_numeral))
        return "".join(array_numeral)


intToRoman(58)

