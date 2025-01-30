def reverse_file_content(input_file, output_file):
  try:
  # Open the input file in read mode
    with open(input_file, 'r') as file:
      content = file.read()
      # Reverse the content
      reversed_content = content[::-1]
      # Open the output file in write mode and write the reversed content
    with open(output_file, 'w') as file:
      file.write(reversed_content)
    print(f"Content from '{input_file}' has been reversed and written to '{output_file}'.")
    
  except FileNotFoundError:
  print(f"Error: The file '{input_file}' was not found.")
  except Exception as e:
  print(f"An error occurred: {e}")


input_file = input("Enter input filename: ")
output_file = input("Enter output filename: ")

reverse_file_content(input_file, output_file)
