/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

#include "../base/listnode.hpp"

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        bool first = true;
        ListNode* c = new ListNode(0);
        ListNode* d = c;

        while ((l1 != NULL) || (l2 != NULL)) {
            if (l1 == NULL) {
                while (l2 != NULL) {
                    cout << "Adding: " << l2->val << endl;
                    d->next = new ListNode(l2->val);
                    l2 = l2->next;
                    d = d->next;
                }
            } else if (l2 == NULL) {
                while (l1 != NULL) {
                    cout << "Adding: " << l1->val << endl;
                    d->next = new ListNode(l1->val);
                    l1 = l1->next;
                    d = d->next;
                }
            } else {
                int val;
                // cout << l1->val << " "<< l2->val << endl;
                if (l1->val <= l2->val) {
                    val = l1->val;
                    l1 = l1->next;
                } else {
                    val = l2->val;
                    l2 = l2->next;
                }
                cout << "Adding: " << val << endl;
                d->next = new ListNode(val);
                d = d->next;
            }
        }
        return c->next;
    }
};
