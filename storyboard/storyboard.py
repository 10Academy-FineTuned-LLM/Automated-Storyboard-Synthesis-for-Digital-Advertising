import cv2
import os

def create_storyboard(frames_dir, storyboard_path, cols=4, rows=4, frame_size=(300, 300)):
    frame_files = sorted(os.listdir(frames_dir))
    total_frames = len(frame_files)
    frame_count = 0
    storyboard = None

    for frame_file in frame_files:
        frame_path = os.path.join(frames_dir, frame_file)
        frame = cv2.imread(frame_path)
        frame = cv2.resize(frame, frame_size)

        if storyboard is None:
            height, width, _ = frame.shape
            storyboard_width = cols * width
            storyboard_height = rows * height
            storyboard = np.zeros((storyboard_height, storyboard_width, 3), dtype=np.uint8)

        col_idx = frame_count % cols
        row_idx = frame_count // cols
        x_start = col_idx * width
        y_start = row_idx * height
        x_end = x_start + width
        y_end = y_start + height

        storyboard[y_start:y_end, x_start:x_end] = frame

        frame_count += 1

    cv2.imwrite(storyboard_path, storyboard)


# Example usage
frames_directory = "frames"
output_storyboard = "storyboard.jpg"
create_storyboard(frames_directory, output_storyboard)
