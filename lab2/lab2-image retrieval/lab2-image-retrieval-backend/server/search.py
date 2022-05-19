################################################################################################################################
# This function implements the image search/retrieval .
# inputs: Input location of uploaded image, extracted vectors
# 
# ###############################################################################################################################
import imageio
import numpy as np
import tensorflow._api.v2.compat.v1 as tf
from image_vectorizer import create_inception_graph, run_bottleneck_on_image
from scipy.spatial.distance import cosine
import pickle
import os
from tensorflow.python.platform import gfile
import random

imsave = imageio.imsave
imread = imageio.imread
FRONT_RES = '../../lab2-image-retrieval-frontend/image-retrieval/src/result/'
BOTTLENECK_TENSOR_NAME = 'pool_3/_reshape:0'
BOTTLENECK_TENSOR_SIZE = 2048
MODEL_INPUT_WIDTH = 299
MODEL_INPUT_HEIGHT = 299
MODEL_INPUT_DEPTH = 3
JPEG_DATA_TENSOR_NAME = 'DecodeJpeg/contents:0'
RESIZED_INPUT_TENSOR_NAME = 'ResizeBilinear:0'
MAX_NUM_IMAGES_PER_CLASS = 2 ** 27 - 1  # ~134M


# show_neighbors(random.randint(0, len(extracted_features)), indices, neighbor_list)

def get_top_k_similar(image_data, pred, pred_final, k):
    print("total data", len(pred))
    print(image_data.shape)
    # for i in pred:
    # print(i.shape)
    # break
    os.mkdir('static/result')

    # cosine calculates the cosine distance, not similiarity. Hence no need to reverse list
    top_k_ind = np.argsort([cosine(image_data, pred_row) \
                            for ith_row, pred_row in enumerate(pred)])[1:k + 1]
    print(top_k_ind)

    for i, neighbor in enumerate(top_k_ind):
        image = imread(pred_final[neighbor])
        # timestr = datetime.now().strftime("%Y%m%d%H%M%S")
        # name= timestr+"."+str(i)
        name = pred_final[neighbor]
        tokens = name.split("\\")
        img_name = tokens[-1]
        print(img_name)
        name = 'static/result/' + img_name
        fro_name = FRONT_RES+img_name
        imsave(name, image)
        imsave(fro_name,image)


def recommend(imagePath, extracted_features):
    tf.reset_default_graph()

    config = tf.ConfigProto(
        device_count={'GPU': 0}
    )

    sess = tf.Session(config=config)
    graph, bottleneck_tensor, jpeg_data_tensor, resized_image_tensor = (create_inception_graph())
    image_data = gfile.FastGFile(imagePath, 'rb').read()
    features = run_bottleneck_on_image(sess, image_data, jpeg_data_tensor, bottleneck_tensor)

    with open('neighbor_list_recom.pickle', 'rb') as f:
        neighbor_list = pickle.load(f)
    print("loaded images")
    print(len(neighbor_list))
    get_top_k_similar(features, extracted_features, neighbor_list, k=random.randint(9, 20))
