#include <stdio.h>
#include <gmp.h>

int main() {
    int n;
    scanf("%d", &n);

    for (int i = 0; i < n; i++) {
        int k;
        scanf("%d", &k);
        int s = k / 2;

        mpz_t sum; 
        mpz_init(sum);
        mpz_set_ui(sum, 0); 

        for (int j = 1; j <= s; j++) {
            mpz_t term;
            mpz_init(term); 
            mpz_set_ui(term, j); 
            mpz_mul(term, term, term);
            mpz_mul_ui(term, term, 8); 
            mpz_add(sum, sum, term); 
            mpz_clear(term); 
        }

        gmp_printf("%Zd\n", sum); 
        mpz_clear(sum); 
    }

    return 0;
}