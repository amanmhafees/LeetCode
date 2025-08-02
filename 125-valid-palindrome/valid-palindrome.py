class Solution(object):
    
    def isPalindrome(self, s):
        com_string=self.extract_alphabet(s)
        length_s=len(com_string)
        # if(length_s==0):
        #     return True
        # for i in range(length_s/2):
        #     if com_string[i] !=com_string[length_s-i-1]:
        #         return False
        # return True
        return com_string==com_string[::-1]
    def extract_alphabet(self,s):
        new_string=""
        for i in s:
            if i.isalnum():
                new_string+=i.lower()
        return new_string
        """
        :type s: str
        :rtype: bool
        """
        