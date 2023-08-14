#include <stdio.h>

void preproces() {
    freopen("output.txt", "w", stdout);
    freopen("input.txt", "r", stdin);
}

int main() {
    preproces();
   // printf() displays the string inside quotation
   printf("Hello, World!\n");
   return 0;
}