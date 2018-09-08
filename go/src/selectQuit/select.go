package main
import (
	"fmt"
)

func fibonnaci(c, quit chan int) {
	x,y := 0,1
	for {
		select {
		case c <- x:
			x,y = y,x+y
		case <-quit:
			fmt.Println("quit")
			return
		}
	}
}
	
func main() {
	c := make(chan int)
	quit := make(chan int)
	go func() {
		count := 0
		for i := range c {
			fmt.Println(i)
			if count == 9 {
				quit <- 0
			}
			count++
		}
	}()
	fibonnaci(c, quit)
}
