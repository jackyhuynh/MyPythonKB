"""
LAB 3: Volume Discounts

START Program

    // Declare Constants
    DECLARE PACKAGE_PRICE AS CONSTANT REAL = 149.00
    DECLARE DISCOUNT_RATE_10_49 AS CONSTANT REAL = 0.10  // 10%
    DECLARE DISCOUNT_RATE_50_99 AS CONSTANT REAL = 0.20  // 20%
    DECLARE DISCOUNT_RATE_100_149 AS CONSTANT REAL = 0.30 // 30%
    DECLARE DISCOUNT_RATE_150_PLUS AS CONSTANT REAL = 0.40 // 40%

    // Declare Variables
    DECLARE num_packages AS INTEGER
    DECLARE discount_amount AS REAL = 0.0
    DECLARE total_purchase_amount AS REAL
    DECLARE calculated_discount_percentage AS REAL = 0.0

    // Input: Get number of packages purchased
    PROMPT "Enter the number of packages purchased: "
    GET num_packages

    // Process: Determine discount based on quantity using nested decision structures (flowchart logic)

    // Flowchart Start Node
    IF num_packages IS GREATER THAN OR EQUAL TO 150 THEN
        SET calculated_discount_percentage = DISCOUNT_RATE_150_PLUS
    ELSE IF num_packages IS GREATER THAN OR EQUAL TO 100 THEN
        SET calculated_discount_percentage = DISCOUNT_RATE_100_149
    ELSE IF num_packages IS GREATER THAN OR EQUAL TO 50 THEN
        SET calculated_discount_percentage = DISCOUNT_RATE_50_99
    ELSE IF num_packages IS GREATER THAN OR EQUAL TO 10 THEN
        SET calculated_discount_percentage = DISCOUNT_RATE_10_49
    ELSE // num_packages IS LESS THAN 10
        // No discount
        SET calculated_discount_percentage = 0.0
    END IF
    // Flowchart End Node

    // Calculate discount amount
    SET discount_amount = (num_packages * PACKAGE_PRICE) * calculated_discount_percentage

    // Calculate total purchase amount after discount
    SET total_purchase_amount = (num_packages * PACKAGE_PRICE) - discount_amount

    // Output: Display discount and total amounts
    DISPLAY "Discount Amount: $" FORMATTED TO 2 DECIMAL PLACES (discount_amount)
    DISPLAY "Total Amount: $" FORMATTED TO 2 DECIMAL PLACES (total_purchase_amount)

END Program
"""


# Name: [Your Name]
# Program Status: Complete
# Description: This program calculates the discount and total purchase amount for software packages
#              based on the quantity purchased, applying different discount tiers.

def main():
    # Named constants for pricing and discount rates
    PACKAGE_PRICE = 149.00
    DISCOUNT_RATE_10_49 = 0.10  # 10% discount for 10-49 packages
    DISCOUNT_RATE_50_99 = 0.20  # 20% discount for 50-99 packages
    DISCOUNT_RATE_100_149 = 0.30  # 30% discount for 100-149 packages
    DISCOUNT_RATE_150_PLUS = 0.40  # 40% discount for 150 or more packages

    # Variable declarations and initializations
    num_packages = 0
    discount_amount = 0.0
    total_purchase_amount = 0.0
    calculated_discount_percentage = 0.0

    # Input: Ask the user to enter the number of packages purchased
    try:
        num_packages = int(input("Enter the number of packages purchased: "))
    except ValueError:
        print("Invalid input. Please enter a whole number for the quantity.")
        return  # Exit the program if input is not a valid integer

    # Process: Determine the discount based on the number of packages
    if num_packages >= 150:
        calculated_discount_percentage = DISCOUNT_RATE_150_PLUS
    elif num_packages >= 100:
        calculated_discount_percentage = DISCOUNT_RATE_100_149
    elif num_packages >= 50:
        calculated_discount_percentage = DISCOUNT_RATE_50_99
    elif num_packages >= 10:
        calculated_discount_percentage = DISCOUNT_RATE_10_49
    else:
        # No discount for less than 10 packages
        calculated_discount_percentage = 0.0

    # Calculate the dollar amount of the discount
    # The original price before discount
    original_price = num_packages * PACKAGE_PRICE
    discount_amount = original_price * calculated_discount_percentage

    # Calculate the total amount of the purchase after discount
    total_purchase_amount = original_price - discount_amount

    # Output: Display the discount amount and the total purchase amount
    # Dollar amounts are rounded to 2 decimal places and display dollar signs
    print(f"Discount Amount: $ {discount_amount:,.2f}")
    print(f"Total Amount: $ {total_purchase_amount:,.2f}")


# This ensures that the main function is called only when the script is executed directly
if __name__ == "__main__":
    main()
