import numpy as np

dataset = 'KS20'
time_step = 12
used_data = 'source'
dimension_x = 'x'
dimension_y = 'z'
dimension_z = 'y'
frames_ps = dataset + '/' + str(time_step) + '/'
nb_nodes = 25

input_data_x = np.load(
			'Datasets/' + frames_ps + 'train_npy_data/' + used_data + '_' + dimension_x + '_' + dataset + '_' + str(
				time_step) + '.npy', allow_pickle=True)

input_data_y = np.load(
			'Datasets/' + frames_ps + 'train_npy_data/' + used_data + '_' + dimension_y + '_' + dataset + '_' + str(
				time_step) + '.npy', allow_pickle=True)

input_data_z = np.load(
			'Datasets/' + frames_ps + 'train_npy_data/' + used_data + '_' + dimension_z + '_' + dataset + '_' + str(
				time_step) + '.npy', allow_pickle=True)


input_data_x = input_data_x.reshape([-1, time_step, nb_nodes])
spine_pos_x = input_data_x[:, :, 0]
spine_pos_x = np.expand_dims(spine_pos_x, -1)
input_data_x = input_data_x - spine_pos_x

input_data_y = input_data_y.reshape([-1, time_step, nb_nodes])
spine_pos_y = input_data_y[:, :, 0]
spine_pos_y = np.expand_dims(spine_pos_y, -1)
input_data_y = input_data_y - spine_pos_y

input_data_z = input_data_z.reshape([-1, time_step, nb_nodes])
spine_pos_z = input_data_z[:, :, 0]
spine_pos_z = np.expand_dims(spine_pos_z, -1)
input_data_z = input_data_z - spine_pos_z

NUM = 0
input_data_x_ins = input_data_x[NUM,:,:]
input_data_y_ins = input_data_y[NUM,:,:]
input_data_z_ins = input_data_z[NUM,:,:]



import matplotlib.pyplot as plt

LIMBS25 = [[12, 13], [13, 14], [14, 15], [16, 17], [17, 18], [18, 19],
         [1, 2], [2, 3], [3, 20], [4, 5], [5, 6], [6, 7], [7, 21], [21, 22],
           [8, 9], [9, 10], [10, 11], [11, 23], [23, 24], [0, 1], [0, 12],[0, 16],[2, 4],[2, 8] ]

LIMBS15 = [[12, 13], [13, 14], [16, 17], [17, 18],
           [4, 5], [5, 6], [6, 7],
           [8, 9], [9, 10], [10, 11],[0, 20],[20, 3], [0, 12],[0, 16],[20, 4],[20, 8] ]

colors = ['b', 'b', 'r', 'r', 'g', 'g', 'g', 'm', 'm', 'm','black','black','b','r','g','m']
# left_leg = [12, 13, 14, 15]
# right_leg = [16, 17, 18, 19]
# torso = [0, 1, 2, 3, 20]
# left_arm = [4, 5, 6, 7, 21, 22]
# right_arm = [8, 9, 10, 11, 23, 24]

fig = plt.figure()

for i in range(time_step):
    xs1 = input_data_x_ins[i]
    ys1 = input_data_y_ins[i]
    zs1 = input_data_z_ins[i]
    ys1 = ys1 / abs(ys1.max() - ys1.min())
    zs1 = zs1 / abs(0 - min(zs1[14],zs1[18]))

    for index, k in enumerate(LIMBS15):
        x = [xs1[k[0]], xs1[k[1]]]
        y = [ys1[k[0]]+ 2*i, ys1[k[1]]+ 2*i]
        z = [zs1[k[0]], zs1[k[1]]]
        plt.plot(y, z, c=colors[index % len(colors)])

plt.show()