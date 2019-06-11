import java.util.Comparator;
import java.util.Map;
import java.util.Set;
import java.util.TreeMap;
import java.util.Arrays;

class SummaryRanges {

    public TreeMap<Integer, Integer> tm;

    /** Initialize your data structure here. */
    public SummaryRanges() {
        tm = new TreeMap<>();
    }

    public void addNum(int val) {
        // System.out.println("addNum " + val);
        Map.Entry<Integer,Integer> left = tm.floorEntry(val);
        Map.Entry<Integer,Integer> right = tm.ceilingEntry(val);

        // System.out.println("addNum pos 1");
        if ((left == null)  && (right == null)) {
            tm.put(val, val);
            return;
        }

        // System.out.println("addNum pos 2");
        if ((left == null) && (right != null)) {
            int rk = right.getKey();
            // check whether it touches the right
            if((rk-val) == 1){
                tm.remove(rk);
                tm.put(val, right.getValue());
            } else if(val < rk){
                tm.put(val, val);
            } else {
                // in interval
            }
            return;
        }

        // System.out.println("addNum pos 3");
        if ((right == null) && (left != null)){
            int lk = left.getKey();
            int lv = left.getValue();
            if((val-lv) == 1) {
                tm.put(lk, val);
            } else if(val > lv) {
                tm.put(val, val);
            } else {
                // in interval
            }
            return;
        }

        int lk = left.getKey();
        int lv = left.getValue();
        int rk = right.getKey();
        int rv = right.getValue();

        // System.out.println("addNum pos 4");
        if(((val-lv) == 1) && ((rk-val) == 1)) {
            tm.remove(rk);
            tm.put(lk,rv);
            return;
        }
        // System.out.println("addNum pos 5");
        if((val-lv) == 1) {
            tm.put(lk,val);
            return;
        }
        // System.out.println("addNum pos 6");
        if((rk-val) == 1) {
            tm.remove(rk);
            tm.put(val,rv);
            return;
        }
        // System.out.println("addNum pos 7");
        tm.put(val,val);
    }

    public int[][] getIntervals() {
        int s = tm.size();
        int[][] a = new int[s][2];

        int i = 0;
        for (Map.Entry<Integer,Integer> entry: tm.entrySet()) {
            a[i][0] = entry.getKey();
            a[i][1] = entry.getValue();
            i++;
        }
        // System.out.println(tm.size());
        return a;
    }

    public static void main2(String[] args) {
        SummaryRanges s = new SummaryRanges();
        // s.tm.put(1,2);
        // s.tm.put(3,4);
        int[] input = {1, 3, 7, 2, 6};
        int[][] a;
        for(int i: input) {
            s.addNum(i);
            a = s.getIntervals();
            // System.out.println(Arrays.deepToString(a));
        }
    }
}
