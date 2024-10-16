import random
from retrying import retry

@retry(stop_max_attempt_number=3)
def my_function():
    if random.randint(0, 10) < 5:
        print('Failed')
        raise ValueError('Oops!')
    else:
        print('Succeeded')

my_function()
