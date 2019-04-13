package mypkg

import "fmt"

const (
  p = 1
  q = 2
  r = "acs"
)
var b int
var c int
var st string

func test(p int, sl string) string {
  fmt.Printf("local %d %s and global %d and %s\n", p, sl, c, st)
  x := r
  fmt.Printf(x)
  return "ret_str"
}

func main() {
  c = 10
  st = "my str"
  ret_str := test(1, "local str")
  fmt.Printf(r)
  fmt.Printf(ret_str)
}

var d int
