#include <iostream>
#include <vector>
#include <random>
#include <algorithm>
#include <assert.h>

#include "median.hpp"

void vector_print(std::vector<int>& a);


bool main2();
bool main3();  // test null
int main(int argc, char** argv) {
  if (false) {
    bool ans = true;
    while (ans) {
      ans = main2();
    }
  }
  if (true) {
    main3();
  }
}

bool main3() {
  std::vector<int> nums1(1,2);
  std::vector<int> nums2(0);
  Solution s;
  double median = s.findMedianSortedArrays(nums1, nums2);
  std::cout << "median: " << median << std::endl;
}

bool main2() {

  std::random_device rd;   // Random device
  std::mt19937 rng(rd());  // Random engine
  std::uniform_int_distribution<int> uni(1,100);
  std::uniform_int_distribution<int> uni_size(1,10);

  int s1 = uni_size(rng);
  int s2 = uni_size(rng);

  std::vector<int> nums1(s1);
  std::vector<int> nums2(s2);
  
  for (int i=0; i<s1; i++) {
    nums1[i] = (int) uni(rng);
  }
  for (int i=0; i<s2; i++) {
    nums2[i] = (int) uni(rng);
  }

  std::sort(nums1.begin(), nums1.end());
  std::sort(nums2.begin(), nums2.end());

  // vector_print(nums1);
  // vector_print(nums2);
  
  std::vector<int> combine;
  combine.insert( combine.end(), nums1.begin(), nums1.end() );
  combine.insert( combine.end(), nums2.begin(), nums2.end() );
  std::sort(combine.begin(), combine.end());

  // vector_print(combine);
  
  double median = (double) combine[combine.size()/2];
  if(combine.size()/2*2 == combine.size()) {
    // std::cout << "Is even" << std::endl;
    median = (double) (median + combine[combine.size()/2-1]) * 0.5;
  }
  // std::cout << "median: " << median << std::endl;

  Solution s;
  double median2 = s.findMedianSortedArrays(nums1, nums2);
  // std::cout << "median2: " << median2 << std::endl;
  // assert( median == median2 );
  if (median != median2) {
    vector_print(nums1);
    vector_print(nums2);
    vector_print(combine);
    std::cout << "median: " << median << ", median2: " << median2 << std::endl;
  }
  return median == median2;
}

void vector_print(std::vector<int>& a) {
  for(auto it = a.begin(); it != a.end(); it++) {
    std::cout << *it << " ";
  }
  std::cout << std::endl;
}
