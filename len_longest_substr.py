class Solution:
    def replace_curr_letters(self, curr_letters, let):
        idx = curr_letters.index(let)
        return '{}{}'.format(curr_letters[idx + 1:], let)

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        curr_letters = ''
        max_len = 0
        curr_len = 0

        for let in s:
            if let in curr_letters:
                curr_letters = self.replace_curr_letters(curr_letters, let)
                print(curr_letters, len(curr_letters))
                max_len = max(max_len, curr_len, len(curr_letters))
                curr_len = len(curr_letters)
            else:
                curr_letters = '{}{}'.format(curr_letters, let)
                curr_len += 1
            print(let, 'cl', curr_len, max_len)
        return max(max_len, curr_len)



