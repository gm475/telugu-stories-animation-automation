import subprocess
import os

def merge_audio_video(audio_file, video_file, output_file):
    """
    Merges audio and video into a single file using FFmpeg.
    """
    # Run FFmpeg command to merge audio and video
    command = [
        "ffmpeg",
        "-i", video_file,
        "-i", audio_file,
        "-c:v", "copy",
        "-c:a", "aac",
        "-strict", "experimental",
        output_file
    ]

    try:
        subprocess.run(command, check=True)
        print(f"Successfully merged {audio_file} and {video_file} into {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error during merging: {e}")
        raise

# Paths to files
audio_path = "output/voiceover.mp3"
video_path = "output/animation.mp4"
output_path = "output/final_video.mp4"

# Create output directory if it doesn't exist
os.makedirs(os.path.dirname(output_path), exist_ok=True)

# Merge the files
merge_audio_video(audio_path, video_path, output_path)
