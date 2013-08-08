"""
Module for general debugging

Functions
---------
`breakpoint`: Stop execution of program and drop into IPython shell

"""
from IPython import embed

"""
Stop program execution and drop into IPython shell

Notes
-----

* All global variables will be available in the IPython shell
* Use `dir()` to list all global variables
* Use `exit` or Ctrl+D to resume program

"""
breakpoint = embed
