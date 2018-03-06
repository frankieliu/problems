
import tensorflow as tf
ts = tf.InteractiveSession()

d = [1, 2, 8, -1, 0, 5.5, 6, 13]
spikes = tf.Variable([False] * len(d), name='spikes')
spikes.initializer.run()

saver = tf.train.Saver()

#
#
#

for i in range(1, len(d)):
    if d[i] - d[i-1] > 5:
        spikes_val = spikes.eval()
        spikes_val[i] = True
        updater = tf.assign(spikes, spikes_val)
        updater.eval()

save_path = saver.save(ts, "/home/fyliu/spikes.ckpt")
print("spikes data saved in file: %s" % save_path)
ts.close()
