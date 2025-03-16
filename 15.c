#include <stdio.h>

int main() {
    int k;
    scanf("%d", &k);

    for (int i = 0; i < k; i++) { 
        int n;
        scanf("%d", &n);
        char a[n + 1];
        scanf("%s", a);

        int op = 0;
        int cl = 0;
        int res = 0;

        for (int q = 0; q < n; q++) {
            if (a[q] == '(') {
                op++;
            } else {
                cl++;
            }

            if (cl > op) {
                res++;
                op = 0;
                cl = 0;
            }
        }

        if (op > cl) {
            res += op - cl;
        }

        printf("%d\n", res / 2);
    }
    return 0;
}