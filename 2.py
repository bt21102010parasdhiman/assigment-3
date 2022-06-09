b = float(input('Enter first number: '))
a = input('Enter sign(+, -, *, / or q for quit): ')

while (a!='q'):
    if a=='+':
        b = b + float(input('Next number: '))
    elif a == '-':
        b = b - float(input('Next number: '))
    elif a == '*':
        b = b * float(input('Next number: '))
    elif a == '/':
        b = b / float(input('Next number: '))
    else:
        print('Invalid operator, try again')
    a = input('Enter next sign(+, -, *, / or q for quit): ')

print(b)

# Or we can also use eval()
