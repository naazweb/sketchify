
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from .models import *
from PIL import Image
import cv2
import numpy as np

import time
import os

"""
def home(request):
    context = {}
    return render(request, 'index.html', context)

"""


def dodgeNaive(image, mask):
    # determine the shape of the input image
    width, height = image.shape[:2]

    # prepare output argument with same size as image
    blend = np.zeros((width, height), np.uint8)

    for col in xrange(width):
        for row in xrange(height):
            # do for every pixel
            if mask[c, r] == 255:
                # avoid division by zero
                blend[c, r] = 255
            else:
                # shift image pixel value by 8 bits
                # divide by the inverse of the mask
                tmp = (image[c, r] << 8) / (255-mask)

                # make sure resulting value stays within bounds
                if tmp > 255:
                    tmp = 255
                    blend[c, r] = tmp

    return blend


def dodgeV2(image, mask):
    return cv2.divide(image, 255-mask, scale=256)


def burnV2(image, mask):
    return (255 - (cv2.divide(255-image, 255-mask, scale=256)))


def home(request):

    if request.method == 'GET':
        form = ImageForm()
        context = {
            'form': form,
        }
        return render(request, 'index.html', context)

    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():

            # Save Original Image and get ID
            add = form.save()
            i_id = add.id
            # quality = int(request.POST.get('quality'))

            # From Id get original Image path for further conversion
            og_image = Images.objects.get(id=add.id)
            image_url = og_image.original_img
            new_name = int(time.time())
            # Opening image and applying convesion operation
            image_path = os.path.join(os.getcwd(),'media',str(image_url))
            img_rgb = cv2.imread(image_path)
            img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
            img_gray_inv = 255 - img_gray
            img_blur = cv2.GaussianBlur(img_gray_inv, ksize=(15, 75),
                                        sigmaX=0, sigmaY=0)

            img_blend = dodgeV2(img_gray, img_blur)
            cv2.imwrite(os.path.join(os.getcwd(),'media','converted','{}.jpg'.format(new_name)), img_blend)

            original_size = os.stat(image_path).st_size
            # converted_size = os.stat('./media/converted/{}.jpg'.format(new_name)).st_size
            converted_size = '1245B'
            # Updating all data
            Images.objects.filter(id=i_id).update(converted_img='converted/{}.jpg'.format(
                new_name), converted_size=converted_size, original_size=original_size)

            images = Images.objects.all().order_by('id').reverse()

            context = {
                'form': form,
                'images': images[0],
                'withquality': image_url,
            }
            # return redirect(request.META['HTTP_REFERER'],context)
            return render(request, 'index.html', context)
