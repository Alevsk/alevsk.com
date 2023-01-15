#!/usr/bin/env python

import os

def check_and_delete_unused_images(image_folder, markdown_folder, dry_run=False):
    """
    This function scans a list of image names recursively from a given folder,
    checks if the image is being used in Markdown files in another given folder,
    and deletes the image if it is not being used.
    """
    deleted_count = 0
    # Get a list of all image files in the image folder
    image_files = [os.path.join(dp, f) for dp, dn, filenames in os.walk(image_folder) for f in filenames]

    # Iterate over each image file
    for image_file in image_files:
        is_used = False

        # Get the image file name without the path
        image_file_name = os.path.basename(image_file)

        # Get a list of all markdown files in the markdown folder
        markdown_files = [os.path.join(dp, f) for dp, dn, filenames in os.walk(markdown_folder) for f in filenames if f.endswith('.md')]

        # Iterate over each markdown file
        for markdown_file in markdown_files:
            with open(markdown_file, 'r') as f:
                markdown_text = f.read()

                # Check if the image file name is in the markdown text
                if image_file_name in markdown_text:
                    is_used = True
                    break

        # If the image is not used and dry_run is False, delete it
        if not is_used and not dry_run:
            os.remove(image_file)
            deleted_count += 1
        # If dry_run is True, print the image file name instead of deleting it
        elif not is_used and dry_run:
            print(f'{image_file_name} will be deleted')
    print(f'Script created using the help of chatGPT, {deleted_count} images were deleted')

image_folder = 'content/posts/images'
markdown_folder = 'content/posts'
dry_run = True

check_and_delete_unused_images(image_folder, markdown_folder, dry_run)