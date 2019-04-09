
Java Dynamic Programming (Runtime: 1 ms, faster than 100.00%)

https://leetcode.com/problems/fibonacci-number/discuss/254602

* Lang:    java
* Author:  denimdatta
* Votes:   0

	class Solution {
		int[] table;
		public int fib(int N) {
			if (N == 0) {
				return 0;
			}
			if (N <= 2) {
				return 1;
			}
			table = new int[N+1];
			Arrays.fill(table, -1);

			table[0] = 0;
			table[1] = 1;
			table[2] = 1;

			findfib(N);

			return table[N];
		}

		private int findfib(int n) {
			if (table[n] != -1) {
				return table[n];
			}

			table[n] = findfib(n-1) + findfib(n-2);
			return table[n];
		}
	}
