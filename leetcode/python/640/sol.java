
My 6ms Java Solution(Beats 100%)

https://leetcode.com/problems/solve-the-equation/discuss/105361

* Lang:    java
* Author:  cxw19960131
* Votes:   0

I have tried to submit 3 times. Except for a 22ms one, the rest are all 6ms  : |
Here is my code(it may be redundant)




    public String solveEquation(String equation) {
        equation = equation + "=";
        int i = 0;
        boolean pos = true;
        int[] res = new int[2];
        List<Integer> temp1 = new ArrayList<>();
        List<Integer> temp2 = new ArrayList<>();
        while (i < equation.length()) {
            char ch = equation.charAt(i);
            if (ch == '=') {
                i++;
                if (temp1.size() == 0) {
                    temp1.add(res[0]);
                    temp1.add(res[1]);
                } else {
                    temp2.add(res[0]);
                    temp2.add(res[1]);
                }
                res[0] = res[1] = 0;
                pos = true;
                continue;
            }
            if (ch == '+') {
                pos = true;
                i++;
            } else if (ch == '-')  {
                pos = false;
                i++;
            }
            if (equation.charAt(i) == 'x') {
                i++;
                res[0] += pos ? 1 : -1;
            } else if (Character.isDigit(equation.charAt(i))) {
                int index = 0;
                int start = i;
                while (i < equation.length() && Character.isDigit(equation.charAt(i))) {
                   i++;
                }
                index = Integer.valueOf(equation.substring(start, i)); 
                if (equation.charAt(i) != 'x') res[1] += pos ? index : -index;
                else {res[0] += pos ? index : -index; i++;}
            }
            
        }
        res[0] = temp1.get(0) - temp2.get(0);
        res[1] = temp2.get(1) - temp1.get(1);
        
        if (res[0] == 0 && res[1] == 0) return "Infinite solutions";
        if (res[0] == 0 && res[1] != 0) return "No solution";
        else return "x=" + res[1] / res[0] + "";
    }
I append a "=" to the end of the equation so to execute the loop smoothly
for example 
x+2x-5+8=-6-6x= :                           
        x+2x-5+8---> **a** :{3(the coefficient of x), 3}                 
         -6-3x---> **b** :{-6, -6}
in this way we can obtain the coefficient of x and Integer and we can change the equation to
9x=-9 ------> **a**[0] - **b**[0] = **b**[1] - **a**[1] 
then by analyzing the different condition of **a** and **b** we can solve this problem
O(n)-time complexity
O(1)-space complexity

ps \uff1a I try to optimize my code but I find time changes to 7ms...
