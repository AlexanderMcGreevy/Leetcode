class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        result = [""]     
        num = 0
        offset=0
        for x in words:
            # if current line is empty, place x directly
            if result[num] == "":
                # guarantee assumption instead of slicing:
                if len(x) <= maxWidth:
                    result[num] = x
                    continue
                
            # otherwise, try to add with one leading space
            if len(result[num]) + 1 + len(x) <= maxWidth:
                result[num] += " " + x
            else:
                # start a new line with x and advance num
                result.append(x)
                num += 1
        # make each line exactly maxWidth by adding spaces left→right
        for i in range(len(result)):
            line = result[i]

            # last line or single-word line: just pad at end
            if i == len(result) - 1 or " " not in line:
                result[i] = line.ljust(maxWidth)
                continue

            words_in_line = line.split(" ")   # current words, single spaces between
            gaps = len(words_in_line) - 1
            g = 0  # gap index (left to right)

            # add one space at a time cycling left→right over gaps
            while len(line) < maxWidth:
                words_in_line[g] += " "       # widen gap g by 1
                g = (g + 1) % gaps            # next gap (wrap around)
                line = " ".join(words_in_line)

            result[i] = line

    
        return result

                        
                    
                        


                        

        