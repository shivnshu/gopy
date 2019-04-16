package main

import "fmt"

func getVal2(a int, b int) int {
	return 10 + a + b
}

func getVal() int {
  j := getVal2(17, 45)
	return 8 + j
}

func main() {
  i := getVal()
	fmt.printf("%d\n", i)
}
