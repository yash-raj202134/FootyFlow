
from utils.video_utils import read_video,write_video


def main():
    
    # read video
    video_frame = read_video("input_videos/08fd33_4.mp4")

    # save video
    write_video(video_frame,'output_videos/output_video.avi')




if __name__ == "__main__":
    main()