
def user_name(print_name):
    print(print_name('Safari'))

user_name(lambda name: name)

def user_names(fn, *args):
    for arg in args:
        print(fn(arg))

user_names(lambda name: name, 'Safari', 'Ghandi', 'Irene','John')

def square_of_number(fn, *args):
    for arg in args:
        print('Result: {:^50.2f}'.format(fn(arg)))

square_of_number(lambda data: data**2, 10, 15, 22, 30)