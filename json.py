import re

# Function to add an enter after Tier lines or certain MAM lines
def add_enters(lines):
    updated_lines = []
    for i, line in enumerate(lines):
        updated_lines.append(line.strip())
        
        # Add an enter after lines containing "Tier <number>"
        if re.search(r'Tier \d+', line):
            updated_lines.append("")  # Add an empty line
        
        # Add an enter after lines containing "MAM .* Research" only if no Tier line follows
        elif re.search(r'MAM .* Research', line):
            if i + 1 < len(lines) and not re.search(r'Tier \d+', lines[i + 1]):
                updated_lines.append("")  # Add an empty line

    return updated_lines

# Input and output file paths
input_file = "rec2.txt"  # Replace with your input file name
output_file = "rec4.txt"  # Replace with your desired output file name

# Process the file
with open(input_file, 'r') as file:
    lines = file.readlines()

updated_lines = add_enters(lines)

# Write the processed content to the output file
with open(output_file, 'w') as file:
    file.write('\n'.join(updated_lines) + '\n')

print(f"Processed file saved as {output_file}")
