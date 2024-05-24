class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        patternFirstIndex = dict()
        patternSignature = []
        for index, char in enumerate(pattern):
            if char not in patternFirstIndex:
                patternFirstIndex[char] = index
            patternSignature.append(patternFirstIndex[char])

        sFirstIndex = dict()
        sSignature = []
        for index, word in enumerate(s.split(" ")):
            if word not in sFirstIndex:
                sFirstIndex[word] = index
            sSignature.append(sFirstIndex[word])

        return patternSignature == sSignature