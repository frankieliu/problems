
Concise Java Solution

https://leetcode.com/problems/find-the-closest-palindrome/discuss/102400

* Lang:    java
* Author:  lixx2100
* Votes:   13

The following code attempts to simplify the logic by covering more cases. It is fine for this problem as the runtime is anyway O(1).
```Java
long ans = 0, diff = Long.MAX_VALUE, n = 0;

private void update(String val) {
    try {
        long tmp = Long.parseLong(val);
        if (tmp == n) return;
        if (Math.abs(tmp - n) < diff || (Math.abs(tmp - n) == diff && tmp < ans)) {
            ans = tmp;
            diff = Math.abs(tmp - n);
        }
    } catch (Exception e) { }
}

private void concat(long leftHalf) {
    String s = "" + leftHalf, rs = new StringBuilder(s).reverse().toString();
    update(s + rs); // abc -> abccba
    update(s + rs.substring(1)); // abc -> abcba
}

public String nearestPalindromic(String n) {
    this.n = Long.parseLong(n);
    diff = Long.MAX_VALUE;
    long leftHalf = Long.parseLong(n.substring(0, (n.length() + 1) / 2));
    concat(leftHalf - 1);
    concat((leftHalf - 1) * 10 + 9); // Handle 1, 1000, 100000, etc.
    concat(leftHalf);
    concat(leftHalf + 1);
    concat((leftHalf + 1) / 10); // Handle 9, 999, 99999, etc.
    return "" + ans;
}
```
