import numpy as np
import matplotlib.pyplot as plt


def computeAndPlotRegression(x, y_matrix, N):
    x_lin = np.vander(x, N+1)
    print x_lin
    coeff, residuals, rank, singulars = np.linalg.lstsq(x_lin, y_matrix)
    plt.plot(
        np.transpose(x_lin).tolist()[0],
        np.transpose(x_lin*coeff).tolist()[0]
    )
    print np.transpose(x_lin).tolist()[0],
    print np.transpose(x_lin*coeff).tolist()[0]
    return coeff, residuals, rank, singulars

x = []
y = []
with open('data.csv', 'r') as f:
    for line in f:
        raw_x, raw_y = line.strip().split(',')
        x.append(float(raw_x))  # n, 1 vector
        y.append(float(raw_y))  # n, 1 vector
        #print "%s %s" % (raw_x, raw_y)

print x
print y


x_matrix = np.transpose(np.matrix(x))
y_matrix = np.transpose(np.matrix(y))
print np.linalg.lstsq(x_matrix, y)
print np.vander(x_matrix, 1)
print np.vander(x_matrix, 2)
# Plot real value
plt.plot(x, y, 'ro')


#plt.show()
# # polynomial regression
# N = 2
# x_pol = np.vander(x, N)
# coeff_pol, residuals_pol, rank_pol, singulars_pol = \
#     np.linalg.lstsq(x_pol, y_matrix)
# #print coeff_pol
# plt.plot(np.transpose(x_pol)[1], x_pol*coeff_pol, 'c--')

# N = 3
# x_pol = np.vander(x, N)
# coeff_pol, residuals_pol, rank_pol, singulars_pol = \
#     np.linalg.lstsq(x_pol, y_matrix)
# #print coeff_pol
# plt.plot(np.transpose(x_pol)[1], x_pol*coeff_pol, 'g-')

# N = 21
# x_pol = np.vander(x, N)
# coeff_pol, residuals_pol, rank_pol, singulars_pol = \
#     np.linalg.lstsq(x_pol, y_matrix)
# #print coeff_pol
# plt.plot(np.transpose(x_pol)[1], x_pol*coeff_pol, 'k:')

# N = 24
# x_pol = np.vander(x, N)
# coeff_pol, residuals_pol, rank_pol, singulars_pol = \
#     np.linalg.lstsq(x_pol, y_matrix)
# #print coeff_pol
# plt.plot(np.transpose(x_pol)[1], x_pol*coeff_pol, 'c-')

# N = 60
# x_pol = np.vander(x, N)
# coeff_pol, residuals_pol, rank_pol, singulars_pol = \
#     np.linalg.lstsq(x_pol, y_matrix)
# #print coeff_pol
# plt.plot(np.transpose(x_pol)[1], x_pol*coeff_pol, 'r-')

# plt.xlabel('X')
# plt.ylabel('Y')
# plt.title('Regression')
# plt.grid()
# plt.show()
