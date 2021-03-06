f = 100
print("outside F", f)
def meth1(a):
    global f
    f = f + a
    print("Inside F", f)

meth1(12)

output ==> 
outside F 100
Inside F 112

==============================================================================================================================
global f
f = 100
print("outside F", f)
def meth1(a):
    global f
    f = f + a
    print("Inside F", f)
    return f

def meth2(a):
    f = a + 10
    f = f + meth1(a)
    print(dir())
    print(f)

meth2(10)

output ==>

outside F 100
Inside F 110
['a', 'f']
130

dir() ==> Returns a list of names in current local scope or a list of object attributes

==============================================================================================================================
deleting a variable already defined
>>> del a

==============================================================================================================================
Printing Raw String ::
>>> print('foo\nbar')
foo
bar
>>> print(r'foo\nbar')
foo\nbar
>>> print(R'foo\nbar')
foo\nbar

==============================================================================================================================
>>> a = 23
>>> b = 24
>>> eval("a+b")
47

==============================================================================================================================
performing indexing and slicing operations ::

==> Only List, Tuple and String can be sliced and indexed, also they support "+" operation.

Dictionary, Set can not be sliced and indexed.


        
==============================================================================================================================        
Python Operators Precedence ::
** 
~ + -  (uniary plus and minus)
* / % //
>> <<
&
^ |
<= < > >= (comparison operators)
<> == != (equality operators)
= %= /= //= -= += *= **= (assignment operators)
is is not (identity operators)

==============================================================================================================================        
getting version of Python 

>>> import sys
>>> print(sys.version)
3.7.1 (default, Dec 14 2018, 13:28:58) 

==============================================================================================================================














