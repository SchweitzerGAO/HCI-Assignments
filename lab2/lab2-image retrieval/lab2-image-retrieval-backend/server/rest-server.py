# !flask/bin/python
# ############################################################################################################################### ------------------------------------------------------------------------------------------------------------------------------ This file implements the REST layer. It uses flask micro framework for server implementation. Calls from front end reaches here as json and being branched out to each projects. Basic level of validation is also being done in this file. # ------------------------------------------------------------------------------------------------------------------------------- ###############################################################################################################################
import os
import shutil

import imageio
import numpy as np
from flask import Flask, jsonify, request, redirect, render_template
from flask_httpauth import HTTPBasicAuth
from werkzeug.utils import secure_filename
from tensorflow.python.platform import gfile
from search import recommend
from flask_cors import CORS

# from scipy.misc import imsave

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
ABS_PATH_RESULT = os.path.abspath('./static/result')
ABS_PATH_UPLOAD = os.path.abspath('.')
ABS_PATH_FAV = os.path.abspath('./favorite')
FRONT_RES = '../../lab2-image-retrieval-frontend/image-retrieval/src/result'
FRONT_FAV = '../../lab2-image-retrieval-frontend/image-retrieval/src/favorite'

app = Flask(__name__, static_url_path="")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
auth = HTTPBasicAuth()
CORS(app, resources=r'/*')

imsave = imageio.imsave
imread = imageio.imread

# ==============================================================================================================================
#                                                                                                                              
#    Loading the extracted feature vectors for image retrieval                                                                 
#                                                                          						        
#                                                                                                                              
# ==============================================================================================================================
extracted_features = np.zeros((2955, 2048), dtype=np.float32)
with open('saved_features_recom.txt') as f:
    for i, line in enumerate(f):
        extracted_features[i, :] = line.split()
print("loaded extracted_features")


# ==============================================================================================================================
#                                                                                                                              
#  This function is used to do the image search/image retrieval
#                                                                                                                              
# ==============================================================================================================================

# backend mixed with frontend
@app.route('/imgUpload', methods=['GET', 'POST'])
def upload_img():
    print("image upload")
    result = 'static/result'
    if not gfile.Exists(result):
        os.mkdir(result)
    shutil.rmtree(result)

    if request.method == 'POST' or request.method == 'GET':
        print(request.method)
        # check if the post request has the file part
        if 'file' not in request.files:
            print('No file part')
            return redirect(request.url)

        file = request.files['file']
        print(file.filename)
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            print('No selected file')
            return redirect(request.url)
        if file:  # and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            input_loc = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            recommend(input_loc, extracted_features)
            # os.remove(input_loc)
            image_path = "/result"
            image_list = [os.path.join(image_path, file) for file in os.listdir(result)
                          if not file.startswith('.')]
            images = {
                'image0': image_list[0],
                'image1': image_list[1],
                'image2': image_list[2],
                'image3': image_list[3],
                'image4': image_list[4],
                'image5': image_list[5],
                'image6': image_list[6],
                'image7': image_list[7],
                'image8': image_list[8]
            }
            return jsonify(images)


# backend seperated with frontend
@app.route('/imgSearch', methods=['GET', 'POST'])
def img_search():
    result = 'static/result'
    if not gfile.Exists(result):
        os.mkdir(result)
    shutil.rmtree(result)

    if 'file' not in request.files:
        print(request)
        print('No file part')
        return jsonify({'code': 400, 'msg': 'Please upload an image'})
    file = request.files['file']

    if file.filename == '':
        print('No selected file')
        return jsonify({'code': 400, 'msg': 'File name cannot be empty'})
    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        input_loc = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        recommend(input_loc, extracted_features)
        # if not os.path.exists(FRONT_RES):
        #     os.makedirs(FRONT_RES)

        # if os.path.exists(FRONT_RES):
        #     shutil.rmtree(FRONT_RES)

        # shutil.copytree('./static/result', FRONT_RES)
        image_path = "/result"
        image_list = ['http://101.42.149.87:9090/result/'+file for file in os.listdir(result)
                      if not file.startswith('.')]
        response = {
            'code': 200,
            'data': {'searchResult': image_list,
                     'uploadPath': os.path.join(ABS_PATH_UPLOAD, input_loc),
                     'lenResult': len(image_list)
                     },
            'msg': 'success'
        }
        return jsonify(response)


@app.route('/addFavorite', methods=['POST'])
def add_favorite():

    img_path = request.form.get('path')
    print(img_path)
    image = imread(img_path)
    fav_name = img_path.split('/')[-1]
    if fav_name in os.listdir(FRONT_FAV):
        return jsonify({'code': 400, 'msg': 'image already exists in favorite list'})
    fav_name_front = os.path.join(FRONT_FAV, fav_name)
    fav_name_back = os.path.join('./favorite',fav_name)
    print(fav_name)
    imsave(fav_name_back,image)
    imsave(fav_name_front, image)

    # if not os.path.exists(FRONT_FAV):
    #     os.makedirs(FRONT_FAV)

    # if os.path.exists(FRONT_FAV):
    #     shutil.rmtree(FRONT_FAV)
    #
    # shutil.copytree('./favorite', FRONT_FAV)

    return jsonify({'code': 200, 'msg': 'success'})


@app.route('/deleteFavorite', methods=['POST'])
def delete_favorite():
    img_path = request.form.get('path')
    img_path_back = os.path.join('./favorite',img_path)
    img_path_front = os.path.join(FRONT_FAV,img_path)
    print(img_path)
    os.remove(img_path_back)
    os.remove(img_path_front)
    # if not os.path.exists(FRONT_FAV):
    #     os.makedirs(FRONT_FAV)

    # if os.path.exists(FRONT_FAV):
    #     shutil.rmtree(FRONT_FAV)
    #
    # shutil.copytree('./favorite', FRONT_FAV)
    return jsonify({'code': 200, 'msg': 'success'})


@app.route('/viewFavorite', methods=['GET'])
def view_favorite():
    fav = './favorite'

    fav_list = [os.path.join(ABS_PATH_FAV,file) for file in os.listdir(fav) if not file.startswith('.')]

    fav_list = sorted(fav_list, key=lambda x: os.path.getctime(x), reverse=True)
    ret_list = ['http://101.42.149.87:9090/favorite/'+file.split('\\')[-1] for file in fav_list]
    if len(fav_list) == 0:
        return jsonify({'code': 404, 'msg': 'Not Found'})
    else:
        return jsonify(
            {
                'code': 200,
                'favoriteList': ret_list,
                'msg': 'success'
            }
        )


# ==============================================================================================================================
#                                                                                                                              
# Main function
#  				                                                                                                
# ==============================================================================================================================
@app.route("/")
def main():
    return render_template('main.html')


if __name__ == '__main__':
    app.run(debug=True, host='localhost')
