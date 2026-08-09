class Solution:

    def encode(self, strs: List[str]) -> str:
        '''
            prepends a string in strings with it's length followed by '#'
            to a single string which is returned for decoding.
        '''
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            decoded.append(s[j + 1: j + 1 + length])
            i = j + 1 + length
        return decoded
