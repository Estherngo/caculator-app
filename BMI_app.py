w=input("what is your weight\n")
w=float(w)
h=input("what is your height in meters\n")
h=float(h)
def BMI_calc(w,h):
    BMI=(w/(h**2))
    BMI=round(BMI,1)
    if BMI < 18.5:
        print(f"Your BMI IS :{BMI}\nunderweight")
    elif 18.4<BMI<25:
        print("f Your BMI is :{BMI}\nnormal")
    elif 24.9<BMI<30:
        print (f"Your BMI is :{BMI}\noverweight ")
        
    elif 34.9<BMI< 40:
        print(f" Your BMI is : {BMI}\nclass 2 obesity")
    else:
        print (f"Your BMI is : {BMI}\nEstreme obesity")
    
    
BMI_calc(w,h)
        
            
    
