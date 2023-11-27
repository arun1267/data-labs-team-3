import streamlit as st
import joblib  # You need to import joblib to load the model



# Load the model
 # Example path to the model file
model = joblib.load("model_joblib")

# Rest of your Streamlit code where you use the loaded model...


# Streamlit app
def main():
    st.title("Gene Mutation")

    # Sidebar input for two numbers
    a = st.sidebar.text_input("Enter first number", 0)  # Assuming default value is 0
    b = st.sidebar.text_input("Enter second number", 0)  # Assuming default value is 0

    # Convert inputs to appropriate data type (int in this case)
    a = int(a)
    b = int(b)

    # Make prediction upon button press
    if st.sidebar.button("Predict"):
        prediction = model.predict(a, b)
        st.write(f'Sum: {prediction}')

# Call the Streamlit app
if __name__ == "__main__":
    main()
