"""
LAB 4

Ocean Levels - Pseudocode

START Program

    // Declare Constants
    DECLARE ANNUAL_RISE_MM AS CONSTANT REAL = 1.8

    // Output Header
    DISPLAY "Year        Rise (in millimeters)"
    DISPLAY "------------------------------------------"

    // Process and Output: Loop through years and calculate rise
    FOR year FROM 1 TO 25 (inclusive)
        DECLARE current_rise AS REAL = year * ANNUAL_RISE_MM
        DISPLAY year TAB TAB current_rise FORMATTED TO 2 DECIMAL PLACES
    END FOR

END Program
"""
