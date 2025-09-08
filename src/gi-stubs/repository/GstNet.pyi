from gi.repository import Gst

class NetClientClock:
    @staticmethod
    def new(
        name: str,
        remote_address: str,
        remote_port: int,
        base_time: int,
    ) -> Gst.Clock: ...

class NetTimeProvider:
    @staticmethod
    def new(
        clock: Gst.Clock,
        address: str,
        port: int,
    ) -> NetTimeProvider: ...
