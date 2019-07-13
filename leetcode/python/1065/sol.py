In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1065.index-pairs-of-a-string.algorithms.json

Trie Java 2ms 100%

https://leetcode.com/problems/index-pairs-of-a-string/discuss/304118

* Lang:    python
* Author:  YifeiGong
* Votes:   3

```
class Solution {
    public int[][] indexPairs(String text, String[] words) {
        /*initializing tire and put all word from words into Trie.*/
        Trie trie=new Trie();
        for(String s:words){
            Trie cur=trie;
            for(char c:s.toCharArray()){
                if(cur.children[c-\'a\']==null){
                    cur.children[c-\'a\']=new Trie();
                }
                cur=cur.children[c-\'a\'];
            }
            cur.end=true;       /*mark there is a word*/
        }
        
        /*if text is "ababa", check "ababa","baba","aba","ba","a" individually.*/
        int len=text.length();
        List<int[]> list=new ArrayList<>();
        for(int i=0;i<len;i++){
            Trie cur=trie;
            char cc=text.charAt(i);
            int j=i;   /*j is our moving index*/
            
            while(cur.children[cc-\'a\']!=null){ 
                cur=cur.children[cc-\'a\'];
                if(cur.end){   /*there is a word ending here, put into our list*/
                    list.add(new int[]{i,j});
                }
                j++;
                if(j==len){  /*reach the end of the text, we stop*/
                    break;
                }
                else{
                    cc=text.charAt(j);  
                }
            }
        }
        /*put all the pairs from list into array*/
        int size=list.size();
        int[][] res=new int[size][2];
        int i=0;
        for(int[] r:list){
            res[i]=r;
            i++;
        }
        return res;
    }
}
class Trie{
    Trie[] children;
    boolean end;   /*indicate whether there is a word*/
    public Trie(){
        end=false;
        children=new Trie[26];
    }
}
```


Python version:
```
class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        trie={}
        for w in words:
            cur=trie
            for c in w:
                if c not in cur.keys():
                    cur[c]={}
                cur=cur[c]
            cur[\'#\']=True
        
        res=[]
        lens=len(text)
        for i in range(lens):
            cur=trie
            cc=text[i]
            j=i
            while cc in cur.keys():
                cur=cur[cc]
                if \'#\' in cur.keys():
                    res.append([i,j])
                j+=1
                if j==lens:
                    break
                else:
                    cc=text[j]
        return res
```
