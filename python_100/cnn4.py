from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.preprocessing.image import ImageDataGenerator
from keras.layers import Dropout



model = Sequential()

model.add(Conv2D(32, (3, 3), input_shape = (200, 200, 3), activation = 'relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(32, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, (3, 3), activation = 'relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
model.add(Dense(64, activation = 'relu'))
model.add(Dropout(0.5))
model.add(Dense(5, activation = 'softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

# this is the augmentation configuration we will use for training
train_datagen = ImageDataGenerator(
    rescale=1./255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True)
# this is the augmentation configuration we will use for testing:
# only rescaling
test_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory('dataset/training_set',
                                                 target_size = (200, 200),
                                                 batch_size = 32,
                                                 class_mode = 'categorical')

validation_generator = test_datagen.flow_from_directory('dataset/test_set',
                                            target_size = (200, 200),
                                            batch_size = 32,
                                            class_mode = 'categorical')
#print("validation_generators", validation_generator)

model.fit_generator(
    train_generator,
    samples_per_epoch=8000,
    epochs=1,
    validation_data=validation_generator,
    validation_steps=2000)


model.save('image_rec_test.h5')
import numpy as np
from keras.preprocessing import image
test_image = image.load_img('/home/lucifer/Downloads/61833371_144640713262993_8942835081001566208_o.jpg', target_size = (200, 200, 3))
test_image = image.img_to_array(test_image)
test_image = test_image/225
#test_image = np.expand_dims(test_image, axis = 0)
result = model.predict(test_image.reshape(1, 200, 200, 3))
print(result)
pred_bool = (result >0.5)
print(pred_bool)
predictions = pred_bool.astype(int)
print(predictions)
for i in predictions:
    for a,b in zip(i, column):
        print(a,b)


