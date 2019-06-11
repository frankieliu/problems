"""It seems nobody has addressed where the recursive function calls
itself more than once in the body, and handles returning to a specific
point in the recursion (i.e. not primitive-recursive). It is said that
every recursion can be turned into iteration, so it appears that this
should be possible.

I just came up with a C# example of how to do this. Suppose you have
the following recursive function, which acts like a postorder
traversal, and that AbcTreeNode is a 3-ary tree with pointers a, b, c.

public static void AbcRecursiveTraversal(this AbcTreeNode x, List<int> list) {
        if (x != null) {
            AbcRecursiveTraversal(x.a, list);
            AbcRecursiveTraversal(x.b, list);
            AbcRecursiveTraversal(x.c, list);
            list.Add(x.key);//finally visit root
        }
}

The iterative solution:

        int? address = null;
        AbcTreeNode x = null;
        x = root;
        address = A;
        stack.Push(x);
        stack.Push(null)

        // stack x, null

        while (stack.Count > 0) {
            bool @return = x == null;

            // if x == null : do something different
            // address at start is A
            if (@return == false) {

                switch (address) {
                    case A:
                        stack.Push(x);
                        stack.Push(B);
                        // x, null, x, B
                        // x = x.a
                        // address is A
                        // keep push all of x.a into the stack
                        // until x becomes null
                        x = x.a;
                        address = A;
                        break;
                    case B:
                        stack.Push(x);
                        stack.Push(C);
                        x = x.b;
                        address = A;
                        break;
                    case C:
                        stack.Push(x);
                        stack.Push(null);
                        x = x.c;
                        address = A;
                        break;
                    case null:
                        list_iterative.Add(x.key);
                        @return = true;
                        break;
                }

            }

            if (@return == true) { // finished pushing all x.a
                // stack x, null, x.a, B, x.a.a, B, x.a.a.a, B
                // then get B and x.a.a.a out?
                address = (int?)stack.Pop();
                x = (AbcTreeNode)stack.Pop();
            }


        }
"""
