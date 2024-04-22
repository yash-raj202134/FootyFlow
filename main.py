
from utils.video_utils import read_video,write_video
from trackers.tracker import Tracker

def main():
    
    # read video
    video_frame = read_video("input_videos/08fd33_4.mp4")

    # Initialize tracker

    tracker = Tracker("models/best.pt")
    tracks = tracker.get_object_tracks(video_frame,read_from_stub=True,stub_path='stubs/track_stubs.pkl')

    # save video
    write_video(video_frame,'output_videos/output_video.avi')




if __name__ == "__main__":
    main()