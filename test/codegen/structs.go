package main

import "fmt"

type person struct {
  name string
  age int
}

func test(p person) {
  p.name = "Don"
}

func main() {
  var p person
  p = person{age: 10, name: "CR"}
  age := p.age
  name := p.name
  fmt.printf("%d %s\n", age, name)
  p.age = 11
  test(p)
  age = p.age
  name = p.name
  fmt.printf("%d %s\n", age, name)
}
