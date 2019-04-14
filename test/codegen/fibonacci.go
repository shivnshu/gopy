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
  x_1 := fibonacci(x-1)
  x_2 := fibonacci(x-2)
  res := x_1 + x_2
	return res
}

func main() {
	var num int = fibonacci(12)
  fmt.printf("Answer: %d\n", num)
}
