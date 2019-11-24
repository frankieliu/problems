// https://codereview.stackexchange.com/questions/102413/segment-tree-with-lazy-propagation
package main

import (
//"fmt"
)

var array []int; // Array to store initial input  like: [1,2,3,4,5,6,7,8,9,10]

/*
   This is Node structure
   val    : aggregate result (sum, min, max ...)
   lazy   : for lazy propagation
   lc, rc : left & right child
*/
type Node struct {
    val    int
    lazy   int
    lc, rc *Node
}


// This function will return middle index of left and right
func midIndx(l, r int) (mid int) {
    mid = l + (r - l) / 2
    return mid
}

// This function is used to create initial tree
func (node *Node) MakeTree(left, right int) {

    // Out of range
    if right < left {
        return
    }

    // Leaf node
    if left == right {
        node.val = array[left]; // Init value
        return
    }

    var lc, rc Node;
    mid := midIndx(left, right)
    lc.MakeTree(left, mid)       // Init left child
    rc.MakeTree(mid + 1, right)  // Init right child

    // link with parent
    node.lc = &lc
    node.rc = &rc

    // set parent value from left and right child
    if node.lc.val > node.rc.val {
        node.val = node.lc.val
    } else {
        node.val = node.rc.val
    }
}

/**
 * Query tree to get max element value within range [l, r]
 */
func (node *Node) Query(left, right, l, r int) int {

    // Out of range
    if right < l || left > r || right < left {
        return -1e18 // as query for maximum number
    }

    // This node needs to be updated
    if node.lazy != 0 {
        node.val = node.val + node.lazy  // Update it
        if left != right {  // propagate lazy value to its child
            node.lc.lazy = node.lc.lazy + node.lazy  // Mark left child as lazy
            node.rc.lazy = node.rc.lazy + node.lazy  // Mark right child as lazy
        }
        node.lazy = 0  // as lazy value is added and propagate to its child, set to 0
    }

    // current segment is totally within range [l, r]
    if left >= l && right <= r {
        return node.val
    }

    mid := midIndx(left, right)
    L := node.lc.Query(left, mid, l, r)       // query left  child
    R := node.rc.Query(mid + 1, right, l, r)  // query right child

    // return max value to parent
    if L > R {
        return L
    } else {
        return R
    }
}

/**
 * Increment elements within range [l, r] with value value
 */
func (node *Node) Update(left, right, l, r, val int) {
    // This node needs to be updated
    if node.lazy != 0 {
        node.val = node.val + node.lazy  // Update it
        if left != right {
            node.lc.lazy = node.lc.lazy + node.lazy  // Mark left child as lazy
            node.rc.lazy = node.rc.lazy + node.lazy  // Mark right child as lazy
        }
        node.lazy = 0 // Reset it
    }

    // Current segment is not within range [l, r]
    if right < l || left > r || right < left {
        return
    }

    // Segment is fully within range
    if left >= l && right <= r {
        node.val = node.val + val
        if left != right { // Not leaf node
            node.lc.lazy = node.lc.lazy + val
            node.rc.lazy = node.rc.lazy + val
        }
        return
    }

    mid := midIndx(left, right)
    node.lc.Update(left, mid, l, r, val)      // Updating left child
    node.rc.Update(mid + 1, right, l, r, val)  // Updating right child


    // Updating root with max
    if node.lc.val > node.rc.val {
        node.val = node.lc.val
    } else {
        node.val = node.rc.val
    }
    return
}

func main() {
    n := (len(array)) - 1
    var start Node
    var l, r, val int
    start.MakeTree(0, n)           // make initial tree
    start.Update(0, n, l, r, val)  // Update tree within a range
    _ = start.Query(0, n, 0, 19)   // Query within a ran
}
