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
    if (b2 > b1) { // Zero length b
      return 0;
    } else {
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
  }

  if (a1 == a2) { // length 1
    int am = a1;
    int bm = (b1 + b2) / 2;
    int bl = (b2 - b1 + 1);
    bool b_odd =  bl % 2;
   
    if (a[am] <= b[bm]) {
      if (b_odd) {
	if ((bl == 1) || (a[am] > b[bm-1])) {
	  return (double) (a[am] + b[bm]) * 0.5;
	} else {
	  return (double) (b[bm-1] + b[bm]) * 0.5;
	}
      } else { // even
	return b[bm];
      }
    } else { // a[am] > b[bm]
      if (b_odd) {
	if (a[am] < b[bm + 1]) {
	  return (double) (a[am] + b[bm]) * 0.5;
	} else {
	  return (double) (b[bm] + b[bm + 1]) *0.5;
	}
      } else { // even
	if (a[am] < b[bm + 1]) {
	  return a[bm];
	} else {
	  return b[bm + 1];
	}
      }
    }
  } // len(a) = 1

  if (a2 == (a1+1)) { // two items left
    int am = a1;              // Left index
    int bm = (b1 + b2) / 2;   // Middle index (left)
    int bl = (b2 - b1 + 1);   // Number of b elements
    bool b_odd =  bl % 2;


    // Let's treat all possibilities
    // b odd

    // aa b bb  a[a2] < b[bm-1]

    // ab a bb  b[bm-1] < a[a2] < b[bm]
    // ba a bb
    
    // ab b ab  a[a1] < b[bm] < a[a2]
    // ba b ab

    // bb a ab  b[bm] < a[a1] < b[bm+1]

    // bb b aa  b[bm+1] < a[a1]
    
    // b even

    // aa bb bb a[a2] < b[bm-1]

    // ab ab bb a[a1] < b[bm] & a[a2] < b[bm+1]
    // ab ba bb
    // ba ab bb
    // ba ba bb

    // ab bb ab a[a1] < b[bm] & a[a2] > b[bm+1]
    // ba bb ab 
    // ab bb ba
    // ba bb ab
    
    // bb aa bb a[a1] > b[bm], a[a2] < b[bm+1]

    // bb ab ab a[a1] > b[bm], a[a2] > b[bm]
    // bb ab ba
    // bb ba ab
    // bb ba ba

    // bb bb aa a[a1] > b[bm+1]

    // |b| = 2
    // a ab b a[a2] < b[bm]

    // a ba b a[a1] < b[bm] & a[a2] < b[bm+1]
    // a ab b

    // a bb a a[a1] < b[bm] & a[a2] > b[bm+1]

    // b ab a a[a1] > b[bm]
    // b ba a

    // Printing
    std::cout
      << "a[" << a1 << "-" << a2 << "] "
      << "a(" << a[a1] << " " << a[a2] << ") "
      << "b[" << b1 << "-" << b2 << "] "
      << "b(";
    for(int i=b1;i<=b2;i++) {
      std::cout << b[i];
      if (i!=b2) std::cout << " ";
    }
    std::cout << ")" << std::endl;

    if (a[a1] <= b[bm]) { // <=
      
      if (b_odd) {        // Odd

	//  a a
	// b b b
	if (a[a2] < b[bm]) {
	  if (a[a2] > b[bm-1]) {
	    return a[a2];
	  } else {
	    return b[bm-1];
	  }
	} else {
	  return b[bm];
	}

      } else {            // Even

	//  a a
	// b b b b
	if (a[a2] <= b[bm]) {
	  if ((bl == 2) || (a[a2] > b[bm-1])) {
	    return (double) (b[bm] + a[a2]) * 0.5;
	  } else {
	    return (double) (b[bm] + b[bm-1]) * 0.5;
	  }
	} else {
	  if (a[a2] <= b[bm+1]) {
	    return (double) (b[bm] + a[a2]) * 0.5;
	  } else {
	    return (double) (b[bm] + b[bm+1]) * 0.5;
	  }
	}
      }
    } else {              // >
      
      if (b_odd) {        // Odd

	//    a a
	// b b b
	if (a[a1] <= b[bm+1]) {
	  return a[a1];
	} else {
	  return b[bm+1];
	} 

      } else {            // Even

	//    a a
	// b b b b
	if (a[a1] > b[bm+1]) {
	  if (bl == 2) {
	    if (a[a2] > b[bm+1]) {
	      return (double) (b[bm+1] + a[a1]) * 0.5;
	    } else {
	      return (double) (a[a1] + a[a2]) * 0.5;
	    }
	  } else {
	    if (a[a1] > b[bm+2]) {
	      return (double) (b[bm+1] + b[bm+2]) * 0.5;
	    } else {
	      if (a[a2] <= b[bm+1]) {
		return (double) (a[a1] + a[a2]) * 0.5;
	      } else {
		return (double) (a[a1] + b[bm+1]) * 0.5;
	      }
	    }
	  }
	} else {   // a[a1] <= b[bm+1]
	  if (a[a2] <= b[bm+1]) {
	    return (double) (a[a1] + a[a2]) * 0.5;
	  } else {
	    return (double) (a[a1] + b[bm+1]) * 0.5;
	  }
	}
      }
    }
  }

  int am = (a1 + a2) / 2;
  int bm = (b1 + b2) / 2;

  if (a[am] <= b[bm]) {
    std::cout
      << "(" << a1 << "," << a2 << "): "
      << "a[" << am << "]=" << a[am] << " <= "
      << "b[" << bm << "]=" << b[bm] << std::endl;
    if (a[am] > b[bm - 1]) {
      // Throw away a1 to (am-1)
      return findMedianSortedArrays(a, am, a2, b, b1, b2 - (am - a1));
    } else {
      // Throw away a1 to am
      return findMedianSortedArrays(a, am + 1, a2, b, b1, b2 - (am - a1 + 1));
    }
  } else {
    std::cout
      << "a[" << am << "]=" << a[am] << " > "
      << "b[" << bm << "]=" << b[bm] << std::endl;
    if (a[am] < b[bm + 1]) {
      // Throw away am+1 to a2
      return findMedianSortedArrays(a, a1, am, b, b1 + (a2 - am), b2);
    } else {
      // Throw away am to a2
      return findMedianSortedArrays(a, a1, am - 1, b, b1 + (a2 - am + 1), b2);
    }
  }
  return -1;
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
