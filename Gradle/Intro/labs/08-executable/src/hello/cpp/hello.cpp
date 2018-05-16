#include <iostream>

int main () {
  std::cout << "Hello, World!\n";
  #ifdef EXTRA_CHEERY
    std::cout << "What a fabulous day!\n";
  #endif
  return 0;
}
