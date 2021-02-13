import numpy as np
import matplotlib.pyplot as plt

arrax = test = np.arange(99)
leftcontact = []
rightcontact = []
for i in range(1,100):
	#arrax.append(i)
	leftcontact.append(0)
	rightcontact.append(100)

print("ALL WHEELS LEFT")
for n in range (1,100,3):
	print("input contact LC", n)
	leftcontact[n] = input()
	print("input contact RC", n)
	rightcontact[n] = input()

fig, (ax1, ax2) = plt.subplots(2)
fig.suptitle('Vertically stacked subplots')

ax1.plot(arrax + 1, rightcontact, 'g--')
ax2.plot(arrax, leftcontact, 'r--')
ax1.invert_yaxis()
plt.legend()
plt.show()
