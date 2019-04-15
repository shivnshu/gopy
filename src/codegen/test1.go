package mypkg

import "fmt"

type person struct {
	age int
	name string
}

func test(p *person) {
  //a := *p.name
}

func main() {
	sahil := person{name: "Sahil", age: 20}
  addr := &sahil
  test(addr)
/*  b := sahil.age*/
  //c := &sahil
  //fmt.printf("Age: %d\n", b)
  //sahil.age = 10
  //b = sahil.age
  /*fmt.printf("New Age: %d\n", b)*/
}
