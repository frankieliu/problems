// https://gist.github.com/sumanth232/0dee3a337232482962f7
/*developed from the pseudo code from cormen page - 926
  easy picturied intuition can be seen at 
  http://www.inf.fh-flensburg.de/lang/algorithmen/pattern/kmpen.htm */


#include<stdio.h>
#include<stdlib.h>
#include<string.h>


// the word 'border' refers to 2 side border
// lps[i] = the longest PROPER prefix of pat[0..i] which is also a suffix of pat[0..i]
void computeLPSarray(char* pat, int m, int* lps) {
  lps[0] = 0;
  int len = 0 , i;

   // calculation of lps starts from 1
  for (i = 1; i < m; ++i)
  {
    /* while (there is a non-zero border && which we cannot extend)
       try to find the next widest border which we can extend */
    while(len>0 && pat[i] != pat[len]) len = lps[len-1];

    if(pat[i] == pat[len]) len = len + 1;

    lps[i] = len;
  }  
}


void KMPSearch(char*pat, char*txt) {
  int n = strlen(txt);
  int m = strlen(pat);

  int* lps = (int*)malloc(m*sizeof(int));
  computeLPSarray(pat, m, lps);

  int i, j=0; // 'j' indicates the number of characters of pat matched
  // Scan the text from left to right
  for (i = 0; i < n; ++i) {

    // mismatch after j matches
    // Do not match pat[0..lps[j-1]] characters, they will match anyway

    /* while (there are already non-zero matches && then a mismatch)
       get the (already matched part of pat)'s longest prefix suffix 
       so that we can resume pattern match after the end of above mentioned lps*/    
    while(j>0 && pat[j] != txt[i]) j = lps[j-1];
  
    if(pat[j] == txt[i]) j++;  // one more character of pat matches

    if(j==m) { // is all of pat matched
      printf("Match found at %d\n",i-m+1 );
      j = lps[j-1];
    }
    
  }
  free(lps);
}
