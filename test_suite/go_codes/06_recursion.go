package main

import "fmt"

func factorial(a int) int {
	if (a == 0) {
		return 1
	}
  i := factorial(a-1)
	return a + i
}

func main() {
  ans := factorial(10)
	fmt.printf("%d\n", ans)
}
