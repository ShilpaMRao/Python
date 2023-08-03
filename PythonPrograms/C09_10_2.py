filename = 'mbox-short.txt'
hour_counts = {}

# Read the file
with open(filename, 'r') as file:
    for line in file:
        # Check for 'From ' lines
        if line.startswith('From '):
            # Split the line and extract the hour
            words = line.split()
            time = words[5]
            hour = time.split(':')[0]

            # Update the hour counts
            hour_counts[hour] = hour_counts.get(hour, 0) + 1

# Sort the hour counts by hour
sorted_counts = sorted(hour_counts.items())

# Print the hour counts
for hour, count in sorted_counts:
    print(hour, count)


    
        


