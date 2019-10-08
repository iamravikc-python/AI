import cv2

# print(img)
# cv2.imshow('image', img)
# cv2.waitKey(5000)
# cv2.destroyAllWindows()


print(type(img))
flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
for j in range(190):
    filename = "C:\\images\\" + str(j) + ".png"
    imagetype = flags[j]
    print(imagetype)
    str1= print(filename)
    
img = cv2.imread('C:\images\steve-jobs.jpeg')
cv2.imshow('image', img)
convertimg= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.waitKey(5000)
cv2.destroyAllWindows()
cv2.imwrite(str1 , convertimg)
    

