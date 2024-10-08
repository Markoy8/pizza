import streamlit as st
import math

# Function to compute ingredients based on area
def calculate_ingredients(area, height):

    WATER_PERCENTAGE = 80
    SALT_PERCENTAGE = 2
    YEAST_PERCENTAGE = 1.2
    OIL_PERCENTAGE = 2.6
    MALT_PERCENTAGE = 1

    SUM_PERCENTAGE = WATER_PERCENTAGE + SALT_PERCENTAGE + YEAST_PERCENTAGE + OIL_PERCENTAGE + MALT_PERCENTAGE
    
    total_weight = area * height

    flour = total_weight * (100/(SUM_PERCENTAGE + 100))
    water = flour * WATER_PERCENTAGE / 100
    salt = flour * SALT_PERCENTAGE / 100
    yeast = flour * YEAST_PERCENTAGE / 100
    oil = flour * OIL_PERCENTAGE / 100
    malt = flour * MALT_PERCENTAGE / 100
    
    return flour, water, salt, yeast, oil, malt

# Function to display the procedure
def display_procedure(flour, water, salt, yeast, sauce, cheese):
    st.markdown("### Pizza Making Procedure")
    st.markdown(f"1. **Prepare the Dough**: In a bowl, mix {flour:.1f} grams of flour with {water:.1f} ml of water, "
                f"{salt:.1f} grams of salt, and {yeast:.1f} grams of yeast. Knead until smooth and elastic.")
    st.markdown("2. **Let the Dough Rise**: Cover the dough and let it rise for 1-2 hours.")
    st.markdown(f"3. **Prepare the Sauce**: Use {sauce:.1f} grams of tomato sauce (or your preferred sauce).")
    st.markdown(f"4. **Spread the Dough**: Roll the dough out to your desired shape and thickness.")
    st.markdown(f"5. **Add Sauce and Cheese**: Spread the sauce evenly and sprinkle {cheese:.1f} grams of cheese on top.")
    st.markdown("6. **Bake**: Bake in a preheated oven at 220°C (430°F) for about 10-15 minutes, or until golden brown.")
    st.markdown("7. **Enjoy your pizza!**")

def transform_chosen_height(chosen_height):
    if chosen_height == 'Thin':
        return 0.45
    if chosen_height == 'Medium':
        return 0.55
    if chosen_height == 'Thick':
        return 0.65


# Streamlit App
st.title("Pizza Ingredient Calculator")
st.markdown("Calculate the ingredients for a homemade pizza based on its shape and size!")

st.sidebar.header("Pizza Settings")
st.sidebar.markdown("### Choose the height of the pizza:")

heights = ['Thin', 'Medium', "Thick"]
chosen_height = st.sidebar.selectbox("Select desired height of your pizza", heights)
height = transform_chosen_height(chosen_height)


# Load images for buttons
rectangular_img = "https://media-assets.lacucinaitaliana.it/photos/61fb0cea67a08706394daa8a/16:9/w_1920,c_limit/pizza-in-teglia-alla-romana-ricetta-originali-preparazione-consigli-la-cucina-italiana.jpg"
circular_img = "https://www.tavolartegusto.it/wp/wp-content/uploads/2018/03/pizza-fatta-in-casa-buona-come-in-pizzeria-tutti-i-segreti-Ricetta-Pizza-fatta-in-casa-1-1.jpg"

st.sidebar.markdown("### Choose the shape of the pizza:")
shapes = ['Rectangle', 'Circle']
chosen_shape = st.sidebar.selectbox("Select shape of your pan", shapes)


# Add height selection buttons    
            
if chosen_shape == 'Rectangle':

    st.sidebar.image(rectangular_img, width=500)

    # Input for rectangle dimensions
    length = st.sidebar.number_input("Enter the length of the pizza (in cm):", min_value=30.0, step=0.5)
    width = st.sidebar.number_input("Enter the width of the pizza (in cm):", min_value=40.0, step=0.5)

    if length and width:
        # Calculate area for rectangle
        area = length * width
        st.write(f"The area of your rectangular pizza is: {area:.2f} cm²")

        # Calculate ingredients
        flour, water, salt, yeast, oil, malt = calculate_ingredients(area, height)

elif chosen_shape == 'Circle':

    st.sidebar.image(circular_img, width=500)

    radius = st.sidebar.number_input("Enter the radius of the pizza (in cm):", min_value=5.0, step=0.5)

    if radius:
        # Calculate area for circle (πr²)
        area = math.pi * (radius ** 2)
        st.write(f"The area of your circular pizza is: {area:.2f} cm²")

        # Calculate ingredients
        flour, water, salt, yeast, oil, malt = calculate_ingredients(area, height)

# Display ingredient amounts
st.markdown("# Ingredients for Your Pizza:")
st.markdown(f"## 🌾Flour: {flour:.1f} grams")
st.write(f"## 💧Water: {water:.1f} ml")
st.write(f"## 🧂Salt: {salt:.1f} grams")
st.write(f"## 🦠Yeast: {yeast:.1f} grams")
st.write(f"## 🫒Oil: {oil:.1f} grams")
st.write(f"## 🌿Malt: {malt:.1f} grams")

# Show procedure
#display_procedure(flour, water, salt, yeast, oil, malt)
