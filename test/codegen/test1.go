package mypkg

import "fmt"

func test(a int, b int) (int, int) {
  c := 11
  fmt.Printf("%d and %d\n", a, b)
  return 12, 13
}

func main() {
  a := 10
  b, c := test(a, 11)
  fmt.Printf("Return %d and %d\n", b, c)
}
