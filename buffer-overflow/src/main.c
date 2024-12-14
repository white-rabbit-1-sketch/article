#include <stdio.h>
#include <string.h>

void vulnerable_function() {
    char buffer[10];
    printf("Enter input: ");
    gets(buffer);
    printf("Buffer content: %s\n", buffer);
}

int main() {
    vulnerable_function();

    return 0;
}