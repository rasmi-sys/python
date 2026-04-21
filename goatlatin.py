class Solution(object):
    def toGoatLatin(self, sentence):
        vowels={'a', 'e', 'i', 'o', 'u' , 'A', 'E', 'I', 'O', 'U'}
        res =[]
        split = sentence.split()

        for i, word in enumerate(split,1):
            cur = []
            if word[0] not in vowels:
                cur.append(word[1:] + word[0])
            else:
                cur.append(word)
            cur.append('ma')
            cur.extend(['a'] * i)
            res.append("".join(cur))

        return " ".join(res)

print(Solution().toGoatLatin("I speak Goat Latin"))