import tensorflow as tf
ts = tf.InteractiveSession()

d = [1,2,8,-1,0,5.5,6,13]

spike = tf.Variable(False)
spike.initializer.run()

for i in range(1, len(d)):
    if d[i] - d[i-1] > 5:
        updater = tf.assign(spike, True)
        updater.eval()
    else:
        tf.assign(spike,False).eval()
    print("Spike", spike.eval())

ts.close()
