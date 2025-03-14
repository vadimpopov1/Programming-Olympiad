#include <stdio.h>  
#include <stdlib.h>  

int main() {
    int k;
    scanf("%d", &k);
    for (int c = 0; c < k; c++) {
    char m[8][8];

    for (int i = 0; i < 8; i++) {
        for (int j = 0; j < 8; j++) {
            scanf(" %c/0", &m[i][j]);
        }
    }

    for (int i = 0; i < 8; i++) {
        for (int j = 0; j < 8; j++) {
            if (m[i][j] != '.') {
                printf("%c", m[i][j]);
            }
        }
    }
    printf("\n");
    }
}