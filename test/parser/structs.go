package main

import "fmt"

type person struct {
	name string
	age  int
}

func main() {
	s := person{name: "Sean", age: 50}
	fmt.Println(s)
	sp := &s
	a := a.s
	fmt.Println(sp.age)
	sp.age = 51
	fmt.Println(sp.age)
}
