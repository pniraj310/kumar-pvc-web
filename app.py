import streamlit as st

# Set the title of the page
st.set_page_config(page_title="Kumar PVC Panels", page_icon=":guardsman:", layout="wide")

# Add custom CSS styles for background and layout
st.markdown("""
    <style>
        body {
            background-image: url('https://images.unsplash.com/photo-1613545325278-3ba253a4d1eb');
            background-size: cover;
            background-attachment: fixed;
            color: #333;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        .main, .block-container {
            background-color: rgba(255, 255, 255, 0.9);
            padding: 20px;
            border-radius: 10px;
        }
        h1, h2, h3 {
            color: #0a3d62;
        }
        .product-card {
            background-color: #ffffff;
            padding: 15px;
            border-radius: 12px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            margin-bottom: 20px;
        }
        .product-card:hover {
            transform: translateY(-5px);
            transition: 0.3s ease-in-out;
        }
    </style>
""", unsafe_allow_html=True)

# Title Section
st.title("Kumar PVC Panels")
st.markdown("### Transform Your Space with Elegant PVC Panels ✨")
st.markdown("""
We bring you premium-quality decorative PVC panels that are perfect for interior beautification. Let your walls speak design!
""")

# Cart Display (moved up)
st.header("Your Cart")
if 'cart' in st.session_state and st.session_state.cart:
    total = 0
    for item in st.session_state.cart:
        st.write(f"{item['product']} - ₹{item['price']}")
        total += item['price']
    st.write(f"**Total**: ₹{total}")
    if st.button("Proceed to Checkout"):
        st.session_state.checkout = True
else:
    st.info("Your cart is empty.")

# Checkout Section
if st.session_state.get("checkout"):
    st.subheader("Checkout")
    name = st.text_input("Your Name")
    email = st.text_input("Email")
    address = st.text_area("Address")
    if st.button("Confirm Purchase"):
        st.success("Thank you for your purchase! We will contact you soon.")
        st.session_state.cart = []
        st.session_state.checkout = False

# Product Section
st.header("PVC Panel Designs")
products = {
    "Classic Design": ["https://images.unsplash.com/photo-1586201375761-83865001e31b", 1000],
    "Modern Design": ["https://images.unsplash.com/photo-1600585154205-3b5c86074ab6", 1200],
    "Artistic Design": ["https://images.unsplash.com/photo-1618221040161-2c9747d4bb53", 1500],
    "Geometric Patterns": ["https://images.unsplash.com/photo-1570129477492-45c003edd2be", 1350],
    "Wood Finish Panels": ["https://images.unsplash.com/photo-1613545324977-95bb1be2b30c", 1600],
    "Textured Panels": ["https://images.unsplash.com/photo-1598300057691-3f4d79f3c9b1", 1450]
}

cols = st.columns(3)
for i, (name, data) in enumerate(products.items()):
    with cols[i % 3]:
        st.markdown("<div class='product-card'>", unsafe_allow_html=True)
        st.image(data[0], caption=name, use_column_width=True)
        st.markdown(f"**Price**: ₹{data[1]} per square meter")
        if st.button(f"Add {name} to Cart", key=name):
            if 'cart' not in st.session_state:
                st.session_state.cart = []
            st.session_state.cart.append({"product": name, "price": data[1]})
        st.markdown("</div>", unsafe_allow_html=True)

# Contact Info
st.header("Contact Us")
st.markdown("""
**Vendor**: Dhiraj Patel  
**Shop**: Kumar PVC Panels  
**Address**: Pili Nadi, Nagpur  
**Phone**: 7666323894  
**Email**: pdheeraj351@gmail.com  
""")

# Footer
st.markdown("""
    <hr>
    <center>
        <p style="color:gray">&copy; 2025 Kumar PVC Panels. Designed with ❤️ for elegance and creativity.</p>
    </center>
""", unsafe_allow_html=True)
