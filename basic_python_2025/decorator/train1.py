def run_time_prossecor(func):
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Time:", end - start)
        return result
    return wrapper

@run_time_prossecor
def list_generator(n):
    return [i for i in range(int(n))]

try:
    n = input("Enter a number: ")
    print(list_generator(n))
except ValueError:
    print("Please enter a number value!")
except Exception as e: 
    print("An error occurred: " + str(e))
