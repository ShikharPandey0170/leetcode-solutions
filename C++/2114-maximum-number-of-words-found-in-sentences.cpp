// LeetCode 2114: Maximum Number of Words Found in Sentences
// Difficulty: Easy
// Topic: Array
// Link: https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/

class Solution {
public:
    int mostWordsFound(vector<string>& sentences) {
        int maxword=0;
        for (string i: sentences){
            int words=0;
            for(int j=0;j<i.size();j++){
            if (i[j]==' ')
                    words++;
            }
            if (maxword<words+1)
                    maxword=words+1;
        }
        return maxword;
    }
};