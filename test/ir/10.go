package mypkg

import "fmt"

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
