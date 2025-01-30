class StringManipulator:
def __init__(self):
self.user_string = ""
def get_String(self):
self.user_string = input("Enter a string: ")
def print_String(self):
print("Uppercase string: {}".format(self.user_string.upper()))

# Example usage:
string_manipulator = StringManipulator()
string_manipulator.get_String() 
string_manipulator.print_String() 
