class Solution {
public:
    int numFriendRequests(vector<int>& ages) {
        int request = 0;

        // Reversing the relationship
        // y > x >= 0.5y + 7

        vector<int> bges(171,0);

        // fill in array
        for(auto a : ages) {
            if (a <= 185) {
                bges[a-15]++;
            }
        }

        // compute
        
            
    }
    int numFriendRequests0(vector<int>& ages) {
        int request = 0;
        // sort(ages.begin(),ages.end());

        for(int i=0; i < ages.size(); i++) {
            for(int j=i+1; j < ages.size(); j++) {
                if (!((ages[i] <= 0.5 * ages[j] + 7) ||
                      (ages[i] > ages[j]) ||
                      ((ages[i] > 100) && (ages[j] < 100))))
                    request++;
                if (!((ages[j] <= 0.5 * ages[i] + 7) ||
                      (ages[j] > ages[i]) ||
                      ((ages[j] > 100) && (ages[i] < 100))))
                    request++;
            }
        }
        return request;
    }
};
