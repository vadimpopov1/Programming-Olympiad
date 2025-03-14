#include <stdio.h>

int main() {
    char str[201];
    fgets(str, 201, stdin);
    for (int i = 0; str[i] != '\n'; i++) {
        if (str[i] == '.') {
            printf("0");
        }else if (str[i] == '-' && str[i + 1] == '.') {
            printf("1");
            i++;
        }else if (str[i] == '-' && str[i + 1] != '-') {
            printf("2");
            i++;
        }
    }
}