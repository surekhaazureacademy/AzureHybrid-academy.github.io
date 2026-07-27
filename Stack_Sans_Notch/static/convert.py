from fontTools.ttLib import TTFont

# Replace with your actual TTF filename
input_font = "my-font.ttf"
output_font = "my-font.woff2"

# Load the TTF font and save it as WOFF2
font = TTFont(input_font)
font.flavor = "woff2"
font.save(output_font)

print(f"Success! Converted {input_font} to {output_font}")
