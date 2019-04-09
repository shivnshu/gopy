package mypkg

import "fmt"

func main() {
  a := 1
  a += 3
  go func(b int) {
    c := 4
    fmt.Println(b)
  }(2)
}
