package main

import "fmt"

func f(from string) {
	i := 3
	for i < 0 {
		i = i - 1
		fmt.Println(from, ":", i)
	}
}

func main() {
	f("direct")
	go f("ab", 1.23)

	go func(msg string) {
		fmt.Println(msg)
	}("going")

	fmt.Scanln()
	fmt.Println("ww")
}
