#include <gtest/gtest.h>
#include "../base/cpp_standards.h"
#include "../base/TreeNode.hpp"
#include "serialize-and-deserialize-binary-tree.hpp"

/*

Serialization is the process of converting a data structure or object
into a sequence of bits so that it can be stored in a file or memory
buffer, or transmitted across a network connection link to be
reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There
is no restriction on how your serialization/deserialization algorithm
should work. You just need to ensure that a binary tree can be
serialized to a string and this string can be deserialized to the
original tree structure.

Example: 

You may serialize the following tree:

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]"

Clarification: The above format is the same as how LeetCode serializes
a binary tree. You do not necessarily need to follow this format, so
please be creative and come up with different approaches yourself.

Note: Do not use class member/global/static variables to store
states. Your serialize and deserialize algorithms should be stateless.

  Solution at:
  https://leetcode.com/articles/serialize-and-deserialize-binary-tree/
*/

void printTreeNode(TreeNode* t, int indent){
    if (t != NULL){
        for (auto n = indent; n > 0; n--) cout << " ";
        cout << t->val << endl;
        printTreeNode(t->left, indent + 1);
        printTreeNode(t->right, indent + 1);
    }
}

// http://math.hws.edu/eck/cs225/s03/binary_trees/

// Good tree example with tree functions
// http://www.cs.uah.edu/~rcoleman/Common/CodeVault/Code/Code202_Tree.html
// http://www.cs.uah.edu/~rcoleman/Common/CodeVault/Code/Code202_Tree.html

// This is important read!
// smart pointers
// https://codereview.stackexchange.com/questions/135432/c-tree-class-implementation
// https://en.cppreference.com/w/cpp/memory/unique_ptr

TEST(Leetcode, serialize_and_deserialize_binary_tree_297) {
    // Solution s;
    TreeNode t(1);
    t.left = new TreeNode(2);
    t.right = new TreeNode(3);
    t.right->left = new TreeNode(4);
    t.right->right = new TreeNode(5);
    printTreeNode(&t, 0);

    Codec c;
    string ser(c.serialize(&t));

    TreeNode* t2 = c.deserialize(ser);
    printTreeNode(t2, 0);
    
    // vector<int> a={,};
    // EXPECT_EQ(, s.(a));
    // vector<int> b={,};
    // EXPECT_EQ(, s.(b));
}
