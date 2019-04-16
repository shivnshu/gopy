package main
// Not ruu

import "fmt"

var gg = 2

type person struct {
  age int
  name string
  k *int
  g int
}

func test(p person) {
  p.age = 20
}

func main() {
  var p person
  p = person{age: 10, name: "aaa"}
  age := p.age
  //name := p.name
  //fmt.printf("Age: %d, Name:%s\n", age, name)
  //test(p)
  //age = p.age
  //name = p.name
  //var i int
  //i = 10
  //var s *int
  //s = &i
  //p.k = s
  //fmt.printf("Age: %d, Name:%s\n", age, name)
  //s = p.k
  //fmt.printf("%x", s)
  //p.g = gg
}
