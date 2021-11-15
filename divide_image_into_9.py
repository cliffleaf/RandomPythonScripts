from PIL import Image

# fill image into a square, then divide into 9 pieces, then export
# This script is for posting Wechat Moments, the maximum number of images allowed is 9

def fill_image(image):
    width, height = image.size
    new_length = width if width >= height else height
    new_image = Image.new(image.mode, (new_length, new_length), color="white")

    if width <= height:
        new_image.paste(image, ((new_length-width)//2, 0))
    else:
        new_image.paste(image, (0, (new_length-height)//2))

    return new_image


def crop_image(image):
    new_image = fill_image(image)
    width = new_image.size[0]  # width == height
    box_width = width / 3

    box_list = [] # a box is a fragment of the image to be divided

    for i in range(3):
        for j in range(3):
            # let i represent the horizontal division, j be the vertical division
            # crop the image with (left, upper, right, lower) boundaries
            box = (j * box_width, i * box_width, (j+1) * box_width, (i+1) * box_width)
            box_list.append(box)
    
    image_list = [new_image.crop(box) for box in box_list]

    return image_list


def save_image(image_list):
    number = 1
    for image in image_list:
        image.save(str(number) + ".png", "PNG")
        number += 1


def main():
    file_path = "taoyao.jpeg"
    image = Image.open(file_path)
    image_list = crop_image(image)
    save_image(image_list)

main()
