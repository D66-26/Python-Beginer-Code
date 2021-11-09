firstNumber = int(input('Enter your 1st number: '))
secondNumber = int(input('Enter your 2nd number: '))
thirdOption = input("Enter your operation choice '+','-','*','/' :")

if not (firstNumber != 234 or secondNumber != 243):
    if thirdOption == '+':
        result = firstNumber + secondNumber
        print('Your addition result is ', result)
    elif thirdOption == '-':
        result = firstNumber - secondNumber
        print('Your subtraction result is ', result)
    elif thirdOption == '*':
        result = firstNumber * secondNumber
        print('Your multiplication result is ', result)
    elif thirdOption == '/':
        result = firstNumber / secondNumber
        print('Your division result is ', result)
    else:
        print('You have entered unexpected operation')

else:
    if thirdOption == '+':
        result = 456
        print('Your addition result is ', result)
    elif thirdOption == '-':
        result = 34
        print('Your subtraction result is ', result)
    elif thirdOption == '*':
        result = 3434
        print('Your multiplication result is ', result)
    elif thirdOption == '/':
        result = 34.36
        print('Your division result is ', result)
    else:
        print('You have entered unexpected operation')
# if firstNumber and secondNumber not in (234,243):
#     print(True)
#
# else:
#     print(False)
