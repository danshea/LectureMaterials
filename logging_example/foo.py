#
# Author: Dan Shea
# Date: 2019.12.10
# Description: simple module that shows how to work with doctest and pytest, and
# updated to also show logging.

class Foo:
    def __init__(self, value=None):
        self.value = value

    def generator(self):
        myvalue = self.value
        while True:
            yield myvalue
            if type(myvalue) is int:
                myvalue += 1
            elif type(myvalue) is str:
                myvalue = myvalue[1:] + myvalue[0]

    def __setattr__(self, name, value):
        if name == 'value':
            if type(value) in [int, str, type(None)]:
                super().__setattr__(name, value)
            else:
                raise TypeError('value must be of type int, str, or None')
        else:
            super().__setattr__(name, value)

    def __repr__(self):
        '''
        Representation of Foo instance
        doctest cases follow:

        >>> Foo()
        <Foo: <class 'NoneType'> generator>

        >>> Foo(0)
        <Foo: <class 'int'> generator>

        >>> Foo('foo')
        <Foo: <class 'str'> generator>
        '''
        return f'<Foo: {type(self.value)} generator>'

# pytest test cases
def test_None_gen():
    '''
    Test that a None genrator yields None
    '''
    foo = Foo()
    assert next(foo.generator()) == None

def test_int_gen():
    '''
    Test that an int generator returns its initial value
    '''
    foo = Foo(0)
    assert next(foo.generator()) == 0

def test_str_gen():
    '''
    Test that a string generator returns its initial value
    '''
    foo = Foo('foo')
    assert next(foo.generator()) == 'foo'
