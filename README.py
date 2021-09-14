# Receipt-
#Lovely Loveseat description
lovely_loveseat_description = 'Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.'
#Lovely Loveseat price
lovely_loveseat_price = 254.00

#Stylish Settee
stylish_settee_description = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."

#Stylish Settee Price
stylish_settee_price = 180.50

#Luxurious Lamp
luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with bream shade."

#Luxurious Lamp Price
luxurious_lamp_price = 52.15

#sales tax 8.8%
sales_tax = 0.088

#Customer 1's total
customer_one_total = lovely_loveseat_price + luxurious_lamp_price

#Customer 1's description 
customer_one_itemization = lovely_loveseat_description + " " + luxurious_lamp_description

#Customer 1's total with tax 
customer_one_tax = customer_one_total * sales_tax

#Customer's total
customer_one_total = lovely_loveseat_price + luxurious_lamp_price + customer_one_tax

print("Customer One Items:")
print(customer_one_itemization)
print("Customer One Total:")
print(customer_one_total)
