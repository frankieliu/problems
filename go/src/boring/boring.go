package main
import "fmt"
import "time"
import "math/rand"

func main() {
	// Make a string channel
	c := make(chan string)
	go boring("aaa", c)
	for i := 0; i < 5; i++ {
		fmt.Printf("%q\n", <-c)
	}
	fmt.Println("Done\n");
}

func boring(msg string, c chan string) {
	for i :=0; ; i++ {
		c <- fmt.Sprintf("%s %d", msg, i)
		time.Sleep(time.Duration(rand.Intn(1e3)) * time.Millisecond)
	}
}
