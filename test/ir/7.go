package mypkg

func test(a int, b float) (int, int) {
	c := a + b
	return c, a
}

func main() {
	a, b := test(1, 2.3)
}
