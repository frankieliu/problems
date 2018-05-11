class Solution {
public:
    int removeDuplicates(vector<int>& nums) {

        if (nums.size() == 0){ return 0; }
        int si = 0; // save index
        int len = 1;

        for(int i = 1; i < nums.size(); i++){
            if (nums[si] != nums[i]) {
                nums[++si] = nums[i];
                len++;
            }
        }
        return len;
    }
};
