
import os
import subprocess
import tempfile

import gradio as gr
from ultralytics import YOLO


# Load pretrained YOLO model
model = YOLO("yolo26n.pt")


def track_video(input_video):
    """Detect and track objects in an uploaded video."""

    if input_video is None:
        return None

    # Create temporary files
    temp_input = input_video

    temp_output = tempfile.NamedTemporaryFile(
        suffix=".mp4",
        delete=False
    ).name

    final_output = tempfile.NamedTemporaryFile(
        suffix=".mp4",
        delete=False
    ).name

    try:
        # Process video with YOLO + ByteTrack
        model.track(
            source=temp_input,
            save=True,
            tracker="bytetrack.yaml",
            conf=0.3,
            project="/content/tracking_results",
            name="output",
            exist_ok=True,
            verbose=False
        )

        # Find YOLO's generated video
        output_directory = "/content/tracking_results/output"

        video_file = None

        for filename in os.listdir(output_directory):
            if filename.lower().endswith(
                (".mp4", ".avi", ".mov", ".mkv")
            ):
                video_file = os.path.join(
                    output_directory,
                    filename
                )
                break

        if video_file is None:
            raise FileNotFoundError(
                "YOLO did not generate an output video."
            )

        # Convert to browser-friendly H.264 MP4
        subprocess.run(
            [
                "ffmpeg",
                "-y",
                "-i",
                video_file,
                "-c:v",
                "libx264",
                "-preset",
                "fast",
                "-crf",
                "23",
                "-pix_fmt",
                "yuv420p",
                "-movflags",
                "+faststart",
                final_output
            ],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        return final_output

    finally:
        # Temporary input/output files are cleaned automatically
        if os.path.exists(temp_output):
            os.remove(temp_output)


# -----------------------------
# GRADIO INTERFACE
# -----------------------------

with gr.Blocks(
    title="AI Object Detection & Tracking"
) as demo:

    gr.Markdown(
        """
        # 🎯 AI Object Detection & Tracking

        Upload a video and let YOLO detect and track objects
        using ByteTrack.

        **Detection:** Object labels + bounding boxes  
        **Tracking:** Unique IDs for detected objects
        """
    )

    input_video = gr.Video(
        label="Upload Video",
        sources=["upload"]
    )

    output_video = gr.Video(
        label="Tracked Output",
        format="mp4"
    )

    track_button = gr.Button(
        "🚀 Detect & Track",
        variant="primary"
    )

    track_button.click(
        fn=track_video,
        inputs=input_video,
        outputs=output_video
    )

    gr.Markdown(
        """
        ### 🧠 How it works

        Video  
        ↓  
        YOLO Object Detection  
        ↓  
        Bounding Boxes + Labels  
        ↓  
        ByteTrack  
        ↓  
        Tracking IDs
        """
    )


if __name__ == "__main__":
    demo.launch()
