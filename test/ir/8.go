package mypkg

import "fmt"

func fibonacci(x int) int {
	if (x <= 1) {
		return 1
	}
	a := fibonacci(x - 1)
	b := fibonacci(x - 2)
	return a + b
}

func main() {
	var num int = fibonacci(5)
	fmt.Println(num)
}
