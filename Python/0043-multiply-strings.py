class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        str1,str2=0,0
        for i in num1:
            str1=str1*10+int(i)
        for j in num2:
            str2=str2*10+int(j)
        str3=str(str1*str2)
        return str3
            
      
        