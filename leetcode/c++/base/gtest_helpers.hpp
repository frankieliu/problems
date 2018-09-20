#include <gtest/gtest.h>
#include "./listnode.hpp"

// https://stackoverflow.com/questions/10060110/how-does-gtest-compare-the-values-in-two-arrays
template<typename T, size_t size>
::testing::AssertionResult ArraysMatch(const T (&expected)[size],
                                       const T (&actual)[size]){
    for (size_t i(0); i < size; ++i){
        if (expected[i] != actual[i]){
            return ::testing::AssertionFailure() << "array[" << i
                                                 << "] (" << actual[i] << ") != expected[" << i
                                                 << "] (" << expected[i] << ")";
        }
    }
    
    return ::testing::AssertionSuccess();
}
// EXPECT_TRUE(ArraysMatch(two_sorted, two));         

::testing::AssertionResult ListNodeMatch(const ListNode (*expected),
                                           const ListNode (*actual)) {
    size_t i = 0;
    while((expected != NULL) && (actual != NULL)) {
        if (expected == NULL) {
            return ::testing::AssertionFailure()
                << "actual[" << i << "] (" <<  actual->val << ") "
                << "is longer than expected[]";
        } else if (actual == NULL) {
            return ::testing::AssertionFailure()
                << "actual[" << i << "] "
                << "is not defined != " 
                << "expected[" << i << "] (" << expected->val << ")";
        } else if (expected->val != actual->val) {
            return ::testing::AssertionFailure()
                << "actual[" << i << "] (" << actual->val << ") != "
                << "expected[" << i << "] (" << expected->val << ")";
        } else {
            cout << "comparing: " << i << " "
                 << expected->val << " "
                 << actual->val << endl;
        }
        actual = actual->next;
        expected = expected->next;
        i++;
    }
    return ::testing::AssertionSuccess();
}
