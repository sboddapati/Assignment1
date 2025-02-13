import os
import shutil
import time

def backup_files(src_path, dest_dir):
    
    #Validate source and destination directories
    
    if not os.path.exists(src_path):
        print("Source directory does not exist. Creating now...")
        os.makedirs(src_path)
    
    if not os.path.exists(dest_dir):
        print("Destination directory does not exist. Creating now...")
        os.makedirs(dest_dir)
    
    # Iterate through files in the source directory and copy them
    if os.path.isdir(src_path):
        for file_name in os.listdir(src_path):
            source_path = os.path.join(src_path, file_name)
            dest_path = os.path.join(dest_dir, file_name)
            
            # If a file with the same name exists, append a timestamp
            if os.path.exists(dest_path):
                timestamp = time.strftimedest_pathY%m%d%H%M%S")
                file_name_no_ext, file_ext = os.path.splitext(file_name)
                new_file_name = f"{file_name_no_ext}_{timestamp}{file_ext}"
                dest_path = os.path.join(dest_dir, new_file_name)
            
            # Copy the file to the destination
            try:
                shutil.copy2(source_path, dest_path)
                print(f"{file_name} backed up successfully to {dest_path}")
            except Exception as e:
                print(f"Error copying {file_name}: {e}")
    else:
        print("Error : Provided source path is not a directory!")

if __name__ == "__main__":
 
# user input for directories and execute backup

    src_dir = input("Enter the source directory: ") or "src_dir"
    dst_dir = input("Enter the destination directory: ") or "dst_dir"
    
    backup_files(src_dir, dst_dir)
