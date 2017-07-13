#include <stdio.h>

int main(void)
{
    int n;
    int k;
    int a[100000];
    int p[100000];

    int i;
    int tmp;
    int max_index;

    scanf("%d %d", &n, &k);

    for (i = 0; i < n; i++) {
        scanf("%d", &a[i]);
    }

    for (i = 0; i < n; i++) {
        p[a[i]] = i;
    }

    for (i = 0; i < n; i++) {
        if (k == 0) break;

        if (a[i] == (n - i)) continue;

        max_index = p[n - i];
        p[n - i] = i;
        p[a[i]] = max_index;

        tmp = a[i];
        a[i] = a[max_index];
        a[max_index] = tmp;

        k -= 1;
    }

    for (i = 0; i < n; i++) {
        printf("%d ", a[i]);
    }
    printf("\n");

    return 0;
}
