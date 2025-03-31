def divide(a, b):
    try:
        a,b = int(a), int(b)
        result = a / b
        return result
    except ZeroDivisionError:
        return "You can't divide by zero!"
    except TypeError:
        return "Please enter only numbers!"
    except ValueError:
        return "Please enter a number value!"
    except Exception as e:
        return "An error occurred: " + str(e)
    finally:
        print("This function run successfuly!")

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

print("Result:", divide(num1, num2))