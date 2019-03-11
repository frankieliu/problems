"""A. Lottery
time limit per test2.0 s
memory limit per test512 MB
inputstandard input
outputstandard output

The internship team holds a lottery at various events.

The organizers choose 10 distinct random numbers from 1 to 32. Each
participant gets a lottery ticket containing 6 distinct numbers from 1
to 32. A ticket is considered to be winning if it contains at least 3
numbers chosen by the organizers.

Help Yulia and write a program that will determine which ticket is
winning.

Input

The first input line contains 10 distinct integers ai (1 ≤ ai ≤ 32),
the numbers chosen by the organizers.

The second line contains one integer n (1 ≤ n ≤ 1000), the number of
the lottery tickets issued at the event.

Each of the next n lines contains 6 distinct integers bj
(1 ≤ bj ≤ 32), the numbers written on the respective lottery ticket.

Output

Print n lines. For each lottery ticket (in the order they appear in
the input) output a line contains Lucky, if the ticket is considered
to be winning, otherwise output a line contains Unlucky.

Example
inputCopy
1 2 3 4 5 6 7 8 9 32
3
1 2 10 11 12 13
1 2 3 10 11 12
32 1 10 20 30 3
outputCopy
Unlucky
Lucky
Lucky
"""
