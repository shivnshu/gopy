package mypkg

import "fmt"

type person struct {
	age  int
	name string
}

func test(a int, b int, c int, d int, e int, f int, g int, h int){
	fmt.printf("a=%d\n", a)
	fmt.printf("b=%d\n", b)
	fmt.printf("c=%d\n", c)
}

func main() {
	a := 1
	b := 2
	c := 3
	d := 4
	e := 5
	f := 6
	g := 7
	h := 8
	test(a,b,c,d,e,f,g,h)
}
