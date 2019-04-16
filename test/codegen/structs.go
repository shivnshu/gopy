package main

import "fmt"

type person struct {
  name string
  age int
}

func main() {
  var p person
  p = person{age: 10, name: "CR"}
  age := p.age
  name := p.name
  fmt.printf("%s, %d\n", age, name)
}
