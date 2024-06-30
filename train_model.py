
model.fit(training, output, n_epoch = 200, batch_size = 8, show_metric = True)
model.save("model.tflearn")