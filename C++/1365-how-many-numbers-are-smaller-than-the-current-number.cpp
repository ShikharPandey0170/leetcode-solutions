// LeetCode 1365: How Many Numbers Are Smaller Than the Current Number
// Difficulty: Easy
// Topic: Array
// Link: https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        vector<int> ans;
        for(int i: nums){
            int count=0;
            for(int j=0;j<nums.size();j++){
                if(nums[j]<i){count+=1;}
            }
            ans.push_back(count);
        }
        return ans;
    }
};