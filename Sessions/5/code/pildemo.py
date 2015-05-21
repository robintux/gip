from PIL import Image
from PIL import ImageFilter
# read image
#im = Image.open('D:\Assaf\py\lena.bmp')

# display
#im.show()

# Threshold segmentation
def seg_img_th(img,output_prefix,ext):
    for th in range(20,200,20):
        seg_img = Image.new('1',img.size,'white') # binary image
        for x in range(img.size[0]):
            for y in range(img.size[1]):            
                if img.getpixel((x,y))[0] < th:                
                    seg_img.putpixel((x,y),0)            
        output_fname = output_prefix + str(th) + '.' + ext    
        seg_img.save(output_fname,ext)
        print 'save ' + output_fname
        del seg_img

def main():
    # create and save an image of vertical lines
    vertical_lines = Image.new('L',(100,100),'white')
    for x in range(vertical_lines.size[0]):
        if x % 2 == 0:
            for y in range(vertical_lines.size[1]):
                vertical_lines.putpixel((x,y),0)

    #vertical_lines.show()

    vertical_lines.save('D:\Assaf\py\output.bmp','bmp')
    del vertical_lines    

    # rotation
    coins = Image.open('D:\Assaf\py\coins.jpg')
    coins.show()
    out = coins.rotate(45)
    out.show()
    del out
    del coins

    # edge detection    
    coins = Image.open('D:\Assaf\py\coins.jpg')
    coins_edges = coins.filter(ImageFilter.FIND_EDGES)
    del coins

    # thresholding of license plate number
    plate = Image.open('D:\Assaf\py\plate.jpg')
    print plate # note that plate is an RGB image!
    outname_prefix = 'D:\Assaf\py\plate_th'
    ext = 'bmp'
    seg_img_th(plate,outname_prefix,ext)




main()
    


