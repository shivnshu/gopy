package mypkg
import "fmt"

func A(x int, y int) int {
	if (x==0) {
		return y+1
	}
	else if (y==0) {
		tmp := A(x-1, 1)
		return tmp
	}
	else {
    sec := A(x, y-1)
		tmp := A(x-1, sec)
    return tmp
	}
}

func main () {
	s := A(2,1)
	fmt.printf("%d\n", s)
}
