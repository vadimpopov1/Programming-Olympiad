#include <stdio.h>
#include <stdlib.h>

int main() {
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; i++) {
        char s[3][11];
        for (int j = 0; j < 3; j++) {
            scanf("%s", s[j]);
        }
        printf("%c%c%c", s[0][0], s[1][0], s[2][0]);
    }
    return 0;
}