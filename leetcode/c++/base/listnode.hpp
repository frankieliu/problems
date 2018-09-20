#ifndef __listnode_h__
#define __listnode_h__

class ListNode {
public:
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

#endif
