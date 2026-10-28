# =====================================================
# StayEase - Hotel Booking Cost Calculator
# College project: Python Programming for Business Students
# NOTE: All prices and policies are SAMPLE assumptions.
# This is a cost estimator, not a real booking system.
# =====================================================

# Section 1: Import Streamlit (we call it "st" to keep the code short)
import streamlit as st

# Section 2: Set up the browser tab title and icon
st.set_page_config(page_title="StayEase plan your stay know your price")

# Section 3: Show the main heading and a short introduction
st.title(" StayEase - Hotel Booking Cost Calculator")
st.write("Choose your room and extras below to estimate the cost of your stay.")

# Section 4: Dictionary of room types and their price per night (in rupees)
# A dictionary stores pairs: room name (key) -> price (value)
room_prices = {
    "Standard Room": 2500,
    "Deluxe Room": 4000,
    "Suite": 6500
}

# Prices of the extra services (stored in variables so they are easy to change)
breakfast_price = 500      # per guest, per night
extra_bed_price = 1000     # per night
late_checkout_price = 500  # once per booking

# Section 5: Dropdown for room type (list of room names comes from the dictionary)
room_type = st.selectbox("Choose your room type", list(room_prices.keys()))

# Section 6: Number of nights (whole number, 1 to 30)
nights = st.number_input("Number of nights (1 to 30)", min_value=1, max_value=30, value=1, step=1)

# Section 7: Number of guests (whole number, 1 to 10)
guests = st.number_input("Number of guests (1 to 10)", min_value=1, max_value=10, value=1, step=1)

# Sections 8, 9 and 10: Checkboxes. Each one gives True (ticked) or False (not ticked)
want_breakfast = st.checkbox("Breakfast (₹500 per guest per night)")
want_extra_bed = st.checkbox("Extra bed (₹1,000 per night)")
want_late_checkout = st.checkbox("Late checkout (₹500 once per booking)")

# Section 17: Check the input first, so the app never crashes on bad values
if nights < 1 or nights > 30:
    st.error("Number of nights must be between 1 and 30.")
elif guests < 1 or guests > 10:
    st.error("Number of guests must be between 1 and 10.")
else:
    # Section 11: Room cost = price per night x number of nights
    room_price_per_night = room_prices[room_type]
    room_cost = room_price_per_night * nights

    # Section 12: Cost of optional services (start at 0, add only if ticked)
    breakfast_cost = 0
    extra_bed_cost = 0
    late_checkout_cost = 0

    if want_breakfast:
        breakfast_cost = breakfast_price * guests * nights  # depends on guests AND nights
    if want_extra_bed:
        extra_bed_cost = extra_bed_price * nights           # depends on nights only
    if want_late_checkout:
        late_checkout_cost = late_checkout_price            # charged only once

    services_cost = breakfast_cost + extra_bed_cost + late_checkout_cost

    # Section 13: Subtotal = room cost + services (the discount is applied to this)
    subtotal = room_cost + services_cost

    # Section 14: Choose the discount percentage using the number of nights
    if nights <= 2:
        discount_percent = 0    # 1-2 nights: no discount
    elif nights <= 4:
        discount_percent = 5    # 3-4 nights: 5% discount
    else:
        discount_percent = 10   # 5-30 nights: 10% discount

    # Section 15: Discount amount and final total
    discount_amount = subtotal * discount_percent / 100
    final_total = subtotal - discount_amount

    # Section 16: Show the itemised price breakdown and the final total
    st.subheader("Your Price Breakdown")
    st.write(f"Room: {room_type} - ₹{room_price_per_night:,.2f} x {nights} night(s) = ₹{room_cost:,.2f}")
    st.write(f"Breakfast: ₹{breakfast_cost:,.2f}")
    st.write(f"Extra bed: ₹{extra_bed_cost:,.2f}")
    st.write(f"Late checkout: ₹{late_checkout_cost:,.2f}")
    st.write(f"Subtotal: ₹{subtotal:,.2f}")
    st.write(f"Discount ({discount_percent}%): - ₹{discount_amount:,.2f}")
    st.success(f"Final Total: ₹{final_total:,.2f}")
