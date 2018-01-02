#include <iostream>
#include <iterator>
#include <vector>

/* rand example: guess the number */
#include <stdio.h>      /* printf, scanf, puts, NULL */
#include <stdlib.h>     /* srand, rand */
#include <time.h>       /* time */

#include "heap.hpp"

int randrange(int low,int high);

int main(int argc, char** argv) {
  /* initialize random seed: */
  srand (time(NULL));

  int num = 100;
  int a[100];

  for (int i; i<num; i++) {
    a[i] = randrange(1,1000);
  }
    
  // std::cout << "Init: " << sizeof(a) << " " << sizeof(a[0]) << std::endl;
  MinHeap h(&a[0], sizeof(a)/sizeof(a[0]));
  // h.Print();
  // h.TreePrint();

  // Heap sort and sort is correct
  bool error = false;
  std::vector<int> sorted = h.Sort();

  bool printSorted = false;
  int prev = sorted[0];
  for(auto it=sorted.begin(); it != sorted.end(); it++) {
    if (printSorted) 
      std::cout << *it << " ";
    if (prev > *it) {
      if (printSorted)
	std::cout << "<< ERROR " ;
      error = true;
    }
  }
  if (printSorted)
    std::cout << std::endl;
  if (error) {
    std::cout << "There was an error..." << std::endl;
  }
}

int randrange(int low,int high)
{
    return rand()%(high-low+1)+low;     
}

