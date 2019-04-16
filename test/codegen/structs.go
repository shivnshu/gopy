package main

import "fmt"

type person struct {
  age int
  name string
}

func test(p person) {
  p.age = 20
}

func main() {
  p := person{age: 10, name: "aaa"}
  age := p.age
  name := p.name
  fmt.printf("Age: %d, Name:%s\n", age, name)
  test(p)
  age = p.age
  name = p.name
  fmt.printf("Age: %d, Name:%s\n", age, name)
}
