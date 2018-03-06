import tensorflow as tf
sess = tf.InteractiveSession()

spikes = tf.Variable([False] * 8, name='spikes')
saver = tf.train.Saver()
sess.run(tf.initialize_all_variables())

# this doesn't work because not all variables are available
# in particular it complains about spikes_#

saver.restore(sess, "./spikes.ckpt")
print(spikes.eval())

sess.close()
