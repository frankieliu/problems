package main
import (
	"fmt"
	"math"
)

type Vertex struct {
	X,Y float64
}

func Abs(v Vertex) float64 {
	return math.Sqrt(v.X*v.X + v.Y*v.Y)
}

func Scale(v Vertex, f float64) Vertex {
	v.X = v.X * f
	v.Y = v.Y * f
	return v
}

func main() {
	v := Vertex{3,4}
	v2 := Scale(v, 10)
	fmt.Println(Abs(v2))
}
