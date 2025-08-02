import cv2
import numpy as np

def calculate_psnr(original_img, enhanced_img):
    mse = np.mean((original_img - enhanced_img) ** 2)
    psnr = 10 * np.log10(255 ** 2 / mse)
    return psnr