class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for word in strs:
            encoded_str += "#" + str(len(word)).zfill(3) + word
        return encoded_str

    def decode(self, s: str) -> List[str]:

        if (len(s) == 0):
            return []

        decoded_message = []

        idx = 0

        while idx <= (len(s) - 4):
            word_len = int(s[idx+1:idx+4]) 
            if (word_len == 0):
                decoded_message.append("")
            else:
                decoded_message.append(s[idx+4:idx+4+word_len])
            idx += word_len + 4

        return decoded_message
