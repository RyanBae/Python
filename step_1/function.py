"""=============================
function
"""
def say_hello() :
    print('hello')


# say_hello()

"""=============================
input plus function
"""
def sum(x,y) :
    print(x+y)

#x = int(input('input x : '))
#y = int(input('input y : '))

# jb_sum(x,y)

"""=============================
return value
"""

def return_sum(x,y) :
    z = x + y
    return z

#x = int(input("input x : "))
#y = int(input("input y : "))
#print(return_sum(x,y))

"""=============================
Multiple return values
: if there are multiple returns, the first result return.
"""

def values_sum(x,y) :
    w = x * y
    return w
    z = x + y
    return z

#x = int(input("input x : "))
#y = int(input("input y : "))
#print(values_sum(x,y))

"""=============================
Parameter input count to be different
is error
"""

def parameter_diff_sum(x,y) :
    z = x + y
    return z

#print(parameter_diff_sum(1))

"""=============================
input not result is default setting
: default Position is after an argument without a default value
  o = def diff_default_sum(x,y=1) :
  x = def diff_default_sum(x=1,y) :
"""

def diff_default_sum(x,y=1) : 
    z = x + y
    return z

#print(diff_default_sum(1))

"""=============================
function call is argment name utilization call
"""

def arg_name_call(x,y) :
    z = x / y
    return z

#print(arg_name_call(x=10,y=5))
#print(arg_name_call(y=5,x=10))

"""=============================
function call is argment name utilization call 
:If you do not include the name of the argument, 
it is assigned in order. If there is a overlap, there will be an error. 
Arguments with no name must be placed before arguments with names.
"""

def arg_names_call(x,y,z) :
    return x + y + z
#= true
#print(arg_names_call(1, z=2, y=3))

#= fail
#print(arg_names_call(1, x=2, y=3))
#print(arg_names_call(z=1, 2, y=3))

"""=============================
variable factor
You can use any value you enter as an argument without specifying the number of arguments.

Use * to save the 'tuple'.
"""
def variable_tuple(*x) :
    print(x)

variable_tuple('one', 'two', 'three', 'four')

"""
Use ** to save the dict(Dictionary / key : value)
""" 

def variable_dict(**x) :
    print(x)

#variable_dict(one=1, two=2, three=3, four=4)
