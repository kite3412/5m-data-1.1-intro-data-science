def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
    return

fizz_buzz(3)
fizz_buzz(5)
fizz_buzz(15)
fizz_buzz(13)