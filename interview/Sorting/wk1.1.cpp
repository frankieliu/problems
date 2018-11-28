#include <iostream>

using namespace std;

int pivot(int a[], int left, int right) {
    return right;
}

void swap(int *a, int *b) {
    int c = *a;
    *a = *b;
    *b = c;
}

int partition(int *a, int left, int right, int pi) {
    // put pivot to the right
    swap(&a[pi], &a[right]);

    int li = left-1;              // right-most pointer index for lesser set
    int v = a[right];
    for (int i = left; i <= right-1; ++i) {
        if (a[i] <= v) {          // if found a lesser number
            li++;                 // move lesser pointer up
            swap(&a[li], &a[i]);  // put this number in that position
        }
    }
    // swap the pivot
    li++;
    swap(&a[li], &a[right]);
    return li;
}

void qs(int a[], int left, int right) {
    if (left >= right) return;
    int pi = pivot(a, left, right);
    pi = partition(a, left, right, pi);
    if (pi > 0) qs(a, left, pi-1);
    if (pi < right-1) qs(a, pi+1, right);
}

int main() {
    int a[] = {3,2,1,5,4,3,2,1};
    int N = sizeof(a)/sizeof(int);
    qs(a, 0, N-1);
    for (int i = 0; i < N; ++i) {
        cout << a[i] << endl;
    }
}
