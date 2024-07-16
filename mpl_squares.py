import matplotlib.pyplot as plt
input_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
plt.plot(input_values,squares, linewidth=5)
plt.title('squares numbers', fontsize=14)
plt.xlabel('value', fontsize=14)
plt.ylabel('squares of value', fontsize=14)
plt.show()