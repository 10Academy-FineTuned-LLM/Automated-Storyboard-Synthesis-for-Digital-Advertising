elements = [
    "Logo", "Call-To-Action (CTA) Button", "Icon", "Product Image", "Text Elements",
    "Infographic", "Banner", "Illustration", "Photograph", "Mascot", "Testimonial Quotes",
    "Social Proof", "Seal or Badge", "Graphs and Charts", "Decorative Elements",
    "Interactive Elements", "Animation Frames", "Coupon or Offer Code",
    "Legal Disclaimers or Terms", "Contact Information", "Map or Location Image", "QR Code"
]

# Assuming the same list of elements
elements_horizontal_placement = {
    "Left": ["Logo", "Icon", "Product Image", "Text Elements", "Infographic", "Mascot", "Graphs and Charts"],
    "Mid": ["Call-To-Action (CTA) Button", "Banner", "Illustration", "Photograph", "Testimonial Quotes", "Interactive Elements", "Animation Frames"],
    "Right": ["Social Proof", "Seal or Badge", "Decorative Elements", "Coupon or Offer Code", "Legal Disclaimers or Terms", "Contact Information", "Map or Location Image", "QR Code"]
}

# Elements that can fit in more than one category based on design needs
flexible_horizontal_placement_elements = {
    "Flexible": ["Call-To-Action (CTA) Button", "Social Proof", "Seal or Badge", "QR Code", "Contact Information"]
}

# Map each element to possible horizontal locations
element_horizontal_locations = {element: [] for element in elements}
for location, elems in elements_horizontal_placement.items():
    for elem in elems:
        element_horizontal_locations[elem].append(location)
for elem in flexible_horizontal_placement_elements["Flexible"]:
    if "Left" not in element_horizontal_locations[elem]:
        element_horizontal_locations[elem].append("Left")
    if "Mid" not in element_horizontal_locations[elem]:
        element_horizontal_locations[elem].append("Mid")
    if "Right" not in element_horizontal_locations[elem]:
        element_horizontal_locations[elem].append("Right")

# Convert location categories from string to numbers
location_to_number_horizontal = {"Left": 1, "Mid": 2, "Right": 3}
element_horizontal_location_numbers = {elem: [location_to_number_horizontal[loc] for loc in locations] for elem, locations in element_horizontal_locations.items()}

print(element_horizontal_location_numbers)