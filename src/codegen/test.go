package mypkg

import "fmt"

type person struct {
	age  int
	name string
}

func test(s person) {
	s.age = 10
}

func main() {
	//var sahil person
	sahil := person{name: "Sahil", age: 20}
	age := sahil.age
	fmt.printf("Age: %d\n", age)
	sahil.age = 30
	age = sahil.age
	fmt.printf("New Age: %d\n", age)
	test(sahil)
	age = sahil.age
	fmt.printf("Age: %d\n", age)
}
