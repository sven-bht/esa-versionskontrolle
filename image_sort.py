from PIL import Image
import os

PATH_SORTED_IMGS = "sorted_images"
PATH_NO_DATE = "sorted_images/no_date"


def create_path_if_not_exists(path):
    if not os.path.exists(path):
        os.makedirs(path)


def copy_file(source, dest):
    os.popen(f"copy {source} {dest}")


def get_date_taken(path):
    create_path_if_not_exists(PATH_SORTED_IMGS)

    images = os.listdir(path)
    for image in images:
        image_path = os.path.join(path, image)
        try:
            exif = Image.open(image_path)._getexif()
            date = exif[36867]
            year = date[0:4]
            year_path = os.path.join(PATH_SORTED_IMGS, year)
            create_path_if_not_exists(year_path)

            month = date[5:7]
            month_path = os.path.join(year_path, month)
            create_path_if_not_exists(month_path)
            copy_file(image_path, os.path.join(month_path, image))

        except:
            create_path_if_not_exists(PATH_NO_DATE)
            copy_file(image_path, os.path.join(PATH_NO_DATE, image))


get_date_taken("images")
