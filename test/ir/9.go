package mypkg

import "fmt"

func factorial(x int) int {
  if (x < 1) {
    return 1
  }
  a := factorial(x-1)
  return x * a
}

func main() {
  out := factorial(10)
  fmt.Println(out)
}
