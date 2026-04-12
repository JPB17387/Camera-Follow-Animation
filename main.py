# Copyright (c) 2026 Jhon Paul Baonil
# Released under the MIT license
# https://github.com/JPB17387/Camera-Follow

import os
import shutil
from datetime import datetime
from CodeVideoRenderer import CameraFollowCursorCV

video = CameraFollowCursorCV(
    code=("file", "javascript_script.js"), 
    language="javascript",
)

video.render()

# Move the output video to your requested folder automatically
output_dir = r"C:\Users\HF\Videos\Code Video Renderer" #here you can change the directory in where do you want your output video to be downloaded
os.makedirs(output_dir, exist_ok=True)

# Generate a unique timestamp to prevent overwriting files (e.g., _20260411_124530)
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
unique_filename = f"CameraFollowCursorCV_{timestamp}.mp4"

# Manim (the underlying engine) saves the file here automatically
source_file = os.path.join("media", "videos", "1080p60", "CameraFollowCursorCV.mp4")
destination_file = os.path.join(output_dir, unique_filename)

if os.path.exists(source_file):
    shutil.copy2(source_file, destination_file)
    print(f"Success! Unique video was automatically saved to: {destination_file}")
else:
    print("Error: Could not find the generated video file to copy.")