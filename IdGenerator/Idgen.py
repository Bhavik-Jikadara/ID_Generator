from PIL import Image, ImageDraw, ImageFont
image = Image.new('RGB',(1000,900), (255, 255, 255))
draw = ImageDraw.Draw(image)
font = ImageFont.truetype('arial.ttf', size=45)

import random
import os
import datetime
import qrcode

os.system("title Id CARD Generator by bhavikjikadara")

d_date = datetime.datetime.now()

reg_format_date = d_date.strftime(" Id CARD Generator ")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print(reg_format_date)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# starting position of the message
print("\n\nAll Fields are Mandatory")
print("Avoid any kind of Spelling Mistakes")
print("Write Everything in uppercase letters")

(x,y)=(50,50)
message = input("\nEnter your Company Name: ")
company = message
color = "rgb(0,0,0)" 
font= ImageFont.truetype("arial.ttf", size = 80)
draw.text((x,y), message, fill=color, font=font)

# adding an unique id number. You can manually take it from user

(x,y)= (600, 75)
idno = random.randint(10000000,90000000)
message = str("Id"+str(idno))
color = "rgb(0,0,0)" #black
font= ImageFont.truetype("arial.ttf", size = 60)
draw.text((x,y), message, fill=color, font=font)

(x,y)= (50,250)
message = input("Enter Your Full Name: ")
name = message
color = "rgb(0,0,0)" #black
font= ImageFont.truetype("arial.ttf", size = 45)
draw.text((x,y), message, fill=color, font=font)



(x,y)= (50,350)
message = input("Enter Your Gender: ")
color = "rgb(0,0,0)" #black
#font= ImageFont.truetype("arial.ttf", size = 45)
draw.text((x,y), message, fill=color, font=font)


(x,y)= (250,350)
message = input("Enter Your age: ")
color = "rgb(0,0,0)" #black
draw.text((x,y), message, fill=color, font=font)


(x,y)= (50,450)
message = input("Enter Your Brithdate: ")
color = "rgb(0,0,0)" #black
draw.text((x,y), message, fill=color, font=font)


(x,y)= (50,550)
message = input("Enter Your Blood Group: ")
color = "rgb(255,0,0)" #black
draw.text((x,y), message, fill=color, font=font)


(x,y)= (50,650)
message = input("Enter Your Mobile Number: ")
color = "rgb(0,0,0)" #black
draw.text((x,y), message, fill=color, font=font)


(x,y)= (50,750)
message = input("Enter Your Address: ")
color = "rgb(0,0,0)" #black
draw.text((x,y), message, fill=color, font=font)

# Save the edited image 

image.save(str(name)+".png")

img = qrcode.make(str(company)+ str(idno)) # this info  is added in QR code, also add other things 
img.save(str(idno)+".bmp")

til = Image.open(name+".png")
im= Image.open(str(idno)+".bmp") #25x25
til.paste(im,(600,350))
til.save(name +".png")

print(("\n\n\nYour ID CARD Successfully created in a PNG File " +name+".png"))
eval(input("\n\nPress any key to Close Program...."))