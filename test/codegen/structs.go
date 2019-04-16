package main
// Not ruu

import "fmt"

var gg = 2

type person struct {
  age int
  name string
  k *int
  g int
  fp float
}

func test(p person) {
  p.age = 20
  p.fp = 5.5
}

func main() {
  var p person
  p = person{age: 10, name: "aaa"}
  age := p.age
  name := p.name
  fmt.printf("Age: %d, Name:%s\n", age, name)
  test(p)
  age = p.age
  name = p.name
  var i int
  i = 10
  var s *int
  s = &i
  p.k = s
  fmt.printf("Age: %d, Name:%s\n", age, name)
  s = p.k
  fmt.printf("%x\n", s)
  p.g = gg
  p_fp := p.fp
  fmt.float_print(p_fp)
}
