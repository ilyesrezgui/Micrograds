import math 
class Value:

    def __init__(self,data,_children=(),_op='',label=''):
        self.grad=0 # this variable is used to keep track of derivative, being intialized to 0 mean that the gradient  has no effect on the output if we increase it decrease it
        self._backward= lambda: None
        self.data=data
        self._prev=set(_children)
        self._op = _op
        self.label=label

    def __repr__(self):
        #this is a built in method that allows you to print the vlaues of an object by simply calling it, in this case, when you create a value object from the Value class and you
        #initate it with a value1=Value(30) for example , when you call value(1) , it will return a string
        return f"Value(data={self.data})"
    # we defined this __add__ method , because python dosen't know how to add two Value objects, that is why we deined a method with __ so that when we use + python with internally call this method
    def __add__(self,other):
        out= Value(self.data+other.data,(self,other),'+',)
        def _backward():
            self.grad+=1.0*out.grad
            other.grad+=1.0*out.grad

        out._backward=_backward
        return out

    def __mul__(self,other):
        out= Value(self.data*other.data,(self,other),'*')
        def _backward():
            self.grad+=(other.data)*out.grad
            other.grad+=(self.data)*out.grad

        out._backward=_backward
        return out

    def tanh(self):
        x = self.data
        t = (math.exp(2*x) - 1)/(math.exp(2*x) + 1)
        out = Value(t, (self, ), 'tanh')
        def _backward():
            self.grad += (1 - t**2) * out.grad
        out._backward = _backward
        return out
    
    def backward(self):

            # topological order all of the children in the graph
            topo = []
            visited = set()
            def build_topo(v):
                if v not in visited:
                    visited.add(v)
                    for child in v._prev:
                        build_topo(child)
                    topo.append(v)
            build_topo(self)

            # go one variable at a time and apply the chain rule to get its gradient
            self.grad = 1
            for v in reversed(topo):
                v._backward()
    def __radd__(self, other): # other + self
        return self + other

    def __sub__(self, other): # self - other
        return self + (-other)

    def __rsub__(self, other): # other - self
        return other + (-self)

    def __rmul__(self, other): # other * self
        return self * other
    
    def __truediv__(self, other): # self / other
        return self * other**-1

    def __rtruediv__(self, other): # other / self
        return other * self**-1

    def __repr__(self):
        return f"Value(data={self.data}, grad={self.grad})"
    
    def Relu(self):
        out= self.data if self.data>0 else 0
        def _backward():
            self.out+= (self.data>0) * out.grad
        out._backward = _backward

            