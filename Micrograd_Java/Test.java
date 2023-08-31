package Micrograd_Java;

public class Test {

	public static void main(String[] args) {
		
		Value v1= new Value("a",3.5);
		Value v2= new Value("b",3);
		Value x=v1.add(v2);
		System.out.println(x);

	}
}
