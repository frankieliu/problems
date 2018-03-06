/*HackerLand University has the following grading policy:

Every student receives a  in the inclusive range from  to .
Any  less than  is a failing grade.
Sam is a professor at the university and likes to round each student's  according to these rules:

If the difference between the  and the next multiple of  is less than , round  up to the next multiple of .
If the value of  is less than , no rounding occurs as the result will still be a failing grade.
For example,  will be rounded to  but  will not be rounded because the rounding would result in a number that is less than .

Given the initial value of  for each of Sam's  students, write code to automate the rounding process. Complete the function solve that takes an integer array of all grades, and return an integer array consisting of the rounded grades. For each , round it according to the rules above and print the result on a new line.

Input Format

First Line

integer 
: number of students
Next  lines

integer 
: individual grades
Output Format

Print  lines, each with the rounded value of a studentâs grade in input order.

Sample Input 0

4
73
67
38
33
Sample Output 0

75
67
40
33
Explanation 0

image

Student  received a , and the next multiple of  from  is . Since , the student's grade is rounded to .
Student  received a , and the next multiple of  from  is . Since , the grade will not be modified and the student's final grade is .
Student  received a , and the next multiple of  from  is . Since , the student's grade will be rounded to .
Student  received a grade below , so the grade will not be modified and the student's final grade is .
*/
#include <bits/stdc++.h>
2
â
3
using namespace std;
4
â
5
vector < int > solve(vector < int > grades){
6
    // Complete this function
7
}
8
â
9
int main() {
10
    int n;
11
    cin >> n;
12
    vector<int> grades(n);
13
    for(int grades_i = 0; grades_i < n; grades_i++){
14
       cin >> grades[grades_i];
15
    }
16
    vector < int > result = solve(grades);
17
    for (ssize_t i = 0; i < result.size(); i++) {
18
        cout << result[i] << (i != result.size() - 1 ? "\n" : "");
19
    }
20
    cout << endl;
21
    
22
â
23
    return 0;
24
}
25
â
