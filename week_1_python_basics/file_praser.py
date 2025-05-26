def parse_csv_file(file_path):
    data = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        headers = lines[0].strip().split(',')
        for line in lines[1:]:
            values = line.strip().split(',')
            row = dict(zip(headers, values))
            data.append(row)
    return data

# Example usage
file_path = 'students.csv'
parsed_data = parse_csv_file(file_path)
print(parsed_data)
