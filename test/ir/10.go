package mypkg

import "fmt"

const (
  z = 10
  y = 11
)

func fibonacci(x int) int {
	if (x <= 1) {
		return 1
	}
	return fibonacci(x-1) + fibonacci(x-2)
}

func main() {
	var num int = fibonacci(5)
	fmt.Println(num)
}
