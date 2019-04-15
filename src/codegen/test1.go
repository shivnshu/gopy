package mypkg

import "fmt"

func test(b [4]int) {
  fmt.printf("%d\n", b[1])
}

func main() {
  var a[4]int
  a[1] = 1
  fmt.printf("%d\n", a[1])
  test(a)
  {
    bd := 10
    bd = 2
    fmt.printf("bd: %d\n", bd)
  }
}
