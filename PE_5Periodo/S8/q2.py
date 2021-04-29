from scipy import stats
import matplotlib.pyplot as plt

size = [128, 256, 384, 512, 640, 768, 896, 1024]

ob1 = [386, 850, 1544, 3035, 6650, 13887, 28059, 50916]
ob2 = [375, 805, 1644, 3123, 6839, 14567, 27439, 52129]
ob3 = [393, 824, 1553, 3235, 6768, 13456, 27659, 51360]

m, b, r_value, p_value, std_err = stats.linregress(size , ob1)

print(m, b)

plt.plot(size, ob1)
# plt.plot(size, ob2)
# plt.plot(size, ob3)

plt.show()