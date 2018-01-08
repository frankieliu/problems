#include <iostream>
#include <iomanip>
#include <vector>
#include "median.hpp"


// Make sure that a is smaller than b
double Solution::findMedianSortedArrays
(
 std::vector<int>& a,
 int a1, int a2,
 std::vector<int>& b,
 int b1, int b2
 ) {

  if (a1 > a2) { // Zero length a
    double ans = ((b2-b1) % 2 == 0) ?
      (b[(b1+b2)/2] + b[(b1+b2)/2+1] * 0.5) :
      b[(b1+b2)/2];
    
    std::cout << std::setfill('-') << std::setw(69) << "-"<< std::endl;
    for (int i=b1; i<=b2; i++) {
      std::cout << b[i] << " ";
    }
    std::cout << ": " << ans;
    std::cout << std::endl;
    return ans;
  }

  // Index at the middle (left of mid if even)
  int am = (a1 + a2) / 2;
  int bm = (b1 + b2) / 2;
  
  std::cout << std::setfill('-') << std::setw(69) << "-"<< std::endl;
  for (int i=a1; i<=a2; i++) {
    std::cout << a[i] << " ";
  }
  std::cout << ": " << a[am];
  std::cout << std::endl;
  for (int i=b1; i<=b2; i++) {
    std::cout << b[i] << " ";
  }
  std::cout << ": " << b[bm];
  std::cout << std::endl;
  
  // std::cout << std::setfill('-') << std::setw(69) << "-"<< std::endl;

  if (a[am] == b[bm]) {
    //    52 56
    // 46 52 61 70
    std::cout << "Mids match/";
    if ((a2-a1+1) % 2 == 0) {
      std::cout << "A even/";
    } else {
      std::cout << "A odd/";
    }
  } else {

    if(a[am] < b[bm]) {
      
      std::cout << "</";
      if (a1 == a2) {
	std::cout << "Same/" ;
	// 10
	// 0 20 30 40
	if ((b2-b1+1) % 2 == 0) {
	  std::cout << "Even/";
	  return b[bm];
	} else {
	  std::cout << "Odd/";
	  if (a[am] > b[bm-1]) {
	    return (b[bm] + a[am])*0.5;
	  } else {
	    return (b[bm-1] + b[bm])*0.5;
	  }
	}
      } else if (a1 == (a2-1)) {
	std::cout << "2 Left/";
	if ((b2-b1+1) % 2 == 0) {
	  //    10 xx
	  // 38 46 66 69
	  std::cout << "Even/";
	  return findMedianSortedArrays(a, am + 1, a2, b, b1, b2 - (am - a1 + 1));
	} else {
	  //    10 xx
	  //  4  16  8
	  std::cout << "Odd/";
	  if (a[a2] > b[bm]) {
	    return b[bm];
	  } else {
	    return a[a2];
	  }
	}
      } else {
	std::cout << "Not Same/";
	return findMedianSortedArrays(a, am, a2, b, b1, b2 - (am-a1));
      }
      
    } else {
      std::cout << ">/";
      if (a1 == a2) {
	// 25
	// 0 20 30 40
	std::cout << "Same/";
	if ((b2-b1+1) % 2 == 0) {
	  std::cout << "Even/";
	  return a[am];
	} else {
	  // 60
	  // 32 42 43 51 58 : 43
	  std::cout << "Odd/";
	  if (a[am] > b[bm+1]) {
	    return (b[bm] + b[bm+1])*0.5;
	  } else {
	    return (b[bm] + a[am])*0.5;
	  }
	}
      }  else if (a1 == a2-1) {
	std::cout << "2/";
	if ((b2-b1+1) % 2 == 0) {
	  std::cout << "Even/";
	  // 56 77 : 56
          // 47 47 80 99 : 47
	  if (a[a2] < b[bm+1]) {
	    return (a[a1] + a[a2])*0.5;
	  } else {
	    return findMedianSortedArrays(a, a1, am, b, b1 + (a2-am), b2);
	  }
	} else {
	  std::cout << "Odd/";
	  // 56 77 : 56
          // 47 47 47 99 100: 47
	  return findMedianSortedArrays(a, a1, am, b, b1 + (a2-am), b2);
	}
      } else {
	std::cout << "Not Same/";
	return findMedianSortedArrays(a, a1, am, b, b1 + (a2-am), b2);
      }
    }
  }
}
					
double Solution::findMedianSortedArrays(std::vector<int>& nums1, std::vector<int>& nums2) {
  int n1s = nums1.size();
  int n2s = nums2.size();
  if (n1s <= n2s) {
    return Solution::findMedianSortedArrays
      (nums1, 0, n1s - 1, nums2, 0, n2s - 1);
  } else {
    return Solution::findMedianSortedArrays
      (nums2, 0, n2s - 1, nums1, 0, n1s - 1);
  }
}
