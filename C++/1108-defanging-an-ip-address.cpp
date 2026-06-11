// LeetCode 1108: Defanging an IP Address
// Difficulty: Easy
// Topic: String
// Link: https://leetcode.com/problems/defanging-an-ip-address/

/Second Attempt
class Solution {
public:
    string defangIPaddr(string address) {
        string result;
        for(char c: address){
            if(c=='.'){result+="[.]";}
            else{result+=string(1,c);}
        }   
        return result;
    }
};

/First Attempt
"""
class Solution {
public:
    string defangIPaddr(string address) {
        int len=address.size();
        char* result=(char*)malloc(len+10);
        int i=0,j=0;

        while (address[i]!='\0'){
            if (address[i]=='.'){
                result[j++]='[';
                result[j++]='.';
                result[j++]=']';
            } else{
                result[j++]=address[i];
            }
            i++;
        }   
        result[j]='\0';
        return result;
    }
};
"""