REA Robot solution
==================

This document describes the solution presented in the current directory.


Overview
--------

* This solution was developed on a Mac using the default Python 2.7 installation and should run on any compatible *nix environment.

* Unit testing was done using Python's default **unittest** module (automatically installed) and the **mock** module (can be installed using PIP).

* Input can be provided either via console or through a text file. There are 4 such input files in the input/ subdirectory.

* Logging is ALWAYS enabled and is appended to the file */tmp/robot.txt*. I didn't use */var/log/* since it requires write permissions which a normal user does not have. Also, syslog is an overkill here, but would certainly be the correct choice for production.

* Input is very lightly post-processed - leading and trailing spaces are removed and commands are upper-cased. No other processing is performed, which means that input should be given in a valid form - in uppercase and with correct type and order for the PLACE command.


Directory Structure
-------------------

All files needed to run this solution are located at the same directory. Test input files are located under the *input/* subdirectory. Unit tests are located inside tests_*.py files and will probably be omitted from a production package.


Design / Architecture considerations
------------------------------------

* I've used *classes* in Python, although support for them is not the same we have in other typed languages such as C# or Java. Even so, it helps organize code in a componantised and extensible manner although we end up simulating Interfaces/Abstract classes
  
* Registering commands (=components) was currently done in a manual fashion. It can be done dynamically, but I decided that was not relevant for the scope of this solution.

* TDD was used to develop this solution. Test commits are always followed by the implementations. There are two exceptions to this rule:
  * I personally like to declare the target implementation class before starting to write tests for it. This explains why a commit with tests also includes an empty class; and
  * After implementing the first Command, all the others were using basically the same "boiler-plated" code (aside from the actual logic) so the test commits include this boiler-plated code as well. I could have ommitted it from the commit, but I would have copy/pasted it later anyway and it didn't affect, in my opinion, the TDD practice and result.

* I've used some *Design Patterns* in the course of the development. Some examples:
  * Visitor - the **Register** function and calls.
  * Builder/Factory - the **Parser** class
  * Abstract - the **CommandBase** class
  * Command - the **CommandBase** derived classes

* Extending the solution with new commands is an simple as creating a new derived class from CommandBase and implementing it' interface. While we continue using manual detection of commands, the class should also call the *Register()* method of the CommandsParser factory.


How to run
----------

To run the solution you may issue the following command:

```
$ python main.py
```

to read input from the console or:

```
$ python main.py --c input/ex_a
```

to read it from the file ex_a located at the input/ direcory.


How to run tests
----------------

Tests can be run using the following command:

```
$ python -m unittest discover
```

from the solution's directory.
