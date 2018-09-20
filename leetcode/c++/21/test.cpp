#include <gtest/gtest.h>
#include "../base/cpp_standards.h"
#include "../base/gtest_helpers.hpp"
#include "../base/listnode.hpp"
#include "merge-two-sorted-lists.hpp"

/*
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
*/

ListNode* vector_to_list(vector<int> v) {
    ListNode* c = new ListNode(0);
    ListNode* d = c;
    for (int x: v) {
        // cout << "adding: " << x << endl;
        d->next = new ListNode(x);
        d = d->next;
    }
    d = c;
    c = c->next;
    delete(d);
    return c;
}

void print_list(ListNode *a) {
    while (a != NULL) {
        cout << a->val;
        a = a->next;
    }
    cout << endl;
}

TEST(Leetcode, merge_two_sorted_lists_21) {
    Solution s;
    ListNode *a = vector_to_list(vector<int>{1, 2, 4});
    ListNode *b = vector_to_list(vector<int>{1, 3, 4});
    ListNode *c = vector_to_list(vector<int>{1, 1, 2, 3, 4, 4});
    ListNode *d = s.mergeTwoLists(a, b);
    
    cout << "a: "; print_list(a);
    cout << "b: "; print_list(b);
    cout << "expected: "; print_list(c);
    cout << "actual:   "; print_list(d);
    
    EXPECT_TRUE(ListNodeMatch(c, s.mergeTwoLists(a, b)));
}
