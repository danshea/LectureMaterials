### Running doctest verbosely

```
(base) nucleus:testing_example(41062)$ python -m doctest -v foo.py 
Trying:
    Foo()
Expecting:
    <Foo: <class 'NoneType'> generator>
ok
Trying:
    Foo(0)
Expecting:
    <Foo: <class 'int'> generator>
ok
Trying:
    Foo('foo')
Expecting:
    <Foo: <class 'str'> generator>
ok
8 items had no tests:
    foo
    foo.Foo
    foo.Foo.__init__
    foo.Foo.__setattr__
    foo.Foo.generator
    foo.test_None_gen
    foo.test_int_gen
    foo.test_str_gen
1 items passed all tests:
   3 tests in foo.Foo.__repr__
3 tests in 9 items.
3 passed and 0 failed.
Test passed.
```

### Running pytest verbosely

```
(base) nucleus:testing_example(41059)$ python -m pytest -v foo.py 
===================================================================== test session starts ======================================================================
platform linux -- Python 3.7.3, pytest-5.0.1, py-1.8.0, pluggy-0.12.0 -- /home/dshea/anaconda3/bin/python
cachedir: .pytest_cache
rootdir: /dsu1/Research/LectureMaterials/testing_example
plugins: arraydiff-0.3, remotedata-0.3.1, openfiles-0.3.2, doctestplus-0.3.0
collected 3 items                                                                                                                                              

foo.py::test_None_gen PASSED                                                                                                                             [ 33%]
foo.py::test_int_gen PASSED                                                                                                                              [ 66%]
foo.py::test_str_gen PASSED                                                                                                                              [100%]

=================================================================== 3 passed in 0.04 seconds ===================================================================
```

