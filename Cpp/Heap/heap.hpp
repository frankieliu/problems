#if !defined(HEAP_H_INCLUDED)
#define HEAP_H_INCLUDED

#include <vector>

class MinHeap {
private:
  std::vector<int> _vector;
  void BubbleDown(int index);
  void BubbleUp(int index);
  void Heapify();

public:
  MinHeap(int* array, int length);
  MinHeap(const std::vector<int>& vector);
  MinHeap();

  void Insert(int newValue);
  int GetMin();
  int DeleteMin();
  std::vector<int>& v();
  void Print();
  void TreePrint();
  void TreePrint(std::vector<int> &v, int index, int depth, bool last, std::vector<bool> &vertical);
  std::vector<int> Sort();
};

#endif
