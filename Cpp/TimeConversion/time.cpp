/*
Given a time in -hour AM/PM format, convert it to military (-hour) time.

Note: Midnight is  on a -hour clock, and  on a -hour clock. Noon is  on a -hour clock, and  on a -hour clock.

Input Format

A single string containing a time in -hour clock format (i.e.:  or ), where  and .

Output Format

Convert and print the given time in -hour format, where .

Sample Input

07:05:45PM
Sample Output

19:05:45
*/

#include <string>
#include <iostream>
#include <sstream>
#include <bits/stdc++.h>

using namespace std;

string timeConversion(string s) {

  // Get the hours
  int h = std::stoi (s.substr(0,2),nullptr);

  // Take care of PM
  if (s.compare(8,10,"PM") == 0) {
    if (h != 12) {
      h += 12;
    } else {
      h += 0;
    }
  } else if (h == 12) {
    h = 0;
  }

  std::stringstream ss;
  
  ss << std::setfill('0') << std::setw(2) << h;

  return ss.str() + s.substr(2,6);
}

int main() {
    string s = "07:05:45PM";
    // cin >> s;

    string result = timeConversion(s);

    cout << result << endl;
    return 0;
}
