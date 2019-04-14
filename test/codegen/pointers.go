package mypkg

import "fmt"

func main() {
  var a int
  a = 10
  var b *int
  b = &a
  var c int
  *b = 11
  fmt.printf("%d\n", a)
}
