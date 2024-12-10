def max_depth(file_name):
    """return the maximum depth"""
    freader = open(file_name, "r")
    header = freader.readline()
    #print(header)
    first_quake = freader.redaline()
    #print(first_quake)
    max_depth = 0
    for line in freader:
        line = line.split(",")
        #print(line) # This line gives the whole data
        depth = float(line[1])
        #print(depth)
        if depth > max_depth:
            max_depth = depth
    return max_depth


def average_magnitude(file_name):
    """return the average magnitude of the earthquakes"""
    freader = open(file_name, "r")
    header = freader.readline()
    average_magnitude = 0
    count = 0
    for line in freader:
        line = line.split(",")
        count = count + 1
        average_magnitude = average_magnitude + float(line[8])
    average_magnitude = average_magnitude/count
    return average_magnitude

def count_earthquakes(file_name);
"""counts the earthquakes"""
freader = open(file_name, "r")
header = freader.readline()
count = 0
for line in freader:
    line = line.split(",")

magnitude = float(line[8])
if (magnitude >= lower_bound and magnitude<= upper_bound):
    count = count + 1
    return count


def main(file_name):

magnitude = average_magnitude(file_name)
print("The average
    depth = max_depth(file_name)
    print("The max_depth is:", depth)



main("C:\Users\12166\Downloads\earthquakes.csv") #need to give your own file name
    
