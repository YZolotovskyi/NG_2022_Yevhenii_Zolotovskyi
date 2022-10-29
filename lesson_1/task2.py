OneNumder = int(input("Enter first number "))
TwoNumder = int(input("Enter second number "))
functions = input("Enter sign \n + - addition \n - -subtraction \n / - division\n * -multiplication\n ** -exponentition \n")

if functions == '+':
    print("Result" , OneNumder + TwoNumder)
elif functions == '-':
    print("Result" , OneNumder - TwoNumder)
elif functions == '/':
    print("Result" , OneNumder / TwoNumder)
elif functions == '*':
    print("Result" , OneNumder * TwoNumder)
elif functions == '**':
    print("Result" , OneNumder ** TwoNumder)
else:
    print("ERROR")