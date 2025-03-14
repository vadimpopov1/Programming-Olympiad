#include <stdio.h>  
#include <stdlib.h>  

int main() {
    int k;
    scanf("%d", &k);
    char *a = (char *)malloc(k * sizeof(char));

    scanf("%s", a);
    
    int r = k - 1;
    int l = 0;
    int len = k;
    while(l < r) {
        if (a[l] == a[r] || len == 0){
            break;
        }
        len -= 2;
        r--;
        l++;
    } 
    printf("%d\n", len);
}   