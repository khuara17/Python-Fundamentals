'''
EXCEPTIONS              Desciption

Exception           Base class for all exceptions

ArithmeticError     Base class for all errors that occur for numeric calculation.

OverflowError       Raised when a calculation exceeds maximum limit for a numeric type.

FloatingPointError  Raised when a floating point calculation fails.

ZeroDivisionError   Raised when division or modulo by zero takes place for all numeric types.

AttributeError      Raised in case of failure of attribute reference or assignment.

EOFError            Raised when there is no input from either the raw_input() or input() function and the end of file is reached.

ImportError         Raised when an import statement fails.

KeyboardInterrupt   Raised when the user interrupts program execution, usually by pressing Ctrl+c.

IndexError              Raised when an index is not found in a sequence.
	
KeyError                Raised when the specified key is not found in the dictionary.

NameError               Raised when an identifier is not found in the local or global namespace.

UnboundLocalError       Raised when trying to access a local variable in a function or method but no value has been assigned to it.

EnvironmentError        Base class for all exceptions that occur outside the Python environment.
	
IOError                 Raised when an input/ output operation fails, such as the print statement or the open() function when trying to open a file that does not exist.

IOError                 Raised for operating system-related errors.

SyntaxError             Raised when there is an error in Python syntax.

IndentationError        Raised when indentation is not specified properly.

SystemError             Raised when the interpreter finds an internal problem, but when this error is encountered the Python interpreter does not exit.
		
ValueError              raised when the built-in function for a data type has the valid type of arguments, but the arguments have invalid values specified.
'''

x = 2
c = {
    2 : 'z'
}
try:
    print(x)
    # print(c[4])
    # x = x / 0
# except ZeroDivisionError:
#     print("ZeroDivisionError has occured...")
except Exception as e:
    print("Some Error has occured..."+str(e))
else:
    print("I am else part")
# except KeyError as i:
#     print("Keyerror has occured"+ str(i))
# except IndentationError:
#     print("Intendatio error")
# except Exception as e:
#     print("Some Error has occured..."+str(e))
finally:
    print("I will get executed everytime..")
