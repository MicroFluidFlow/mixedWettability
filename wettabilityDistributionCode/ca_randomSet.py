# To generate a set of random numbers
import numpy as np
import matplotlib.pyplot as plt


# Set a seed for reproducibility
np.random.seed(1) #25

# Desired average and range
desired_average = 90
value_range = (0,180) #(0, 180)

# Generate 150 random values
random_values = np.random.uniform(value_range[0], value_range[1], 150)

# Adjust the values to achieve the desired average
current_average = np.mean(random_values)
random_values = random_values - (current_average - desired_average)

# Clip values to ensure they are within the specified range
random_values = np.clip(random_values, value_range[0], value_range[1])

# Round the values to integers if needed
random_values = np.round(random_values).astype(int)

# Reshape the array into a 16x8 array
array_15x10 = random_values.reshape((15, 10))

# Plotting the phase diagram
plt.imshow(array_15x10, cmap='jet', interpolation='nearest')
plt.colorbar(label='Values')
plt.title('Phase Diagram of Random Values')
plt.xlabel('Column Index')
plt.ylabel('Row Index')
plt.savefig('caDist.pdf')
plt.show()

# Specify the file name
output_file = "constAlphacaData.txt"

# Open the file in write mode
with open(output_file, "w") as file:
    # Iterate over the rows and columns of the array
    for i in range(15):
        for j in range(10):
            # Write the structure for each element to the file
            file.write(f"    r{i+1}_{j+1}\n")
            file.write("    {\n")
            file.write(f"        type            constantAlphaContactAngle;\n")
            file.write(f"        theta0          {array_15x10[i, j]};\n")
            file.write(f"        limit           gradient;\n")
            file.write(f"        value           uniform 0;\n")
            file.write("    }\n")
