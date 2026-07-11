class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> answer;
        int product=1;
        int count=0;
        for(int i: nums){
            if (i!=0){
                product*=i;
            } else{
            count++;}
        }
        for(int i=0;i<nums.size();i++){
            if (count>1){answer.push_back(0);}
            else if (count==1){
                if (nums[i]==0){answer.push_back(product);}
                else {answer.push_back(0);}
            }
            else {answer.push_back(product/nums[i]);}
        }
        return answer;
    }
};