import tensorflow as tf

x = tf.constant([[1, 2]])
neg_x = tf.negative(x)

print(neg_x)

with tf.Session(
        config=tf.ConfigProto(log_device_placement=True)) as ts:
    result = ts.run(neg_x)
    print(result)
