from random_password_generator import RandomPasswordGenerator

pass_one = RandomPasswordGenerator(4)
pass_two = RandomPasswordGenerator(4)
assert pass_one != pass_two