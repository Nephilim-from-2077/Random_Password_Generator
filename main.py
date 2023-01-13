import random

upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_case = "abcdefghijklmnopqrstuvwxyz"
number = "0123456789"
symbols = "!@#$%^&*<>\/|"
length_of_password = 8
pass_generator = upper_case + lower_case + symbols + number

password = "".join(random.sample(pass_generator, length_of_password))

print("Hey, here is your Password: ", password)