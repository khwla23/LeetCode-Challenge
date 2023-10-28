class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) <= 1:
            return len(chars)

        count = 1 #calculate the num of frequency of an alphabet 
        index = 0 #Tackle which index to overwrite 

        for i in range(1, len(chars)):
            if chars[i] == chars[i-1]:
                count += 1
            else:
                chars[index] = chars[i - 1]
                index += 1 #increment to avoid overwriting the first occurrence of the alphabet 
                if count > 1:
                    str_count = str(count)
                    if len(str_count) > 1:
                        for a_count in str_count:
                            chars[index] = a_count
                            index += 1
                    else:
                        chars[index] = str_count
                        index += 1
                count = 1

        #tackling when the list ends
        chars[index] = chars[-1]
        index += 1
        if count > 1:
            str_count = str(count)
            if len(str_count) > 1:
                for a_count in str_count:
                    chars[index] = a_count
                    index += 1
            else:
                chars[index] = str_count
                index+=1
        return index

