#if !(defined (MEDIAN_H_INCLUDED))
#define MEDIAN_H_INCLUDED

#include <vector>

class Solution {
public:
  double findMedianSortedArrays
  (
   std::vector<int>& a,
   int a1, int a2,
   std::vector<int>& b,
   int b1, int b2
   );
  double findMedianSortedArrays(std::vector<int>& nums1, std::vector<int>& nums2);
};

#endif
