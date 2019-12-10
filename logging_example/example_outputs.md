### Here we start an ipython session and import our foo package

```
$ ipython
Python 3.7.3 (default, Mar 27 2019, 22:11:17) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.6.1 -- An enhanced Interactive Python. Type '?' for help.

In [1]: from logging_example import foo

In [2]: exit
```

###  A quick `ls` to show that `foo.log` got created thanks to our `__init.py__`

```
$ ls
BinaryTree.ipynb  BinaryTree2.png  BinaryTree4.png  BinaryTree6.png  CircularBuffer.ipynb  LICENSE    Trie.ipynb  logging_example
BinaryTree1.png   BinaryTree3.png  BinaryTree5.png  BinaryTree7.png  Introduction_I.ipynb  README.md  foo.log     testing_example
```

### Lastly, we see that our `INFO` message was logged at import time

```
$ cat foo.log 
2019-12-11 08:32:04,281 DEBUG: The foo module was imported.
2019-12-11 08:32:04,281 INFO: The foo module was imported.
2019-12-11 08:32:04,281 WARNING: The foo module was imported!
2019-12-11 08:32:04,281 ERROR: Ooops. The foo module was imported!
2019-12-11 08:32:04,282 CRITICAL: Agh! The foo module was imported!
```
