from PIL import Image
# def getchar(Char):
#     return "@" if Char< 128 else " "


#将灰度值转换为字符
ascii_chars = list('MNHQ$OC?7>!:-;. ')
def getchar(gray):
    unit = 256 / len(ascii_chars)
    return ascii_chars[int(gray // unit)]
    #return '@' if gray < 128 else ' '
    
def main():
    #img_name = "hellokitty.jpg"  # 0705.png   
    img_name = "0705.png"   
    try:
        img = Image.open(img_name)
        
    except FileNotFoundError:
        print(f"The file {img_name} was not found.")
        return
    wigth = 200 # 80  200  
    hight = 120 # 40 120
    img = img.resize((wigth, hight))
    img = img.convert("L")  #L 代表灰色图像
    text = ""
    for y in range(hight):
        for x in range (wigth):
            text += getchar(img.getpixel((x, y)))
        text += '\n'

    fd = open("hellokitty.txt","w")
    fd.write(text)
    fd.close()


if __name__== "__main__":
    main()
