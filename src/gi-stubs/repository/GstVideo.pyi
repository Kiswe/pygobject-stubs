from gi.repository import Gst

def video_event_new_downstream_force_key_unit(
    timestamp: int,
    stream_time: int,
    running_time: int,
    all_headers: bool,
    count: int,
) -> Gst.Event: ...
