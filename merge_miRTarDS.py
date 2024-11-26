def merge_files(output_file, file_list):
    # Open the output file in write mode
    with open(output_file, 'w', encoding='utf-8') as outfile:
        # Iterate through each file in the list
        for i, file in enumerate(file_list):
            # Open each file in read mode
            with open(file, 'r', encoding='utf-8') as infile:
                lines = infile.readlines()
                
                # For the first file, write all lines with first-line modification
                if i == 0:
                    outfile.writelines(lines)
                else:
                    # For other files, skip the first line and write the rest
                    outfile.writelines(lines[1:])
    
    # Print a message when merging is done
    print(f"Merging complete, the combined file is: {output_file}")

# List of files to merge
file_list = [f"miRTarDS_part_{i}.txt" for i in range(1, 11)]

# Call the function to merge files into the output file
output_file = "miRTarDS_combined.txt"
merge_files(output_file, file_list)
