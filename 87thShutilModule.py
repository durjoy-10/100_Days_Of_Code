''' shutil is a Python standard library module that provides a high-level interface for 
 file operations. It includes functions for copying files, copying entire directory
 trees, removing directories, and more.'''


# shutil.copy(src, dst): Copies a single file from src to dst.
import shutil

src = 'source_file.txt'
dst = 'destination_folder/new_file.txt'
shutil.copy(src, dst)


# shutil.copy2(src, dst): Similar to shutil.copy(), but also attempts to preserve file metadata.
import shutil

src = 'source_file.txt'
dst = 'destination_folder/new_file.txt'
shutil.copy2(src, dst)


# shutil.copyfile(src, dst): Copies the contents of src to dst, but the destination must be a filename.
import shutil

src = 'source_file.txt'
dst = 'destination_file.txt'
shutil.copyfile(src, dst)



# shutil.copytree(src, dst): Recursively copies an entire directory tree rooted at src to dst.
import shutil

src = 'source_directory'
dst = 'destination_directory'
shutil.copytree(src, dst)



# shutil.rmtree(path): Recursively deletes a directory tree rooted at path.
import shutil

directory_to_delete = 'directory_to_delete'
shutil.rmtree(directory_to_delete)



# shutil.move(src, dst): Moves a file or directory from src to dst.
import shutil

src = 'source_file.txt'
dst = 'destination_folder/new_file.txt'
shutil.move(src, dst)



# shutil.make_archive(base_name, format, root_dir=None, base_dir=None):
# Creates an archive file (such as zip or tar) containing the contents of a directory.
import shutil

dir_to_archive = 'directory_to_archive'
shutil.make_archive('archive_name', 'zip', dir_to_archive)



# shutil.unpack_archive(filename, extract_dir=None, format=None): Extracts an archive file into a directory.
import shutil

archive_file = 'archive_name.zip'
extract_dir = 'extracted_files'
shutil.unpack_archive(archive_file, extract_dir)
