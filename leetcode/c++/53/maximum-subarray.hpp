class Solution {
public:
    
    int maxSubArray(vector<int>& nums) {
        if (nums.size()==0) return 0;
        if (nums.size()==1) return nums[0];
        int cur_max = nums[0];
        int prev_max = nums[0];
        for (auto i = 1; i < nums.size(); i++) {
            if ((prev_max + nums[i]) < nums[i]) {
                prev_max = nums[i];
            } else {
                prev_max += nums[i];
            }
            if (prev_max > cur_max) {
                cur_max = prev_max;
            }
            cout << cur_max << endl;
        }
        return cur_max;
    }
};
