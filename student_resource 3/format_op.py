import re
import pandas as pd

# Define the entity_unit_map
entity_unit_map = {
    "width": {
        "centimetre",
        "foot",
        "millimetre",
        "metre",
        "inch",
        "yard"
    },
    "depth": {
        "centimetre",
        "foot",
        "millimetre",
        "metre",
        "inch",
        "yard"
    },
    "height": {
        "centimetre",
        "foot",
        "millimetre",
        "metre",
        "inch",
        "yard"
    },
    "item_weight": {
        "milligram",
        "kilogram",
        "microgram",
        "gram",
        "ounce",
        "ton",
        "pound"
    },
    "maximum_weight_recommendation": {
        "milligram",
        "kilogram",
        "microgram",
        "gram",
        "ounce",
        "ton",
        "pound"
    },
    "voltage": {
        "millivolt",
        "kilovolt",
        "volt"
    },
    "wattage": {
        "kilowatt",
        "watt"
    },
    "item_volume": {
        "cubic foot",
        "microlitre",
        "cup",
        "fluid ounce",
        "centilitre",
        "imperial gallon",
        "pint",
        "decilitre",
        "litre",
        "millilitre",
        "quart",
        "cubic inch",
        "gallon"
    }
}

unit_mapping = {
    "cm": "centimetre",
    "mm": "millimetre",
    "m": "metre",
    "in": "inch",
    "\"": "inch",
    "ft": "foot",
    "yd": "yard",
    "kg": "kilogram",
    "g": "gram",
    "mg": "milligram",
    "lb": "pound",
    "oz": "ounce",
    "ton": "ton",
    "v": "volt",
    "w": "watt",
    "mv": "millivolt",
    "kv": "kilovolt",
    "cf": "cubic foot",
    "ml": "millilitre",
    "l": "litre",
    "μl": "microlitre",
    "cup": "cup",
    "fl oz": "fluid ounce",
    "cl": "centilitre",
    "gal": "gallon",
    "imp gal": "imperial gallon",
    "pt": "pint",
    "dl": "decilitre",
    "qt": "quart",
    "cu in": "cubic inch"
}


# Regex to capture number followed by unit
pattern = r"(\d+(?:\.\d+)?)\s*(\w+|\"|')"

def format_unit(entity_name, text):
    matches = re.findall(pattern, text.lower())  # Find all matches (case-insensitive)
    
    for value, unit in matches:
        unit = unit_mapping.get(unit, unit)  # Convert abbreviation to full form
        # Check if the unit is allowed for the entity
        if unit in entity_unit_map.get(entity_name, {}):
            return f"{value} {unit}"
    
    return ""

def process_csv(input_csv, output_csv):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(input_csv)
    
    # Check if the required columns ('initial_preds' and 'entity_name') exist
    if 'initial_preds' not in df.columns or 'entity_name' not in df.columns:
        print("The CSV must have 'initial_preds' and 'entity_name' columns.")
        return
    
    # Apply the format_unit function to each row
    df['final_preds'] = df.apply(lambda row: format_unit(row['entity_name'], str(row['initial_preds'])), axis=1)
    
    # Save the updated DataFrame to a new CSV file
    df.to_csv(output_csv, index=False)
    print(f"Output saved to {output_csv}")

# Example usage
input_csv = "test.csv"  # The input CSV file
output_csv = "output_with_preds.csv"  # The output CSV file with the 'final_preds' column

# Process the CSV
process_csv(input_csv, output_csv)
