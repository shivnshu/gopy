package main

import "fmt"

func test1(a int, b int) (int, int, int) {
  return a, b, a + b
}

func test2(a string) (string, int) {
  fmt.printf("local a = %s\n", a)
  return a, 10
}

func main () {
  a, b, sum := test1(1, 2)
  fmt.printf("a: %d, b: %d, sum: %d\n", a, b, sum)
  var str string
  var s int
  str, s = test2("my string")
  fmt.printf("Returned str: %s\n", str)
  fmt.printf("Returned s: %d\n", s)
  return
}
