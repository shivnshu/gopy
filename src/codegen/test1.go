package mypkg

import "fmt"

func main() {
  sum := 0
  for i := 0; i<10; i += 1 {
    sum += i
  }
  fmt.Printf("%d\n", sum)
}
