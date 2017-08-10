from PIL import Image

# RGB values for recoloring.
darkBlue = (60, 68, 102)
red = (237, 132, 132)
lightBlue = (145, 245, 247)
yellow = (247, 243, 168)

# Import image.
my_image = Image.open("shibe.jpg") #change IMAGENAME to the path on your computer to the image you're using
image_list = my_image.getdata() #each pixel is represented in the form (red value, green value, blue value, transparency). You don't need the fourth value.
image_list = list(image_list) #Turns the sequence above into a list. The list can be iterated through in a loop.

recolored = [] #list that will hold the pixel data for the new image.

#YOUR CODE to loop through the original list of pixels and build a new list based on intensity should go here.

for tuples in image_list:
    x = tuples[0] + tuples[1] + tuples[2]
    if x < 182:
        recolored.append(darkBlue)
    elif x >= 182 and x < 364:
        recolored.append(red)
    elif x >= 364 and x < 546:
        recolored.append(lightBlue)
    elif x >= 546:
        recolored.append(yellow)

# Create a new image using the recolored list. Display and save the image.
new_image = Image.new("RGB", my_image.size) #Creates a new image that will be the same size as the original image.
new_image.putdata(recolored) #Adds the data from the recolored list to the image.
new_image.show() #show the new image on the screen
new_image.save("recolored1.jpg", "jpeg") #save the new image as "recolored.jpg"
