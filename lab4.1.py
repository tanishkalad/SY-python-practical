

status = input("Enter order status (pending/shipped/delivered): ").strip().lower()

if status == "pending":
    message = "Your order has been received and is currently being processed."
elif status == "shipped":
    message = "Great news! Your order has been shipped and is on its way."
elif status == "delivered":
    message = "Your order has been successfully delivered. Thank you for shopping with us!"
else:
    message = "Sorry, the order status entered is not recognized."

print("\n===== ORDER TRACKING UPDATE =====")
print(f"Status: {status.capitalize()}")
print(f"Update: {message}")
print("=================================")
