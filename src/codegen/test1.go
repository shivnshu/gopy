package mypkg

import "fmt"

func test(b [4]int, c int) {
  fmt.printf("%d\n", b[1])
  fmt.printf("%d\n", c)
}

func sin(a float) {
  var ans = 0
  var accum float = 1
  var flag bool = true
  for i:=0;i<5;i+=1 {
    if (flag == true) {
      accum += a * a / 2
    } else {
    }
  }
}

func main() {
  var a[4]int
  a[1] = 1
  fmt.printf("%d\n", a[1])
  test(a, 11)
  {
    bd := 10
    bd = 2
    fmt.printf("bd: %d\n", bd)
  }
}
