#include <stdio.h>
#include "calculator.c"


void print_float(float im){
	printf("float result: %f\n\n", im);
}


void print_int(int im){
	printf("int result: %d\n\n", im);
}


#define my_printf(X) _Generic((X), \
	float: print_float, \
	int: print_int, \
	default: print_float \
	) (X)


void	add_tests(void){
	int a = 3;
	int b = 4;
	int c = 50;
	float x = 3.9;
	float y = 4.7;

	printf("\n\t~~~ADD BLOCK~~~\n");
	printf("(%d + %d): \n", a, b); my_printf(add(a, b));
	printf("(%d + %d): \n", a, c); my_printf(add(a, c));
	printf("(%f + %f): \n", x, y); my_printf(add(x, y));
	printf("(%d + %f): \n", a, y); my_printf(add(a, y));
}

void	sub_tests(void){
	int a = 45;
	int b = 456;
	int c = -9;
	int d = 0;
	float x = 0.465;
	float y = 456.456;

	printf("\n\t~~~SUB BLOCK~~~\n");
	printf("(%d - %d): \n", a, b); my_printf(sub(a, b));
	printf("(%d - %d): \n", a, c); my_printf(sub(a, c));
	printf("(%d - %d): \n", b, d); my_printf(sub(b, d));
	printf("(%f - %f): \n", x, y); my_printf(sub(x, y));
	printf("(%f - %d): \n", x, b); my_printf(sub(x, b));
	printf("(%d - %f): \n", d, y); my_printf(sub(d, y));
}

void	mul_tests(void){
	int a = -86;
	int b = 4;
	int c = 4567;
	int d = 0;
	float x = 1.4;
	float y = -4.46;

	printf("\n\t~~~MUL BLOCK~~~\n");
	printf("(%d * %d): \n", a, b); my_printf(mul(a, b));
	printf("(%d * %d): \n", a, c); my_printf(mul(a, c));
	printf("(%d * %d): \n", b, d); my_printf(mul(b, d));
	printf("(%f * %f): \n", x, y); my_printf(mul(x, y));
	printf("(%f * %d): \n", x, b); my_printf(mul(x, b));
	printf("(%d * %f): \n", d, y); my_printf(mul(d, y));
}

void	div_tests(void){
	int a = 0;
	int b = 2;
	int c = -86;
	int d = 30;
	float x = 1.4;
	float y = -4.46;

	printf("\n\t~~~DIV BLOCK~~~\n");
	printf("(%d / %d): \n", a, b); my_printf(div(a, b));
	printf("(%d / %d): \n", c, d); my_printf(div(c, d));
	printf("(%d / %d): \n", b, d); my_printf(div(b, d));
	printf("(%f / %f): \n", x, y); my_printf(div(x, y));
	printf("(%f / %d): \n", x, b); my_printf(div(x, b));
	printf("(%d / %f): \n", a, y); my_printf(div(a, y));
}


int	main(void){
	add_tests();
	sub_tests();
	mul_tests();
	div_tests();
}