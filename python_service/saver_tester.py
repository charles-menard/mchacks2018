from saver import Saver

my_saver = Saver()

path = "./models/fruits/apple"

array = my_saver.load(path, "my_array")

print(array)