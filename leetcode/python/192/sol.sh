
1 Line Solution using Pipes

https://leetcode.com/problems/word-frequency/discuss/55465

* Lang:    bash
* Author:  fabrizio3
* Votes:   3

    cat words.txt | tr '\
' ' ' | sed "s/\\s\\s*/ /g" | awk -v RS=' ' '{print $0}' | sort | uniq -c | sort -nr -k1 | awk '{print $2" "$1}'

**cat word.txt** :
output the text in the file

**tr '\
' ' '** :
substitute endlines with single space

**sed "s/\\s\\s*/ /g"** :
substitute multiple spaces with single space

**awk -v RS=' ' '{print $0}'** :
output one word per line by changing Record Separator in AWK to single space. $0 is the entire record (1 word).

**sort** :
sort alphabetically the list of words (with repetitions) to prepare it for uniq command.

**uniq -c** :
print the list of unique words with their count. Before uniq you need to sort the list of words.

**sort -nr -k1** :
sort the list of unique words by their count  (-nr numerical reverse sorting) (-k1 sort by the first field that is the count of repetitions for the current word)

**awk '{print $2" "$1}'** :
for each line print before the second field $2, that is the word, and then the first field that is the count of repetitions for the word.
