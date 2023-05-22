# Lab 3 Report

|   ID    |    Name     |
| :-----: | :---------: |
| 1953902 | GAO Yangfan |

[TOC]

## 1. The task for data analysis

Among the 3 datasets that Prof. Shen provided, I chose the Black Friday dataset for this assignment.

This dataset illustrates the basic personal info, the product category and the money payed for the purchase etc. in a certain Black Friday. As the personal info contains necessary features like gender, age, I decided to analyze the data in the following 4 aspects:

1. The ratio of each gender of each age range that purchased in Black Friday, which will be illustrated in a pie chart.
1. The ratio of each age range of each gender range that purchased in Black Friday, which will be illustrated also in a pie chart.

3. The varying of purchase amount with the growing of age(general, separated gender), which will be illustrated in a line chart

4. The number of purchasers of each product category, which will be illustrated in a bar chart.

## 2. Layout of dashboard

On the top is the title of the dashboard followed by 4 diagrams mentioned in part 1.

The first 2 diagrams illustrates task 1 and 2 in part 1, whose layout are like this:

![image-20220528163501078](C:\Users\CharlesGao\AppData\Roaming\Typora\typora-user-images\image-20220528163501078.png)

Users can select the age range by clicking the dropdown or select the gender by clicking the radio items.

Task 3 is illustrated by this diagram:

![image-20220528163847233](C:\Users\CharlesGao\AppData\Roaming\Typora\typora-user-images\image-20220528163847233.png)

If users click on 'Separated Gender', the trend for each gender will be illustrated like this:

![image-20220528164548530](C:\Users\CharlesGao\AppData\Roaming\Typora\typora-user-images\image-20220528164548530.png)

Task 4 is illustrated by a bar chart like this:

![image-20220528164159302](C:\Users\CharlesGao\AppData\Roaming\Typora\typora-user-images\image-20220528164159302.png)

This not only shows the total amount for each category but also the gender distribution by different colors.

## 3. What the patterns revealed

Some interesting things can be concluded from this dashboard:

1.  The ratio of male purchasers of Black Friday is much more than that of female (at least in this dataset), which is contrast to the stereotype that women do more shopping than men do.
2. Purchasers aged between 26-35 tend to by the most items on Black Friday than other ages, both for men and women.
3. Purchasers in this dataset are prone to by items of category 8, which implies this category is either daily musts or has huge discount on Black Friday.

## Appendix: How to run this

1. `pip install -r requirements.txt`
2. `python my_data_visualization.py`
3. visit http://127.0.0.1:8050/

*OR* 

directly visit http://101.42.149.87:8050/
