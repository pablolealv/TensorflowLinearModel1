import tensorflow as tf

# Model parameters
W = tf.Variable([1], dtype=tf.float32)
b = tf.Variable([3], dtype=tf.float32)
# Model input and output
x = tf.placeholder(tf.float32)
linear_model = W*x + b
y = tf.placeholder(tf.float32)

# I added this log_dir to execute from my shell in tensorboard
logs_dir = './Second'
# loss
loss = tf.reduce_sum(tf.square(linear_model - y)) # sum of the squares
# optimizer
optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)

# training data
x_train = [1, 2, 3, 4]
y_train = [4, 5, 6, 7]
# training loop
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init) # reset values to wrong

# I am writing the model to graph in TensorBoard
writer = tf.summary.FileWriter(logs_dir, sess.graph)

for i in range(1000):
  sess.run(train, {x: x_train, y: y_train})

# evaluate training accuracy
curr_W, curr_b, curr_loss = sess.run([W, b, loss], {x: x_train, y: y_train})
print("W: %s b: %s loss: %s"%(curr_W, curr_b, curr_loss))

# Using W=1 and b=3 the loss funtion will be 0
