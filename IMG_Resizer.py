import os
import cv2
import time
from PyInstaller.utils.hooks import collect_submodules, collect_data_files

#use pyinstaller -F python_file.py

def resize_images(input_folder, custom_name, width, height):
    output_folder = os.path.join(input_folder, custom_name)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    file_number = 1
    image_count = 0

    for filename in os.listdir(input_folder):
        if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
            file_path = os.path.join(input_folder, filename)
            try:
                img = cv2.imread(file_path)
                resized_img = cv2.resize(img, (width, height))

                base, ext = os.path.splitext(filename)
                new_filename = f"{custom_name}_{file_number:02}{ext}"
                cv2.imwrite(os.path.join(output_folder, new_filename), resized_img)
                print(f"'{new_filename}' saved to folder: '{custom_name}'")
                file_number += 1
                image_count += 1
            except Exception as e:
                print(f"Error converting {file_path}: {e}")
    print(f"Total images processed: {image_count}")

def exit_or_input(prompt):
    user_input = input(prompt)
    if user_input.lower() == 'exit':
        for i in range(2, 0, -1):
            print(f'Program exited by user. Closing in {i}....')
            time.sleep(1)
        exit()
    return user_input

def main():
    while True:
        print("I AM IMG RESIZER. Enter 'exit' to quit")
        while True:
            input_folder = exit_or_input("Enter the input folder path: ")
            if os.path.isdir(input_folder):
                break
            else:
                print("Invalid folder path. Please try again.")

        while True:
            custom_name = exit_or_input("Enter the File name: 'xxx'_ord.format: ")
            if custom_name.isalnum():
                break
            else:
                print("Letters and numbers only. Please try again.")

        while True:
            dimensions = exit_or_input("Enter the dimensions (width,height): ")
            try:
                width, height = map(int, dimensions.split(','))
                if width > 0 and height > 0:
                    break
                else:
                    print("Width must be a positive integer. Please try again.")
            except ValueError:
                print("Invalid format. Please enter(width,height).")

        while True:
            proceed = exit_or_input("Enter 'y' to start resizing: ").lower()
            if proceed == 'y':
                resize_images(input_folder, custom_name, width, height)
                print("Conversion completed successfully!")
                break
            else:
                print("Invalid command. Please enter 'y' or 'exit'")

if __name__ == "__main__":
    main()
