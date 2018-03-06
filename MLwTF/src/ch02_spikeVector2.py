# See https://github.com/tensorflow/tensorflow/issues/2999

import tensorflow as tf
sess = tf.InteractiveSession()

raw_data = [1., 2., 8., -1., 0., 5.5, 6., 13]
spikes = tf.Variable([False] * len(raw_data), name='spikes')
# spikes.initializer.run()

saver = tf.train.Saver()

# in ipython you have to initialize all variables
# including saver
sess.run(tf.initialize_all_variables())

for i in range(1, len(raw_data)):
    if raw_data[i] - raw_data[i-1] > 5:
        spikes_val = spikes.eval()
        spikes_val[i] = True
        updater = tf.assign(spikes, spikes_val)
        updater.eval()

save_path = saver.save(sess, "./spikes.ckpt")
print("spikes data saved in file: %s" % save_path)
sess.close()
