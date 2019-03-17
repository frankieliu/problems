
[Python/Java] DFS solution with explanation

https://leetcode.com/problems/most-frequent-subtree-sum/discuss/245383

* Lang:    python3
* Author:  Max_I
* Votes:   0

The idea is very simple:
1. Traverse structure using post order
2. Calculate sum of sub trees on every step
3. Store frequence of occurence of calculated sum into map/dict
4. Maintain max of frequence of occurence on every step. Letter we will use it to filter out result
5. Traverse map/dict and filter output based on max of frequence of occurence 
Java implementation:
```
import java.util.ArrayList;
import java.util.Hashtable;
import java.util.Map;
    private Hashtable<Integer,Integer> _data=new Hashtable<>();
    private Integer _maxVal=0;
    public int[] findFrequentTreeSum(TreeNode root) {
        ArrayList<Integer> res=new ArrayList<>();
        this.dfs(root);
        for(Map.Entry<Integer,Integer> item:this._data.entrySet()){
            if (item.getValue()==this._maxVal){
                res.add(item.getKey());
            }
        }
        int[] output=new int[res.size()];
        for(int i=0; i<res.size();i++){
            output[i]=res.get(i);
        }
        return  output;

    }
    private Integer dfs(TreeNode node){
        if (node ==null){
            return 0;
        }
        Integer left=this.dfs(node.left);
        Integer right=this.dfs(node.right);
        Integer cur=left+right+node.val;
        if (_data.containsKey(cur)){
            _data.put(cur,_data.get(cur)+1);
        }
        else{
            _data.put(cur,0);
        }
        this._maxVal=Math.max(this._maxVal,_data.get(cur));
        return cur;
    }
```

Python Implementation:
```
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def dfs(node):
            if node is None:
                return 0
            left=dfs(node.left)
            right=dfs(node.right)
            cur=left+right+node.val
            if cur in self.d:
                self.d[cur]+=1
            else:
                self.d[cur]=0
            self.maxVal=max(self.maxVal, self.d[cur])
            return cur
        self.d={}
        self.maxVal=0
        dfs(root)
        res=[]
        for k,v in self.d.items():
            if v==self.maxVal:
                res.append(k)
        return res
        
```
