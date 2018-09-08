package main
import (
	"fmt"
	"golang.org/x/tour/tree"
)


func Walk2(t *tree.Tree, ch chan int){
	if t != nil {
		Walk2(t.Left,ch)
		ch <- t.Value
		Walk2(t.Right,ch)
	}
}

func Walk(t *tree.Tree, ch chan int) {
	Walk2(t, ch)
	close(ch)
}

func Same(t1, t2 *tree.Tree) bool {
	c1 := make(chan int)
	c2 := make(chan int)
	go Walk(t1, c1)
	go Walk(t2, c2)

	for {
		n1,ok1 := <-c1
		n2,ok2 := <-c2
		if ok1 == true && ok2 == true {
			if n1 != n2 {
				return false
			}
		}
		if ok1 == false && ok2 == true {
			return false
		}
		if ok1 == true && ok2 == false {
			return false
		}
		if ok1 == false && ok2 == false {
			break
		}
	}
	return true
}

func main() {
	ch := make(chan int)
	go Walk(tree.New(1), ch)
	for i := range ch {
		fmt.Println(i)
	}
	fmt.Println(Same(tree.New(1), tree.New(1)))
	fmt.Println(Same(tree.New(1), tree.New(2)))
}
