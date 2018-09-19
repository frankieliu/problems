package main
import "fmt"
import "time"
import "math/rand"

type Message struct {
	str string
	wait chan bool
}

// Note this works because msg2 will have to finish
// before msg1 is released

func main() {

	// Make a string channel
	c := fanIn(boring("aaa"), boring("bbb"))

	for i := 0; i < 5; i++ {

		// Note we don't know who comes first here
		// so we could end up with:
		// aaa, bbb : the order doesn't matter here
		// bbb, aaa : but the next two must contain aaa and bbb
		
		msg1 := <-c; fmt.Println(msg1.str)
		msg2 := <-c; fmt.Println(msg2.str)
		msg1.wait <- true // release msg1
		msg2.wait <- true // release msg2
	}
	
	fmt.Println("Done\n");
}

func fanIn(ch1, ch2 <-chan Message) <-chan Message {
	c := make(chan Message)
	go func() {
		for {
			select {
			case s := <-ch1: c <- s
			case s := <-ch2: c <- s
			}
		}
	} ()
	return c
}

func boring(msg string) <-chan Message {
	c := make(chan Message)
	waitForIt := make(chan bool)

	go func() {
		for i :=0; ; i++ {
			c <- Message{fmt.Sprintf("%s %d", msg, i), waitForIt}
			time.Sleep(time.Duration(rand.Intn(1e3)) * time.Millisecond)
			<-waitForIt
		}
	}()
	return c
}
