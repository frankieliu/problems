import tensorflow as tf
ts = tf.InteractiveSession()

r = [1,2,8,-1,0,5.5,6,13]

s = tf.Variable(False)
s.initializer.run()

for i in range(1, len(r)):
    
    if r[i] - r[i-1] > 5:
        updater = tf.assign(s, tf.constant(True))
        updater.eval()
    else:
        tf.assign(s, False).eval()
        
    print("Spike",s.eval())
    
