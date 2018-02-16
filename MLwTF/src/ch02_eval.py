import tensorflow as tf

ts = tf.InteractiveSession()

x = tf.constant([[1, 2]])
print(x)
neg_x = tf.negative(x)
print(neg_x)

result = neg_x.eval()
print(neg_x)
print(result)

ts.close()
