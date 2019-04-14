package mypkg

import "fmt"

type person struct {
	age int
	name string
}

const a = 5

func main() {
	sahil := person{name: "Sahil", age: 20}
  b := sahil.age
  fmt.printf("Age: %d\n", b)
}
