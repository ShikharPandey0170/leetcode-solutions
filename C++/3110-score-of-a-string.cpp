// LeetCode 3110: Score of a String
// Difficulty: Easy
// Topic: String
// Link: https://leetcode.com/problems/score-of-a-string/

class Solution {
public:
    int scoreOfString(string s) {
        int ans=0;
        for (int i=0;i<s.size()-1;i++){
            char x=s[i];
            char y=s[i+1];
            ans+= x>y?(x-y):(y-x);
        }
        return ans;
    }
};