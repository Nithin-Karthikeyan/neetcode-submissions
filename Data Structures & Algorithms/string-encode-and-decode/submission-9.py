class Solution:

    def encode(self, strs: List[str]) -> str:
        # Encode using the len of the string and a delimiter before each string
        encoded_string = ""
        delim = "-"
        for s in strs:
            encoded_string += str(len(s)) + delim + s   
        return encoded_string

    def decode(self, s: str) -> List[str]:
        # We know that: <len><delim><string> is the order
        delim = "-"
        decoded_strs = []
        # for idx, char in enumerate(s):
        #     # If the current index is an int, and next is the delim, take the next consecutive chars according to the int, and add to strs
        #     if char.isdigit() and idx+1 < len(s):
        #         if s[idx+1] == "-":
        #             len_decoded_string = int(char) 
        #             decoded_string = s[idx+2:idx+2+len_decoded_string]
        #             decoded_strs.append(decoded_string)
        #             # Also jump to the next string since we know that the length is defined
        #         # idx
        # return decoded_strs

        i = 0
        while i < len(s):
            # Since len is the starting of string, go from there and search 
            # till delim
            # Anyways when we jump index, we will make sure to jump to the next 
            # length value
            j = i
            while s[j] != delim:
                j += 1
            
            # Everything up to the delim is length
            len_decoded_string = int(s[i:j])  
            start = j+1  
            end = start + len_decoded_string
            decoded_strs.append(s[start:end])
            i = end 

        # for i in range(len(s)):
        #     if s[i].isdigit() and i+1 < len(s):
        #         if s[i+1] == delim:
        #             len_decoded_string = int(s[i])
        #             decoded_string = s[i+2:i+2+len_decoded_string]
        #             decoded_strs.append(decoded_string)

        #             i += len_decoded_string + 2
        return decoded_strs