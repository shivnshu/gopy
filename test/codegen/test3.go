package mypkg

import "fmt"

func main() {
  a := 1
  if (a == 11) {
    fmt.Printf("if\n")
  }
  else  if (a == 12) {
    fmt.Printf("else if\n")
  }
  else {
    fmt.Printf("else\n")
  }
//  var a *int
//  b := 10
//  a = &b
}
