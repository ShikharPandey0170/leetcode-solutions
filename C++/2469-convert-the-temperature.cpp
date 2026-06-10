// LeetCode 2469: Convert the Temperature
// Difficulty: Easy
// Topic: Math
// Link: https://leetcode.com/problems/convert-the-temperature/

class Solution {
public:
    vector<double> convertTemperature(double celsius) {
        vector<double> l={celsius+273.15,celsius*1.80+32.00};
        return l;
    }
};