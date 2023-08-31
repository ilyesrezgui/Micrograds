import streamlit as st
from PIL import Image
from io import BytesIO
from graphviz import Source
from Value import Value
from Micrograd_Python.tracegraph import draw_dot

def main():
    st.title("Manual backpropagation on a single neuron ")

    # Create input boxes for the values
    a_input = st.number_input("Enter value for 'x1':", value=0.0)
    b_input = st.number_input("Enter value for 'x2':", value=0.0)
    c_input = st.number_input("Enter value for 'w1':", value=0.0)
    f_input = st.number_input("Enter value for 'w2':", value=0.0)
    r_input = st.number_input("Enter value for 'bias':", value=0.0)

    # Create a button to generate and display the graph
    if st.button("Generate and Display Graph"):
        # Create Value objects using the entered values
        a = Value(a_input, label='x1')
        b = Value(b_input, label='x2')
        w1 = Value(c_input, label='w1')
        w2 = Value(f_input, label='w2')
        r = Value(r_input, label='bias')

        # Define your graph computation
        e = a * w1
        e.label = 'x1*w1'
        d = b*w2
        d.label = 'x2*w2'
        L = e+d
        L.label = 'x1*w1+x2*w2'
        bb=L+r
        bb.label = 'x1*w1+x2*w2+b'
        res=bb.tanh()
        res.label='tanh(x1*w1+x2*w2+bias)'
        st.text("Before Backpropagation")
        gr = draw_dot(res)
        # Get the PNG image data as BytesIO object
        png_bytes = gr.pipe(format='png')
        png_io = BytesIO(png_bytes)
        st.image(png_io, caption="Generated Graph", use_column_width=True)

        res.backward()

        st.text("After Backpropagation")
        # Generate the graphviz visualization
        gr2 = draw_dot(res)
        
        # Get the PNG image data as BytesIO object
        png_bytes2 = gr2.pipe(format='png')
        png_io = BytesIO(png_bytes2)
        
        # Display the generated PNG image
        st.image(png_io, caption="Generated Graph", use_column_width=True)

if __name__ == "__main__":
    main()
