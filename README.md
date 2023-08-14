# c2py
Code translation from C to Python Programming Language

### Directory Structure
```
.
├── LICENSE
├── README.md
├── test
│   ├── 1
│   │   ├── CCode
│   │   │   └── main.c
│   │   ├── input.txt
│   │   ├── output.txt
│   │   ├── res.txt
│   │   └── translation
│   │       └── main.py
│   └── 2
│       ├── CCode
│       │   └── main.c
│       ├── input.txt
│       ├── output.txt
│       ├── res.txt
│       └── translation
│           └── main.py
├── test.py
└── translator.py
```

### Testing
```
python3 test.py

Output:
TEST 1
TEST 2
2 out of 2 tests passed.
Accuracy is 100.0%.
```

### Requirements
```
Python3
GCC
```

### Code Style support
```
The long term goal is to support google c++ style guide.
For now these are the sytles that are supported.
```

#### Header file inclusions
1. No support for now, except for basic IO libs.
2. All header files should be done at the top of the file.

#### ```#``` define
1. No support for now.
2. Longterm support for preprocessor, so that all these
are take will be taken care.

#### Function definition support
1. Any function used apart from main has to have 
function declaration
2. Only below declaration type supported
``` 
    <type> <function_name>(<arg1>, <arg2>, ..) {
        // Code
    }
```  

#### While loop support
1. Only below declaration is supported
```
    while(<statement>) {
        // Code
    }
```

#### For loop support
1. Only below decalarations are supported
```
    for(<expression>; <expression>; <expression>) {
        // Code
    }
```
#### Types
1. int (all types) X
2. string literal X
3. array X
4. enum X
5. pointers X
6. float (all types) X
7. void X
8. user defined structures X
9. const X
10. char

#### Expressions
1. = X
2. == X
3. * (pointer) X
4. * (multiplication) X
5. & (address of) X
6. <> X
7. e1, e2 :operator: e3 (compount expression) X
8. |, &, ||, &&, ^, <<, >>, ~ (bitwise operators) X

#### Function support

##### Basic IO
1. scanf(string, a1, a2, ..)
2. printf(string, a1, a2, ..)

#### Memory Related
1. malloc
2. memset
3. sizeof

### Documents
https://google.github.io/styleguide/cppguide.html
