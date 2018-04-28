// http://www.eriksmistad.no/getting-started-with-google-test-on-ubuntu
//
// Installing libgtest
// 1. sudo apt-get install libgtest-dev
// 2. sudo apt-get install cmake # install cmake
// 3. cd /usr/src/gtest
// 4. sudo cmake CMakeLists.txt
// 5. sudo make
// 6. sudo cp *.a /usr/lib
//
// Using it:
// 1. write tests.cpp
// 2. write CMakeLists.txt
// 3. cmake CMakeLists.txt
// 4. make
// 5. ./runTests

// whattotest.cpp
#include <math.h>
 
double squareRoot(const double a) {
    double b = sqrt(a);
    if(b != b) { // nan check
        return -1.0;
    }else{
        return sqrt(a);
    }
}
