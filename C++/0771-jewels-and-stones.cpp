// LeetCode 0771: Jewels and Stones
// Difficulty: Easy
// Topic: String
// Link: https://leetcode.com/problems/jewels-and-stones/

class Solution {
public:
    int numJewelsInStones(string jewels, string stones) {
        int count=0;
        for(auto i:jewels){
            for(auto j:stones){
                if(i==j){count+=1;}
            }
        }
        return count;
    }
};