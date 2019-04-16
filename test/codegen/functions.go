package main

import "fmt"

func test1(a int, b int) (int, int, int) {
  return a, b, a + b
}

func test2(a string, b float) (string, int) {
  fmt.printf("local a = %s\n", a)
  fmt.float_print(b)
  return a, 10
}

func main () {
  a, b, sum := test1(1, 2)
  fmt.printf("a: %d, b: %d, sum: %d\n", a, b, sum)
  var str string
  var s int
  str, s = test2("my string", 3.4)
  fmt.printf("Returned str: %s\n", str)
  fmt.printf("Returned s: %d\n", s)
  return
}
