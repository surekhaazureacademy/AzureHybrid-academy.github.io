from fontTools.ttLib import TTFont

# Replace with your actual TTF filename
input_font = "StackSansNotch-Regular.ttf"
output_font = "StackSansNotch-Regular.woff2"

# Load the TTF font and save it as WOFF2
font = TTFont(input_font)
font.flavor = "woff2"
font.save(output_font)

print(f"Success! Converted {input_font} to {output_font}")
