# Python program to execute
# main directly
print ("Always executed")

def my_function():
    print ("I am inside function")
 
if __name__ == "__main__":
    print ("Executed when invoked directly")
    my_function()
else:
    print ("Executed when imported")
    
