import streamlit as st

st.write('# FU CALC')
number1 = st.number_input('number 1')

# Define options for the selectbox
options = st.selectbox('Select operation', ['add', 'minus', 'divide', 'multiply']) 
number2 = st.number_input('number2')

# Calculate results
add = number1 + number2
minus = number1 - number2

# Handle potential division by zero
if number2 != 0:
    divide = number1 / number2
else:
    divide = "Division by zero!"  # Provide a message when division by zero occurs

multiply = number1 * number2

# Display results based on selected option
if options == 'add':
    st.write('# Answer is', add)
elif options == 'minus':
    st.write('# Answer is', minus)
elif options == 'divide':
    st.write('# Answer is', divide)  # Display the result or the error message
elif options == 'multiply':
    st.write('# Answer is', multiply)
else :
    st.write('# Answer is', multiply)
