# Description

This script allows you to resize an input image to multiple sizes and save the resized images in an output folder. It uses the Python Imaging Library (PIL) to perform resizing and the click library for command line interface.

![Recording2024-02-10222738-ezgif com-video-to-gif-converter](https://github.com/DlgshKurd/Image-Resizer/assets/96995162/0931f3d3-a040-4d69-abf6-fc9faaf4f4ea)

# Features

- Resize input image to specified sizes
- Save resized images in an output folder
- Command line interface for easy usage

# Installation

1. Install Python (if not already installed)
2. Install PIL and click library: `pip install click Pillow`
3. Download the script from the GitHub repository: [Image Resizer GitHub Repo](https://github.com/DlgshKurd/Image-Resizer)
   
# Configuration

- Default sizes for resizing are [16, 32, 48, 128]


# Example Usages

Example 1: `python main.py -o "c:/Users/YourUserName/Downloads/example.jpg"`

Example 2: `python main.py "c:/Users/YourUserName/Downloads/example.jpg" -s 64,128,256`

Example 3: `python main.py "c:/Users/YourUserName/Downloads/example.jpg" -s 64,128,256 -o "c:/Users/YourUserName/Downloads/example.jpg"`

# ImageResizer Executable 
 
run the following in your command line: 
 
   `ImageResizer.exe "Path/to/image.png" -o "Downloads" -s 10,20,30`

