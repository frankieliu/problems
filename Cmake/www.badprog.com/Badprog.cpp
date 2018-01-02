#include <iostream>
#include "Badprog.h"

using namespace std;

Badprog::Badprog() {
  cout << "Constructor" << endl;
}

int main(int argc, char *argv[]) {
  Badprog b;
  return 0;
}
