import os
import hashlib

def get_file_md5(file_path):
    """Returns the MD5 hash of a file."""
    with open(file_path, 'rb') as f:
        md5sum = hashlib.md5()
        while True:
            data = f.read(8192)
            if not data:
                break
            md5sum.update(data)
        return md5sum.hexdigest()

def delete_files_with_same_md5(directory):
    """Deletes all files with the same md5sum in a directory."""
    files_md5sum = {}
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            md5sum = get_file_md5(file_path)
            if md5sum in files_md5sum:
                os.remove(file_path)
                print(f'Deleted file {file_path}')
            else:
                files_md5sum[md5sum] = file_path

# Example usage
directory = '/Users/user/Documents/projects/water'
delete_files_with_same_md5(directory)
