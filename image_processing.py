# import os
# from PIL import Image, ImageEnhance

# class ImageProcessing:
#     def __init__(self, input_folder, outer_folder):
#         self.input_folder = input_folder
#         self.outer_folder = outer_folder
#         # Ensure the output directory exists
#         if not os.path.exists(outer_folder):
#             os.makedirs(outer_folder)

#     def enhance_image(self, image_path):
#         try:
#             image = Image.open(image_path)
#             # Enhance the image (e.g., increase contrast)
#             enhancer = ImageEnhance.Contrast(image)
#             enhanced_image = enhancer.enhance(2.0)  # Adjust enhancement level as needed
            
#             # Save enhanced image
#             filename = os.path.basename(image_path)
#             enhanced_image_path = os.path.join(self.outer_folder, f"enhanced_{filename}")
#             enhanced_image.save(enhanced_image_path)
            
#             # Reduce image size (e.g., resize to 50% of original size)
#             reduced_image = self.reduce_image_size(enhanced_image)
#             reduced_image_path = os.path.join(self.outer_folder, f"reduced_{filename}")
#             reduced_image.save(reduced_image_path)

#             return enhanced_image_path, reduced_image_path
#         except Exception as e:
#             print(f"Error enhancing image: {e}")
#             return None, None

#     def reduce_image_size(self, image):
#         width, height = image.size
#         new_size = (int(width * 0.5), int(height * 0.5))  # Resize to 50%
#         return image.resize(new_size, Image.Resampling.LANCZOS)
import os
from PIL import Image, ImageEnhance

class ImageProcessing:
    def __init__(self, input_folder, outer_folder):
        self.input_folder = input_folder
        self.outer_folder = outer_folder
        # Ensure the output subdirectories exist
        self.enhanced_folder = os.path.join(outer_folder, "enhanced")
        self.reduced_folder = os.path.join(outer_folder, "reduced")
        if not os.path.exists(self.enhanced_folder):
            os.makedirs(self.enhanced_folder)
        if not os.path.exists(self.reduced_folder):
            os.makedirs(self.reduced_folder)

    def enhance_image(self, image_path):
        try:
            image = Image.open(image_path)
            # Enhance the image (e.g., increase contrast)
            enhancer = ImageEnhance.Contrast(image)
            enhanced_image = enhancer.enhance(2.0)  # Adjust enhancement level as needed
            
            # Save enhanced image
            filename = os.path.basename(image_path)
            enhanced_image_path = os.path.join(self.enhanced_folder, f"enhanced_{filename}")
            enhanced_image.save(enhanced_image_path)
            
            # Reduce image size (e.g., resize to 50% of original size)
            reduced_image = self.reduce_image_size(enhanced_image)
            reduced_image_path = os.path.join(self.reduced_folder, f"reduced_{filename}")
            reduced_image.save(reduced_image_path)

            return enhanced_image_path, reduced_image_path
        except Exception as e:
            print(f"Error enhancing image: {e}")
            return None, None

    def reduce_image_size(self, image):
        width, height = image.size
        new_size = (int(width * 0.5), int(height * 0.5))  # Resize to 50%
        return image.resize(new_size, Image.Resampling.LANCZOS)
