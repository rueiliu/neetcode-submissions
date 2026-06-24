class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""

        for s in strs:
            string = string + str(len(s)) + "#" + s
        
        return string

    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        while i < len(s):
            j = i
            # This correctly handles multi-digit lengths (e.g., "12#")
            while s[j] != "#":
                j += 1

            # Extract the length using the absolute boundaries i and j
            length = int(s[i:j])

            # Extract the actual string that comes right after the "#"
            res.append(s[j + 1 : j + 1 + length])

            # Move the pointer 'i' to the start of the next encoded block
            i = j + 1 + length

        return res

            

        