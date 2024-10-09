import streamlit as st
import math
import pandas as pd

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

# Function to color rows alternatively
def highlight_rows(row):
    return ['background-color: #d6dbdf' if row.name % 2 == 0 else 'background-color: #ffffff' for _ in row]

def display_ingredients(flour, water, salt, yeast, oil, malt):

    ingredients = {
        "Ingredient": ["🌾Flour", "💧Water", "🧂Salt", "🦠Yeast", "🫒Oil", "🌿Malt"],
        "Quantity (gr)": [f"{x:.1f}" for x in [flour, water, salt, yeast, oil, malt]]
    }

    # style
    th_props = [
        ('font-size', '18px'),
        ('text-align', 'center'),
        ('font-weight', 'bold'),
        ('color', '#6d6d6d'),
        ('background-color', '#f7ffff')
    ]
                                
    td_props = [
        ('font-size', '18px'),
        ('color', '#000000')
    ]
                                    
    styles = [
        dict(selector="th", props=th_props),
        dict(selector="td", props=td_props)
    ]

    df_ingredients = pd.DataFrame.from_dict(ingredients)
    styled_df = df_ingredients.style.set_properties(**{'text-align': 'center'}).set_table_styles(styles).apply(highlight_rows, axis=1)
    st.table(styled_df)

def show_flour_details(flour):
     
    SEMOLA_PERCENTAGE = 10
    FARRO_PERCENTAGE = 18
    TYPE_2_PERCENTAGE = 8
    TYPE_00_PERCENTAGE = 36
    TYPE_0_PERCENTAGE = 28 

    flours = {
        "Flour type": ["Semola", "Farro", "Buratto (2)", "00", "0"],
        "Quantity (gr)": [
            int(SEMOLA_PERCENTAGE * flour / 100), 
            int(FARRO_PERCENTAGE * flour / 100), 
            int(TYPE_2_PERCENTAGE * flour / 100), 
            int(TYPE_00_PERCENTAGE * flour / 100), 
            int(TYPE_0_PERCENTAGE * flour / 100)
            ]
    }

    # style
    th_props = [
        ('font-size', '18px'),
        ('text-align', 'center'),
        ('font-weight', 'bold'),
        ('color', '#6d6d6d'),
        ('background-color', '#f6ddcc')
    ]
                                
    td_props = [
        ('font-size', '18px'),
        ('color', '#000000')
    ]
                                    
    styles = [
        dict(selector="th", props=th_props),
        dict(selector="td", props=td_props)
    ]

    df_flours = pd.DataFrame.from_dict(flours)
    styled_df = df_flours.style.set_properties(**{'text-align': 'center'}).set_table_styles(styles).apply(highlight_rows, axis=1)
    st.table(styled_df)

# Streamlit App
st.title("Pizza Ingredients Calculator")
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

    st.sidebar.markdown("### Enter main dimension of your pan")

    # Input for rectangle dimensions
    length = st.sidebar.number_input("Enter the length of the pizza (in cm):", min_value=30, step=5)
    width = st.sidebar.number_input("Enter the width of the pizza (in cm):", min_value=40, step=5)

    if length and width:
        # Calculate area for rectangle
        area = length * width
        st.write(f"The area of your rectangular pizza is: {area:.2f} cm²")

      

elif chosen_shape == 'Circle':

    st.sidebar.image(circular_img, width=500)

    st.sidebar.markdown("### Enter main dimension of your pan")

    radius = st.sidebar.number_input("Enter the DIAMETER of the pan (in cm):", min_value=5, step=5) / 2

    if radius:
        # Calculate area for circle (πr²)
        area = math.pi * (radius ** 2)
        st.write(f"The area of your circular pizza is: {area:.2f} cm²")


# Custom CSS for a big button
st.markdown(
    """
    <style>
    div.stButton > button {
        font-size: 24px;
        padding: 15px 30px;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True
)

# Emoji button
if st.button("🚀 Compute Ingredients"):
    # Calculate ingredients
    flour, water, salt, yeast, oil, malt = calculate_ingredients(area, height)
    
    display_ingredients(flour, water, salt, yeast, oil, malt)
    

    # Hidden section, for now collapsed
    hidden_section = st.expander("Show Flour details")
    with hidden_section:
        show_flour_details(flour)
# Show procedure
#display_procedure(flour, water, salt, yeast, oil, malt)
