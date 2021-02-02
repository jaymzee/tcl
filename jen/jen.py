import numpy as np
import matplotlib.pyplot as plt

p=np.array([[1,8],[7,4],[7,5],[7,6],[12,2],[12,3],[13,3],[14,2],[15,2],[15,1]])
[x, y] = p.T
a = np.array([x, np.ones(10)]).T
[m, b] = np.linalg.solve(a.T @ a, a.T @ y)

plt.plot(x, y, '.', label = 'data points')
plt.plot(x, m * x + b, label = 'LMS solution')
plt.axis('equal')
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.title('$ y = %.3g x + %.3g $' % (m, b))
plt.legend()
plt.show()
