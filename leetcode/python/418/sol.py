
Python ~100ms

https://leetcode.com/problems/sentence-screen-fitting/discuss/90853

* Lang:    python3
* Author:  yorkshire
* Votes:   0

Similar to other solutions, preprocess to find the number of sentences that can fit on a row starting with each word. Also find the next starting word.
Big speedup comes from checking how many complete sentences can fit on a row before going word by word.

```
class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        sentence_len = sum(len(w) for w in sentence) + len(sentence)
        
        # line_fits[i] = (number of complete sentences, index of next starting word) for a row starting with sentences[i]
        line_fits = []
        
        for start_word_index in range(len(sentence)):
        
            row_length, sentences = 0, 0
            word_index = start_word_index
            
            while row_length + sentence_len <= cols:                # can fit next sentence in row
                row_length += sentence_len
                sentences += 1
        
            while row_length + len(sentence[word_index]) <= cols:   # can fit next word in row
                row_length += len(sentence[word_index]) + 1         # extend row_length by word and space
                word_index += 1                                     # move to next word
                if word_index == len(sentence):                     # fitted last word of sentence
                    sentences += 1
                    word_index = 0

            line_fits.append((sentences, word_index))

        fits, word_index = 0, 0
        for _ in range(rows):
            sentences, next_word_index = line_fits[word_index]
            fits += sentences
            word_index = next_word_index
            
        return fits
