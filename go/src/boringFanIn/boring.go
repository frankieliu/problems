package main
import "fmt"
import "time"
import "math/rand"

func main() {
	// Make a string channel
	c := fanIn(boring("aaa"), boring("bbb"))
	for i := 0; i < 5; i++ {
		fmt.Printf("%q\n", <-c)
	}
	fmt.Println("Done\n");
}

func fanIn(ch1, ch2 <-chan string) <-chan string {
	c := make(chan string)
	go func() { for {c <- <-ch1} }()
	go func() { for {c <- <-ch2} }()
	return c
}

func boring(msg string) <-chan string {
	c := make(chan string)
	go func() {
		for i :=0; ; i++ {
			c <- fmt.Sprintf("%s %d", msg, i)
			time.Sleep(time.Duration(rand.Intn(1e3)) * time.Millisecond)
		}
	}()
	return c
}
