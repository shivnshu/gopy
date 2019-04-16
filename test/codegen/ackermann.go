package mypkg
import "fmt"

func A (x int, y int) int{
	if x==1 {
		return y+1
	}
	else if y==0 {
		tmp := A(x-1, 1)
		return tmp
	}
	else {
		tmp := A(x-1, A(x, y-1))
	}
}

func main () {
	s := A (2,1)
	fmt.printf("%d\n", s)
}