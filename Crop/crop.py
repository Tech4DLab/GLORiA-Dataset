import cv2
import sys
import shutil
import os

def center_crop(img, dim):
	"""Returns center cropped image
	Args:
	img: image to be center cropped
	dim: dimensions (width, height) to be cropped
	"""
	width, height = img.shape[1], img.shape[0]

	# process crop width and height for max available dimension
	crop_width = dim[0] if dim[0]<img.shape[1] else img.shape[1]
	crop_height = dim[1] if dim[1]<img.shape[0] else img.shape[0] 
	mid_x, mid_y = int(width/2), int(height/2)
	cw2, ch2 = int(crop_width/2), int(crop_height/2) 
	crop_img = img[mid_y-ch2:mid_y+ch2, mid_x-cw2:mid_x+cw2]
	return crop_img

if __name__ == "__main__":
	tam = len(sys.argv)
	copia_hd = "./Copia_HD"
	copia_224 = "./Copia_224"
	
	if not os.path.exists(copia_hd):
		os.mkdir(copia_hd)
	if not os.path.exists(copia_224):
		os.mkdir(copia_224)
	for i in range(1, tam):
		src = sys.argv[i]	
		image = cv2.imread(sys.argv[i])

		ccrop_img = center_crop(image, (2500,2500))
		cv2.imwrite(sys.argv[i], ccrop_img)
		shutil.copy2(src, copia_hd)
		
		resize_im = cv2.resize(ccrop_img,(224,224))
		cv2.imwrite(sys.argv[i], resize_im)
				
		shutil.copy2(src, copia_224)
		
