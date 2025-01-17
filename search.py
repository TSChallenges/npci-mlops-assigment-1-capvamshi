import re


def grep(pattern, file_name):
    with open(file_name, 'r') as fp:
        for line in fp:
            if re.search(pattern, line):
                print(line.strip())
    return


def sed(old_pattern, new_pattern, file_name):
    # Read the file contents
    with open(file_name, 'r') as file:
        text = file.read()
    # Use re.sub() to replace the old pattern with the new pattern
    new_text = re.sub(old_pattern, new_pattern, text)
    # Write the modified contents back to the file
    with open(file_name, 'w') as file:
        file.write(new_text)

    print(
        f'Successfully replaced "{old_pattern}" with "{new_pattern}" in {file_name}.')
    return


def awk(n, file_name):
    with open(file_name, 'r') as file:
        for line in file:
            # Split the line into columns based on whitespace
            columns = re.split(r'\s+', line.strip())
            # Select the first `n` columns
            selected_columns = columns[:n]
            # Print the selected columns joined by a tab character
            print('\t'.join(selected_columns))
    return


def main():
    file_name = input("Enter the file name")
    command = input("Enter the command: grep, sed, awk")

    if command == 'grep':
        pattern = input("Enter the pattern")
        grep(pattern, file_name)
    elif command == 'sed':
        old_pattern = input("Enter old pattern")
        new_pattern = input("Enter new pattern")
        sed(old_pattern, new_pattern, file_name)
    elif command == 'awk':
        n = int(input("Enter the column number"))
        awk(n, file_name)
    else:
        print("Comamnd is invalid")


if __name__ == "__main__":
    main()
