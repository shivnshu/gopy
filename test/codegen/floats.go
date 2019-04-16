package main

import "fmt"

func main() {
  var i float
  i = 10.1
  j := 1.2
  k := i + j
  m := i/j
  o := 1
  q := 1.2 - o

  fmt.float_print(i)
  fmt.float_print(j)
  fmt.float_print(k)
  fmt.float_print(m)
  fmt.float_print(q)
}
