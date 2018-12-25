class Solution:
    def select_max_pal(self, new_max_pal, old_max_pal):
        if len(new_max_pal) >= len(old_max_pal):
            return new_max_pal
        else:
            return old_max_pal

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s
        max_pal = s[0]
        for idx in range(len(s)):
            print('o')
            for jdx in range(1, len(s) // 2 + 1):
                print('o', idx - jdx, idx + jdx)
                if idx - jdx < 0 or idx + jdx >= len(s):
                    break
                elif s[idx - jdx] == s[idx + jdx]:
                    print('yes')
                    max_pal = self.select_max_pal(
                        s[idx - jdx:idx + jdx + 1], max_pal)
                else:
                    print('no')
                    break

        for idx in range(len(s)):
            if idx + 1 < len(s) and s[idx] == s[idx + 1]:
                for jdx in range(0, len(s) // 2 + 1):
                    print('e', idx - jdx, idx + jdx + 1)
                    if idx - jdx < 0 or idx + 1 + jdx >= len(s):
                        break
                    elif s[idx - jdx] == s[idx + 1 + jdx]:
                        print('yes')
                        max_pal = self.select_max_pal(
                            s[idx - jdx:idx + 2 + jdx], max_pal)
                    else:
                        print('no')
                        break
        return max_pal

