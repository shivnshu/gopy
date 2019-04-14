package mypkg

import "fmt"

func main() {
  a := 1
  b := 2
  x := &a
  fmt.printf("a: %d\n", a)
  *x = 3
  fmt.printf("a: %d\n", a)
  y := *x
  fmt.printf("y: %d\n", y)
  z := &b
  tmp := *x
  fmt.printf("tmp: %d\nb: %d\n", tmp, b)
  *z = tmp
  fmt.printf("b: %d\n", b)
}
