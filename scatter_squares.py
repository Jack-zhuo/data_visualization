import matplotlib.pyplot as plt

# write lists by hand
# x_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# y_values = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# write lists automatically
x_values = list(range(1, 10))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values,c=y_values,cmap=plt.cm.Blues,edgecolor='none', s=200)
plt.title("Scatter plot", fontsize=14)
plt.xlabel("value", fontsize=14)
plt.ylabel("squares of value", fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)

plt.axis([0, 10, 0, 10**2])
plt.savefig("scatter_squares.png")
