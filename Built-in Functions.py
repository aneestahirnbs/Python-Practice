#The function list is extracted from Python Standard library
# abs()	dict()	help()	min()	setattr()
# all()	dir()	hex()	next()	slice()
# any()	divmod()	id()	object()	sorted()
# ascii()	enumerate()	input()	oct()	staticmethod()
# bin()	eval()	int()	open()	str()
# bool()	exec()	isinstance()	ord()	sum()
# bytearray()	filter()	issubclass()	pow()	super()
# bytes()	float()	iter()	print()	tuple()
# callable()	format()	len()	property()	type()
# chr()	frozenset()	list()	range()	vars()
# classmethod()	getattr()	locals()	repr()	zip()
# compile()	globals()	map()	reversed()	__import__()
# complex()	hasattr()	max()	round()
# delattr()	hash()	memoryview()	set()


#abs(x)
#Returns the absolute of number
print("abs(-1):",abs(-1))

#all(iterable)
#Returns true if elements of iterable are true
print("all([1,23,4,5,None]):",all([1,23,4,5,None]))

#ascii(x)
#Return the printable string representation of passed value
print("ascii():",ascii(''))

# bin(x)
# Convert an integer number to a binary string.
print("bin(12):",bin(12))

# bool([x])
# Return a Boolean value, i.e. one of True or False. x is converted using the standard truth testing procedure.
print("bool[{}]:",bool({}))

# bytearray([source[, encoding[, errors]]])
# Return a new array of bytes.
print("bytearray(5)",bytearray(5))

# classmethod(function)
# Return a class method for function.
#More like a static method in c,c++
class C:
    @classmethod
    def foo(cls):
        print("Static method or class method more specifically")
c_obj=C();
c_obj.foo();
C.foo();

# class complex([real[, imag]])
# Return a complex number with the value real + imag*1j or convert a string or number to a complex number.
c=complex(1,2)
print("Complex Number complex(1,2):",c)

# delattr(object, name)
# This is a relative of setattr(). The arguments are an object and a string.
c_obj.newAttr="blingggg"
print("C newAttr",c_obj.newAttr)
delattr(c_obj,"newAttr")

# class dict(**kwarg)
# class dict(mapping, **kwarg)
# class dict(iterable, **kwarg)
# Create a new dictionary. The dict object is the dictionary class.
dic=dict({'alpha':1,'beta':2,'gamma':3})
print("dic['alpha']:",dic['alpha'])

# dir([object])
# Without arguments, return the list of names in the current local scope.
print("Names in current scope:",dir())

# divmod(a, b)
# Take two (non complex) numbers as arguments and return a pair of numbers consisting of their quotient and remainder
print("divmod(5,2):",divmod(5,2))

# enumerate(iterable, start=0)
# Return an enumerate object. iterable must be a sequence, an iterator, or some other object which supports iteration.
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print("list(enumerate(seasons,0)):",list(enumerate(seasons,0)))

# eval(expression, globals=None, locals=None)
# The arguments are a string and optional globals and locals. If provided, globals must be a dictionary. If provided, locals can be any mapping object.
# The expression argument is parsed and evaluated as a Python expression
x = 1
print("eval('x+1'):",eval('x+1'))

# filter(function, iterable)
# Construct an iterator from those elements of iterable for which function returns true.
def isEven(x):
    return x %2 ==0

print("Filtered list of even numbers :",list(filter(isEven, [1,2,3,4,5,6,7,8,9])))


# class float([x])
# Return a floating point number constructed from a number or string x.
print("float('-1.23'):",float('-1.23'))
