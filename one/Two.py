import one
print("Top level in Two.py")
one.func()
if __name__ == '__main__':
    print("Two.py is run directly")
else:
    print("Two.py has been imported")