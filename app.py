import streamlit as st


class Calculator:
    def __init__(self):
        self.price = 0.0
        self.amount = 0.0

    def get_price(self, price, amount):
        self.price = price
        self.amount = amount 
        net = (self.price / 1000) * self.amount
        return net

    def get_amount(self, price, amount):
        self.price = price
        self.amount = amount
        if self.price == 0:
            return 0.0
        net = (1000 / self.price) * self.amount
        return net


st.title("Price & Quantity Calculator")

calc = Calculator()

tab1, tab2 = st.tabs(["Calculate Price", "Calculate Quantity"])

with tab1:
    st.subheader("Calculate Price")
    price_input = st.number_input("Enter price/kg (₹)", min_value=0.0, value=100.0)
    grams_input = st.number_input("Enter amount in grams", min_value=0.0, value=500.0)
    
    total_price = calc.get_price(price_input, grams_input)
    st.success(f"Total Price: ₹{total_price:.2f}")

with tab2:
    st.subheader("Calculate Quantity")
    price_input2 = st.number_input("Enter price/kg (₹) ", min_value=0.0, value=100.0)
    money_input = st.number_input("Enter money for items (₹)", min_value=0.0, value=50.0)
    
    total_grams = calc.get_amount(price_input2, money_input)
    st.success(f"Quantity: {total_grams:.2f} grams")