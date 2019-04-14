package main

import "fmt"

var a int = 2
var aa int = 3
var aaa int = a + aa
const (
  b = 123
  c = "string1"
)
var d int
var e string

func test() {
  fmt.printf("d = %d\n", d)
  e = "string2"
  fmt.printf("aa = %d, aaa = %d\n", aa, aaa)
}

func main() {
  fmt.printf("a = %d, b = %d, c = %s\n", a, b, c)
  d = 4
  test()
  fmt.printf("e = %s\n", e)
}
