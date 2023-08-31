package Micrograd_Java;
import java.util.ArrayList;
import java.util.List;

public class Value {
	String label="";
	double data=0.0;
	double grad=0.0;
	String op="";
	List<Value> childrens = new ArrayList<>(); // childrens is a list of all previous values that resulted in the current Value
	
	
	public Value(String label,String op,double data,List<Value> childrens) { // this constructer is for returning Value objects from the mathematical operations
		this.label=label;
		this.op=op;
		this.data=data;
		this.childrens=childrens;
		
	}
	
	public Value(String label,double data) { // this constructer is for building Value objects, it dosen't need an operation string 
		this.label=label;
		this.data=data;
		
	}
	public Value add (Value v1) {
		List<Value> childrenList = new ArrayList<>();
		childrenList.add(v1);
		childrenList.add(this);
		Value x= new Value(this.label+"+"+v1.label, "+", this.data+v1.data,childrenList);
		// you chould add the line that would do the backward step using the backwardAdd method
		return x;
	}
	

	
	public Value sub (Value v1) {
		List<Value> childrenList = new ArrayList<>();
		childrenList.add(v1);
		childrenList.add(this);
		Value x=  new Value(this.label+"-"+v1.label, "-", this.data-v1.data,childrenList);
		// before returning x you should perform the backpro
		return x;
	}
	
	public Value mul (Value v1) {
		List<Value> childrenList = new ArrayList<>();
		childrenList.add(v1);
		childrenList.add(this);
		Value x= new Value(this.label+"*"+v1.label, "*", this.data*v1.data,childrenList);
		//x.grad= x.backmul(this, v1);
		return x;
	}
	
	public double backtanh(Value v) {
		// I called the backtanh  method with the outputed object from the tanh operation passing the object that we used to calculated tanh as parameter
		double out=1-(((1-Math.exp(-2*v.data))/(1+Math.exp(-2*v.data)))*((1-Math.exp(-2*v.data))/(1+Math.exp(-2*v.data))));
		return out*this.grad;	
	}
	public Value tanh() {
		List<Value> childrenList = new ArrayList<>();
		childrenList.add(this);
		double out=((1-Math.exp(-2*this.data))/(1+Math.exp(-2*this.data)));
		Value x= new Value("tanh("+this.data+")","tanh",out,childrenList);
		x.grad=x.backtanh(this);
		return x;
	}
	
	public Value Relu() {
	    double reluValue = this.data < 0 ? 0 : this.data;
	    Value x = new Value("Relu", reluValue);
	    return x;
	}
	

	
    @Override
    public String toString() {
        return "Value[label=" + label + ", data=" + data + ", grad=" + grad + ", op=" + op + "\nchildren"+childrens+"]";
    }
	
}
