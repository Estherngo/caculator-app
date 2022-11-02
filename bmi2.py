import streamlit as st
w=st.sidebar.number_input("what is your weight\n",step=1)
w=float(w)
h=st.sidebar.number_input("what is your height in meters\n")
st.sidebar.image('unicast logo2-2.JPG')
st.selectbox("choose your gender", ["Male", "Female"])

if st.button('calculate'):
    BMI=(w/(h**2))
    BMI=round(BMI,1)
    if BMI < 18.5:
        st.write(f"Your BMI IS :{BMI}\nunderweight")
    elif 18.4<BMI<25:
        st.write("f Your BMI is :{BMI}\nnormal")
    elif 24.9<BMI<30:
        st.write(f"Your BMI is :{BMI}\noverweight ")
        
    elif 34.9<BMI< 40:
        st.write (f" Your BMI is : {BMI}\nclass 2 obesity")
    else:
        st.write (f"Your BMI is : {BMI}\nEstreme obesity")
    
    

        
