import numpy as np
import tensorflow as tf

d = np.random.normal(10,1,100)

update_avg = alpha * curr_value + (1 - alpha) * prev_avg

with tf.Session() as sess:
    for i in range(len(d)):
        curr_avg = sess.run(update_avg,
                            feed_dict={curr_value : d[i]})
        sess.run(tf.assign(prev_avg, curr_avg))
