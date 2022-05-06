# senior-project-spring-2022-AI-positioning-system
senior-project-spring-2022-AI-positioning-system created by GitHub Classroom

![image](https://user-images.githubusercontent.com/72994790/155942737-dd6101bf-0149-4948-a8da-c893bec73347.png)

Project Describes                                                                                          
About
Use Artificial Intelligence algorithms to find images that are similar to scanned images. And extract the text to determine. The use this text and table to locat the picture. I'm going to test this with photos from different databases. The Photos1 and photos2 groups are different and it come from different cities and places.        
This project can help you find the location of the photo you want. And there's a certain probability of finding its exact location. There are plenty of similar photos to be found.

Include 4 part
1. similarity of pictures:
Use Python3 code to scan pictures that the user needs. Then, compare the scanned images with images in the image database and find similar images. This step will use the picture website: https://www.pexels.com to help search for similar pictures. It used a grayscale image, and take the average and binarize each pixel based on the average. Then, it uses Ahash to calculate the similarity number.
2. Find text or numbers in picture: 
Extract words and numbers from highly similar images. Use the ORC to detect the text (print text). Then use character segmentation and recognition to locate the text and number area in the pictures. Print the repeat the same location number and names to the check location part.
3. Find Location
(Use training model to find the name)
From maximum to minimum, pick the number that repeats the most, or. Text and use the item. Text to get the location.
Use the repeat names and numbers(latitude, longitude) to locate the scan picture, which includes continents, oceans, and direct location. It used a training model to find the location name and ran multiple times to get the location. Also, the starting model uses the most repeated name and number.
4. Test project:
At the end of the project, I will test all the deta and code. Then, calculate the correct rate.
picture_detabase is use my detabase picture to test it.
Here is the picture web: https://www.pexels.com

Special notes:  3/17 There is currently a problem with the text in the scanner and the text &number extraction. My code cannot precise, and location the white block for the text. I research about some Scan the picture use Optical Character Recognition (OCR) essay and paper to help me to solve the problem of clarity, but it does not work for now. The current progress about finding similarities is complete but not tested yet. The image database for the first group has been compiled, and there are three similar images. And the first image has print text.

Technologies and Software Used:                        
Python; Pycharm, tesseract-OCR web

Project Components
![image](https://user-images.githubusercontent.com/72994790/155926459-9816875a-93bd-442a-a118-edb4be6c404b.png)

Picture Detabase (this detabase will include 500 pictures and it's include some samiliar pictures. All the text and number is print number/text)
This also in WIKI
[Simple-gantt-chart_ms .xlsx](https://github.com/comp195/senior-project-spring-2022-AI-positioning-system/files/8189944/Simple-gantt-chart_ms.xlsx)
Here is the picture website: https://www.pexels.com

Callenges: (find text & number):
The tesseract-OCR web may not very fit my requirements. This web is work now.

Callenges: My OCR part finally worked. but still need to connect numbers and message together. 
