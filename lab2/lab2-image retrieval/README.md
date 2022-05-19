# HCI Lab2 Report

|   ID    |    Name     |
| :-----: | :---------: |
| 1953902 | GAO Yangfan |

[TOC]

## 1. Design Principles of an Information Retrieval Engine

In the lecture, Prof. Shen mentioned 5 principles or tasks to complete for an information retrieval engine, they are:

- Formulation
- Initialization
- Review
- Refinement
- Use

I will display how I adopted these principles in my image retrieval system one by one in this report.

*To better adopt these principles, I separated the frontend and backend and used **Flask as the backend framework and Vue.js as the frontend framework*** and I used the selected subset of ImageNet with 2295 images provided altogether with the backend code.



## 2. Initialization & Formulation

*Initialization*

The searching button is just at an conspicuous position of the web page:

<img src="C:\Users\CharlesGao\AppData\Roaming\Typora\typora-user-images\image-20220514100604118.png" alt="image-20220514100604118" style="zoom:50%;" />

*Formulation*

Users can click the input box to upload an image and preview that image in the input box, the searching session will be triggered automatically after uploading the image:

<img src="C:\Users\CharlesGao\AppData\Roaming\Typora\typora-user-images\image-20220514100921965.png" alt="image-20220514100921965" style="zoom:50%;" />

Users can also preview the image of a bigger size by clicking this:

<img src="C:\Users\CharlesGao\AppData\Roaming\Typora\typora-user-images\image-20220514104555658.png" alt="image-20220514104555658" style="zoom:50%;" />

and the user will see:

<img src="C:\Users\CharlesGao\AppData\Roaming\Typora\typora-user-images\image-20220514104854549.png" alt="image-20220514104854549" style="zoom: 33%;" />

## 3. Review

The system also provides a brief review of the searching result(the number of result):

<img src="C:\Users\CharlesGao\AppData\Roaming\Typora\typora-user-images\image-20220514101737770.png" alt="image-20220514101737770" style="zoom:50%;" />

followed by the list of results:

![image-20220514102342931](C:\Users\CharlesGao\AppData\Roaming\Typora\typora-user-images\image-20220514102342931.png)

## 4. Refinement

To change the searching parameters, users can re-upload the image if they find the image is not what they intended to upload by deleting the current one and upload the image.

To delete the image, users may click this:

![image-20220514105014836](C:\Users\CharlesGao\AppData\Roaming\Typora\typora-user-images\image-20220514105014836.png)

## 5. Use

To use the result, users can add any of them to the favorite list:

<img src="C:\Users\CharlesGao\AppData\Roaming\Typora\typora-user-images\image-20220514111431306.png" alt="image-20220514111431306" style="zoom:50%;" />

 Also, users can view the favorite list by clicking the navigation tag on the top of the page:

<img src="C:\Users\CharlesGao\AppData\Roaming\Typora\typora-user-images\image-20220514112809200.png" alt="image-20220514112809200" style="zoom:50%;" />

Users can view the favorite image at the 'favorite' page and choose to delete the image:

<img src="C:\Users\CharlesGao\AppData\Roaming\Typora\typora-user-images\image-20220514113412836.png" alt="image-20220514113412836" style="zoom:50%;" />

## Appendix: How to run this

*Local*

You can run this project locally by the steps below:

1. Unzip the submitted file **in the same directory**

2. Run the backend

a. `cd lab2-image-retrieval-backend/server`

b. `pip install -r requirement.txt`

c. `python rest-server.py`

3. Run the frontend

a. `cd lab2-image-retrieval-frontend/image-retrieval `

b.`npm run serve`

c. visit [http://localhost:8080](http://localhost:8080)



*Visit on the Internet*

I will try to deploy this on the server and I will update this on GitHub if I successfully deployed this. 

[update] You can now visit http://101.42.149.87:8080 as I deployed this to the server. 
