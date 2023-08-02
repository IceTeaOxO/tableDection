import os

def batch_rename_txt_files(folder_path, prefix='text_'):
    if not os.path.exists(folder_path):
        raise ValueError("The specified folder path does not exist.")

    txt_files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]
    txt_files.sort()

    renamed_count = 0
    for idx, filename in enumerate(txt_files, start=1):
        new_name = f"{prefix}{str(idx).zfill(6)}.txt"
        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_name)
        os.rename(old_path, new_path)
        renamed_count += 1

    return renamed_count

if __name__ == "__main__":
    folder_path = "data/datasets2/train"
    prefix = "img_"  # You can change the prefix to whatever you like

    try:
        count = batch_rename_txt_files(folder_path, prefix)
        print(f"{count} txt files renamed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
