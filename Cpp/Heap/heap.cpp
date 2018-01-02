#include <iostream>
#include <vector>
#include "heap.hpp"

MinHeap::MinHeap(int *array, int length) : _vector(array, array+length) {
  Heapify();
}
MinHeap::MinHeap(const std::vector<int>& v) {
  std::vector<int> _vector(v);
  Heapify();
}
MinHeap::MinHeap() {
  std::vector<int> _vector;
}
int MinHeap::GetMin() {
  if (_vector.size() >= 1) {
    return _vector[0];
  } else {
    return 0;
  }
}
int MinHeap::DeleteMin() {
  // Move the last element in heap to top
  // Decrease the array size by 1
  // Perform BubbleDown on the first node
  int size = _vector.size();
  if (size == 0) return 0;
  int tmp = _vector[0];
  _vector[0] = _vector[size-1];
  BubbleDown(0);
  _vector.resize(size-1);
  return tmp;
}
void MinHeap::Insert(int newValue) {
  int new_size = _vector.size() + 1;
  _vector.resize(new_size);
  _vector[new_size - 1] = newValue;
  BubbleUp(new_size - 1);
}
void MinHeap::BubbleDown(int index) {
  // Exchange with the minimum leaf
  int left_index = 2*index+1;
  int right_index = 2*index+2;
  int s = _vector.size();

  if (index >= s) { return; }
  int j = _vector[index];

  int exchange_index = left_index;
  if (left_index >= s) {
    return;
  } else {
    if (right_index < s) {     // right exists
      if (_vector[left_index] > _vector[right_index]) {
	exchange_index = right_index;
      }
    }
  }
  if (_vector[exchange_index] >= j) {
    return;
  } else {
    // Exchange
    int tmp = _vector[exchange_index];
    _vector[exchange_index] = j;
    _vector[index] = tmp;
    BubbleDown(exchange_index);
  }
}    
void MinHeap::BubbleUp(int index) {

  if ((index == 0) || (index > (_vector.size() - 1))) { return; }

  // Exchange with the parent
  int parent = (int) ((index-1)/2);
  int j = _vector[index];
  if (_vector[parent] > j) {
    _vector[index] = _vector[parent];
    _vector[parent] = j;
    BubbleUp(parent);
  } else {
    return;
  }
}
void MinHeap::Heapify() {
  // Go from the last element to the first and bubble up on
  // each one
  int s = _vector.size();
  for (int i=s/2 - 1; i>=0; i--) {
    BubbleDown(i);
    // BubbleUp(i);
  }
}
std::vector<int>& MinHeap::v() {
  std::cout << "In MinHeap::v " << _vector.size() << std::endl;
  return _vector;
}
void MinHeap::Print() {
  // std::vector<int> v = h.v();
  // std::cout << "Size of vector: " << v.size() << std::endl;
  for(auto it=_vector.begin(); it!=_vector.end(); ++it) {
    std::cout << ' ' << *it;
  }
  std::cout << '\n';
}
void MinHeap::TreePrint() {
  std::vector<bool> vertical(0);
  MinHeap::TreePrint(_vector, 0, 0, false, vertical);
}

/**
   Printing a heap (or a binary bin)
   
   Print the Left Node, and descend on the Child and recurse
   Print the Right Node, and descend on the Child and recurse

   Parent
   ├─── Child A
   │    └─── Child AA
   │         ├─── Child AAA
   │         └─── Child AAB
   └─── Child B

   
   If AA is the last one then all its children should receive a blank at A's level,
   but since A is not the last one then it should still extend down with a vertical
   bar.

   So Child AAA, should receive " "x4 from AA, and should receive "│    " from Parent.
   Basically the parents, should inform the number of bars to print.

 */
void MinHeap::TreePrint(std::vector<int> &v, int index, int depth, bool last, std::vector<bool> &vertical) {
  
  const char *UR = u8"\u2514";
  const char *VR = u8"\u251c";
  
  const char *LR = u8"\u2500";
  const char *UD = u8"\u2502";
  const char *SP = "   ";

  // if (depth > 1) return;
  if (index >= v.size()) return;
  
  // print the spaces
  for (int i = 0; i < vertical.size(); i++) {
    if(vertical[i]) {
      std::cout << UD << SP;               // "│    "
    } else {
      std::cout << " " << SP;              // "     "
    }
  }

  // If the last one then don't print
  if (depth > 0) {
    if ((!last) && (index != v.size()-1)) {
      std::cout << VR << LR << LR << " ";  //  ├─── Child AAA
      vertical.push_back(true);
    } else {
      std::cout << UR << LR << LR << " ";  //  └─── Child AAB
      vertical.push_back(false);
    }
  }

  // Print the node name
  std:: cout << v[index] << std::endl;

  // Print the children
  MinHeap::TreePrint(v, 2*index+1, depth+1, false, vertical);
  MinHeap::TreePrint(v, 2*index+2, depth+1, true, vertical);

  // Pop the vertical information
  vertical.erase(std::end(vertical));
}
std::vector<int> MinHeap::Sort() {
  // Note this is destructive
  std::vector<int> out;
  while(_vector.size() != 0){
    out.push_back(MinHeap::DeleteMin());
  }
  return out;
}
