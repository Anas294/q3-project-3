import streamlit as st

st.title("🌎Unit converter app")
st.markdown("### convert length, weight and time instantly")
st.write("welcome select a category, enter  value and get the converted result in real-time")

category = st.selectbox("choose a category", {"Length", "Weight", "Time"})

def convert_units(category, value,unit):
    if category == "length":
        if unit == "Kilometers to Miles":
            return value * 0.621371
        elif unit == "Miles to Kilometers":
            return value / 0.621371
        
    elif category == "weight":
           if unit == "Kilograms to Pounds":
                return value * 2.20462
           if unit == "Pounds to Kilograms":
                return value / 2.20462
    elif category == "Time":
         if unit == "Seconds to Minutes":
              return value / 60
         elif unit == "Minutes to second":
              return value * 60
         elif unit == "Minutes to Hours":
              return value / 60
         elif unit == "Hours to Minutes":
              return value * 60
         elif unit == "Hours to Day":
              return value / 24
         elif unit =="Day to Hours":
              return value * 24
         return 0 
 
if category == "Length":
     unit = st.selectbox("🛹select conversation",{"Miles to Kilometers","Kilometers to Miles"})
elif category == "Weight":
     unit = st.selectbox("⚖ select conversation",{"Kilograms to pounds","Pounds to Kilograms"})
              
elif category == "Time":
     unit = st.selectbox("⏰ select conversation",{"seconds to Minutes","Minutes to second","Minutes to Hours","Hours to Minutes","Hours to Day","Day to Hours"})
       
value = st.number_input("enter the value to convert")

if st.button("convert"):
     result = convert_units(category, value, unit)
     st.success(f"The result is{result:.2f}")
    
     