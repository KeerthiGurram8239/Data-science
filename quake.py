def max_depth(file_name):
    """Return the maximum depth from the earthquake data."""
    freader = open(file_name, "r")
    first_quake = freader.readline()  # Skip header
    max_depth = 0
        
    for line in freader:
        line = line.strip().split(",")
        depth = float(line[1])  # Assuming depth is in the second column
        if depth > max_depth:
            max_depth = depth

    return max_depth

def average_magnitude(file_name):
    """Return the average magnitude from the earthquake data."""
    freader = open(file_name, "r")
    header = freader.readline()  # Skip header
    total_magnitude = 0
    count = 0

    for line in freader:
        line = line.strip().split(",")
        magnitude = float(line[4])  # Assuming magnitude is in the fifth column
        total_magnitude += magnitude
        count += 1

    if count == 0:
        return 0  # Prevent division by zero
    return total_magnitude / count

def main(file_name):
    depth = max_depth(file_name)
    avg_magnitude = average_magnitude(file_name)
    print("The maximum depth is:", depth)
    print("The average magnitude is:", avg_magnitude)

# Replace the path with the path to your own CSV file
main("C:/Users/12166/Downloads/earthquakes.csv")
