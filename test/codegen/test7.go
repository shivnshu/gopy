package mypkg

import "fmt"

func main() {
	sum := 0
	for i := 0; i <= 20; i += 1 {
		sum += i
		if sum < 100 {
			fmt.printf("%d\n", sum)
			continue
		}
		fmt.printf("aa\n")
	}
}
