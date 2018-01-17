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

  // Printing
  
  // std::cout
  //   << "a[" << a1 << "-" << a2 << "] "
  //   << "a(";
  // for(int i=a1;i<=a2;i++) {
  //   std::cout << a[i];
  //   if (i!=a2) std::cout << " ";
  // }
  // std::cout << ")" << std::endl;
  // std::cout
  //   << "b[" << b1 << "-" << b2 << "] "
  //   << "b(";
  // for(int i=b1;i<=b2;i++) {
  //   std::cout << b[i];
  //   if (i!=b2) std::cout << " ";
  // }
  // std::cout << ")" << std::endl;

  
  if (a1 > a2) { // Zero length a
    if (b1 > b2) { // Zero length b
      return 0;
    } else {
      if (b2 == b1) return b[b1];
	
      double ans = ((b2-b1+1) % 2 == 0) ?
	(double) (b[(b1+b2)/2] + b[(b1+b2)/2+1]) * 0.5 :
	b[(b1+b2)/2];
    
      // std::cout << std::setfill('-') << std::setw(69) << "-"<< std::endl;
      // for (int i=b1; i<=b2; i++) {
      // 	std::cout << b[i] << " ";
      // }
      // std::cout << ": " << ans;
      // std::cout << std::endl;
      
      return ans;
    }
  }

  if (a1 == a2) { // length 1
    
    // std::cout << "|a| = 1 :" << std::endl;
    
    int am = a1;
    int bm = (b1 + b2) / 2;
    int bl = (b2 - b1 + 1);
    bool b_odd =  bl % 2;

    // b odd
    // abbb a[a1] < b[bm-1]
    
    // babb b[bm-1] < a[a1] < b[bm+1]
    // bbab

    // bbba else

    if (bl==1) {
      return double (b[bm] + a[a1]) * 0.5;
    }
    
    if (b_odd) {
      
      // std::cout << "b odd" << std::endl;
      
      if (a[a1] <= b[bm-1]) {
	return (b[bm-1]+b[bm]) * 0.5;
      }

      if (a[a1] <= b[bm+1]) {
	return (b[bm] + a[a1]) * 0.5;
      }

      return (b[bm] + b[bm+1]) * 0.5;
    }

    // std::cout << "b even" << std::endl;

    // abb
    // bab
    // bba
    if (a[a1] < b[bm]) {
      return b[bm];
    }

    if (a[a1] < b[bm+1]) {
      return a[a1];
    }

    return b[bm+1];
    
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

    // ab bb ab a[a1] < b[bm], a[a2] > b[bm+1]
    // ba bb ab
    // ab bb ba
    // ba bb ba
    
    // bb bb aa a[a1] > b[bm+1]

    // |b| = 2
    // a ba b a[a2] < b[bm+1]
    // a ab b

    // a bb a a[a1] < b[bm] & a[a2] > b[bm+1]

    // b ab a a[a1] > b[bm]
    // b ba a

    if (bl==2) {
      
      // std::cout << "|bl| = 2 :";
      
      if (a[a2] <= b[bm+1]) {
	if (a[a1] < b[bm]) {
	  // a ab b
	  return (double) (a[a2] + b[bm]) * 0.5;
	} else {
	  // b aa b
	  return (double) (a[a1] + a[a2]) * 0.5;
	}
      }

      // a[a2] > b[bm+1]
      if (a[a1] < b[bm]) {
	// abba
	return (double) (b[bm]+b[bm+1])*0.5;
      } else {
	// baba
	return (double) (a[a1]+b[bm+1])*0.5;
      }
    }

    if (b_odd) {
      
      // std::cout << "b odd" << std::endl;

      if (a[a2] < b[bm-1]) {
	return b[bm-1];
      }

      if (a[a2] <= b[bm]) {
	return a[a2];
      }

      if (a[a2] <= b[bm+1]) {
	if (a[a1] <= b[bm]) {
	  return b[bm];
	} else {
	  return a[a1];
	}
      }

      // a[a2] > b[bm+1]
      if (a[a1] <= b[bm]) {
	return b[bm];
      }

      if (a[a1] <= b[bm+1]) {
	return a[a1];
      }
      
      return b[bm+1];

    } // b_odd

    // b is even

    // std::cout << "b even" << std::endl;
            
    if (a[a2] <= b[bm-1]) {
      // aa bb bb
      return (double) (b[bm-1] + b[bm]) * 0.5;
    }

    if (a[a2] <= b[bm+1]) {
      if (a[a1] <= b[bm]) {
	// (ab) (ab) bb
	return (double) (a[a2] + b[bm]) * 0.5;
      } else {
	// bb aa bb
	return (double) (a[a1] + a[a2]) * 0.5;
      }
    }

    // a[a2] > b[bm+1]
    if (a[a1] <= b[bm]) {
      // (ab) bb (ab)
      return (double) (b[bm] + b[bm+1]) * 0.5;
    }
    
    if (a[a1] <= b[bm+2]) {
      // bb (ab) (ab)
      return (double) (a[a1] + b[bm+1]) * 0.5;
    }

    // a[a1] > b[bm+2]
    return (double) (b[bm+1]+b[bm+2]) * 0.5;
  }

  int am = (a1 + a2) / 2;
  int bm = (b1 + b2) / 2;
  int bl = (b2 - b1) + 1;
  int al = (a2 - a1) + 1;
  bool b_odd = bl % 2;
  
  if (a[am] <= b[bm]) {

    
    // std::cout
    //   << "(" << a1 << "," << a2 << "): "
    //   << "a[" << am << "]=" << a[am] << " <= "
    //   << "b[" << bm << "]=" << b[bm] << std::endl;
    
    if (a[am] > b[bm - 1]) {
      // Throw away a1 to (am-1)
      return findMedianSortedArrays(a, am, a2, b, b1, b2 - (am - a1));
    } else {
      if (a[am + 1] > b[bm]) {
	// Throw away a1 to (am-1)
	return findMedianSortedArrays(a, am, a2, b, b1, b2 - (am - a1));
      } else {
	// Throw away a1 to am
	return findMedianSortedArrays(a, am + 1, a2, b, b1, b2 - (am - a1 + 1));
      }
    }

  } else { // a[am] > b[bm]

    // std::cout
    //   << "a[" << am << "]=" << a[am] << " > "
    //   << "b[" << bm << "]=" << b[bm] << std::endl;

    if (a[am+1] > b[bm+1]) {
      // Throw away am+1 to a2
      return findMedianSortedArrays(a, a1, am, b, b1 + (a2 - am), b2);
    } else {
      if (al == 3) {
	if (b_odd) {
	  if (a[a1] < b[bm]) {
	    // (ab) ba ba
	    return (double) (b[bm]+a[am]) * 0.5;
	  } else {
	    // bb aa ba
	    return (double) (a[a1]+a[am]) * 0.5;
	  }
	} else { 	// b_even
	  // (abb) a b(ab)
	  return a[am];
	}
      } else {
	// Throw away am+2 to a2
	return findMedianSortedArrays(a, a1, am + 1, b, b1 + (a2 - (am + 2) + 1), b2);
      }
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
