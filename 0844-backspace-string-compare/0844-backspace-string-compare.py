class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        string = []
        for i in range(len(s)):
            if s[i] == "#":
                if string:
                    string.pop()
            else:
                string.append(s[i])
        sec_string = []

        for j in range(len(t)):
            if t[j] == "#":
                if sec_string:
                    sec_string.pop()
            else:
                sec_string.append(t[j])

        return string == sec_string

        