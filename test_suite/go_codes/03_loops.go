package main

import "fmt"

func main() {
	i := 0
  j := 0
	for i=0; i < 10; i+=1 {
		for j = 0; j < 20; j += 1 {
			fmt.printf("%d %d, ", i, j)
		}
		fmt.printf("\n")
	}
}
