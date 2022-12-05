# final_project
this is my repo for my senior project

# purpose 
my goal for this project was to move through the entire machine learning proccess and create an ner for job boards

# part 1 - Research 
the first part of my project was research. I will not relay everything I looked into but in the end I decieded to implement 
a pretrained model and make it more useful for my purposes, as it meant that I would not need to label as much data by hand 
the pretrained model I decieded to use was googles BERT. and moving through many readings and tutorials I decided on a really great 
article to base my model on with some changes for hyperparremeterization. 
[ml tutorial](https://towardsdatascience.com/text-classification-with-bert-in-pytorch-887965e5820f)

# part 2 - Data Collection 
after the reasearch phase I started the most tedius yet most fufilling part of the proccess. data collection
In the data collection folder I have placed all my tools I used.
for my first attempt I made a app where a peice of text would appear and you would label it by writing in the key that connects to a label. 
this took a little longer to use than I would like so I made a program called mach2. I would edit the text itself with the label attributed to it. and then I 
ran mach2 to seperate the mask from the text.

i than ran a program which then converted the mask and label into a csv.
the three csv files in this repo. one is a repo with aroound 50 words per entry
the v3 has around 150 words per entry
I found v3 did a better job while testing than v1 did.

# part 3 - Model 
I did a lot of work on the model getting it to work the way I wanted, but becuase it is all about the syntax, it will not show in the code. if I decieded to keep all the code 
i added and then deleted we could write a poorly coded book.
the model is saved as a file for colab becuase my computer lacks the gpu.

# part 4 - Where the magic happens
last was the infrastucture. I make a gui for the python application that would accept text 
run that text throught the model I trained earlier
and then return the important things.

 this model is far from perfect. and given more time I would label more text files. but the labeling proccess took so long that It came down to have an ok model that works
 or a bunch of data with no model.
 
 
the model object is too large to be saved to github. so if you want to run it. you will probabaly have to train your own first. if I had time
I would create an api to use the model to avoid these extra steps
 
 thanks
