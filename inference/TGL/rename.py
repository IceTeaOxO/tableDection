import os

def batch_rename_images(folder_path, prefix='img_', start_number=1):
    if not os.path.exists(folder_path):
        raise ValueError("The specified folder path does not exist.")

    file_list = os.listdir(folder_path)
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']

    renamed_count = 0
    for filename in file_list:
        file_ext = os.path.splitext(filename)[1].lower()
        if file_ext in image_extensions:
            new_name = f"{prefix}{str(start_number).zfill(5)}{file_ext}"
            old_path = os.path.join(folder_path, filename)
            new_path = os.path.join(folder_path, new_name)
            os.rename(old_path, new_path)
            start_number += 1
            renamed_count += 1

    return renamed_count

if __name__ == "__main__":
    folder_path = "inference\TGL"
    prefix = "img_"  # You can change the prefix to whatever you like
    start_number = 1  # You can change the starting number if needed

    try:
        count = batch_rename_images(folder_path, prefix, start_number)
        print(f"{count} images renamed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
