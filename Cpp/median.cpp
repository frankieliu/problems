#include <iostream>
#include <vector>

using namespace std;
class Solution {
public:
  double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
    cout << nums1.size() << "\n";
    return 0.0;
  }
};

int main(int argc, char** argv) {
  Solution s;
  vector<int> nums1 = {1,2,3,4,5,6,7};
  vector<int> nums2 = {3,4,5,6,7,8,9};
  cout << s.findMedianSortedArrays(nums1, nums2) << endl;
}
