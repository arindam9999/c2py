test1 = ["#include <stdio.h>\n"]
res1  = ["#include <stdio.h>"]

test2 = ['#include <stdio.h>\n', 
        '\n', 
        'void preproces() {\n', 
        '    freopen("output.txt", "w", stdout);\n', 
        '    freopen("input.txt", "r", stdin);\n', 
        '}\n', 
        '\n', 
        'int main() {\n', 
        '    preproces();\n', 
        '   // printf() displays the string inside quotation\n', 
        '   printf("Hello, World!\\n");\n', '   return 0;\n', 
        '}\n', 
        '\n']
res2  = ['#include <stdio.h>', 
         ' ', 
         'void preproces() {', 
         'freopen("output.txt", "w", stdout);', 
         'freopen("input.txt", "r", stdin);', '}', 
         ' ', 
         'int main() {', 
         'preproces();', 
         '// printf() displays the string inside quotation', 
         'printf("Hello, World!\\n");', 
         'return 0;', '}', 
         ' ']

test3 = ['while(b=c){\n', 
         '    // Do this\n', 
         '    c = a + b;\n', 
         '}']
res3  = ['while(b=c){', 
         '// Do this', 
         'c = a + b;', 
         '}']

test4 = ['while (false) {\n', 
         '    // Do this\n', 
         '    int c = 0, a = 0, d = 0, b = 0;\n', 
         '    c = a, d = b;\n', 
         '}']
res4  = ['while (false) {', 
         '// Do this', 
         'int c = 0, a = 0, d = 0, b = 0;', 
         'c = a, d = b;', 
         '}']

test5 = ['int foo(int a1, int a2, int * a3) {\n', 
         '    //Check this\n', 
         '    a2 = a1;\n', 
         '    int c = a2;\n', 
         '    return a1 + a2;\n', 
         '}']
res5  = ['int foo(int a1, int a2, int * a3) {', 
         '//Check this', 
         'a2 = a1;', 
         'int c = a2;', 
         'return a1 + a2;', 
         '}']

test6 = ['for(int i = 0; i < n; i++){\n', 
        '\t// Do this\n', 
        '\ti++;\n', 
        '}\n']
res6  = ['for(int i = 0; i < n; i++){', 
         '// Do this', 
         'i++;', 
         '}']


tests = []
tests.append([test1, res1])
tests.append([test2, res2])
tests.append([test3, res3])
tests.append([test4, res4])
tests.append([test5, res5])
tests.append([test6, res6])