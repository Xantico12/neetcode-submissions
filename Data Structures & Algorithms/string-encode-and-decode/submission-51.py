class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        
        encodedStr = ""
        allWordsStr = ""
        decKey = ""
        for word in range(len(strs)):
            allWordsStr += strs[word]
            if word < len(strs) - 1:
                decKey += str(len(strs[word])) + ","

        decKey = decKey + str(len(strs[len(strs) - 1])) + "]"
        encodedStr = decKey + allWordsStr

        print("decKey: " + decKey)
        print("encodedStr: " + encodedStr)

        return encodedStr

    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        dividerIdx = s.find("]")
        decKey = list(map(int, s[:dividerIdx].split(",")))
        unsplitStr = s[dividerIdx + 1:]

        print("decKey2: " + str(decKey))

        decodedList = [""] * len(decKey)

        currentIdx = 0
        listIdx = 0

        for i in decKey:
            for ch in range(currentIdx, currentIdx + i):
                decodedList[listIdx] += unsplitStr[ch]
            
            currentIdx += i
            listIdx += 1

            

        return decodedList
