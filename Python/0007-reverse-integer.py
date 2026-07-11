class Solution:
    def reverse(self, x: int) -> int:
        if (str(x)[::-1])[-1]=='-':
            x=int('-'+(str(x)[::-1])[:-1])
        else:
            x=int(str(x)[::-1])
        if -2_147_483_648 <= x <= 2_147_483_647:
            return x
        else:
            x=0
            return x
        