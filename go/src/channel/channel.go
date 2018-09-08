package main
import "fmt"
func sum(a []int, c chan int) {
	s := 0
	for _, v := range s {
		s += v
	}
	c <- s
}

func main() {
	s := []int{7,2,8,-9,4,0}
	c := make(chan int)
	go sum(s[:len(s)/2], c)
	go sum(s[len(s)/2:], c)
	x, y := <-c, <-c
	fmt.Println(x,y,x+y)
}
