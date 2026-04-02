from gi.repository import Gst
from gi.repository import GLib

class ATSCStreamType:
    DCII_VIDEO: int
    AUDIO_AC3: int
    SUBTITLING: int
    ISOCH_DATA: int
    SIT: int
    AUDIO_EAC3: int
    AUDIO_DTS_HD: int

class Descriptor:
    tag: int
    tag_extension: int
    length: int
    data: int

class DVBDescriptorType:
    NETWORK_NAME: int
    SERVICE_LIST: int
    STUFFING: int
    SATELLITE_DELIVERY_SYSTEM: int
    CABLE_DELIVERY_SYSTEM: int
    VBI_DATA: int
    VBI_TELETEXT: int
    BOUQUET_NAME: int
    SERVICE: int
    COUNTRY_AVAILABILITY: int
    LINKAGE: int
    NVOD_REFERENCE: int
    TIME_SHIFTED_SERVICE: int
    SHORT_EVENT: int
    EXTENDED_EVENT: int
    TIME_SHIFTED_EVENT: int
    COMPONENT: int
    MOSAIC: int
    STREAM_IDENTIFIER: int
    CA_IDENTIFIER: int
    CONTENT: int
    PARENTAL_RATING: int
    TELETEXT: int
    TELEPHONE: int
    LOCAL_TIME_OFFSET: int
    SUBTITLING: int
    TERRESTRIAL_DELIVERY_SYSTEM: int
    MULTILINGUAL_NETWORK_NAME: int
    MULTILINGUAL_BOUQUET_NAME: int
    MULTILINGUAL_SERVICE_NAME: int
    MULTILINGUAL_COMPONENT: int
    PRIVATE_DATA_SPECIFIER: int
    SERVICE_MOVE: int
    SHORT_SMOOTHING_BUFFER: int
    FREQUENCY_LIST: int
    PARTIAL_TRANSPORT_STREAM: int
    DATA_BROADCAST: int
    SCRAMBLING: int
    DATA_BROADCAST_ID: int
    TRANSPORT_STREAM: int
    DSNG: int
    PDC: int
    AC3: int
    ANCILLARY_DATA: int
    CELL_LIST: int
    CELL_FREQUENCY_LINK: int
    ANNOUNCEMENT_SUPPORT: int
    APPLICATION_SIGNALLING: int
    ADAPTATION_FIELD_DATA: int
    SERVICE_IDENTIFIER: int
    SERVICE_AVAILABILITY: int
    DEFAULT_AUTHORITY: int
    RELATED_CONTENT: int
    TVA_ID: int
    CONTENT_IDENTIFIER: int
    TIMESLICE_FEC_IDENTIFIER: int
    ECM_REPETITION_RATE: int
    S2_SATELLITE_DELIVERY_SYSTEM: int
    ENHANCED_AC3: int
    DTS: int
    AAC: int
    XAIT_LOCATION: int
    FTA_CONTENT_MANAGEMENT: int
    EXTENSION: int

class PMT:
    pcr_pid: int
    program_number: int
    descriptors: list[Descriptor]
    streams: list[PMTStream]

class PMTStream:
    stream_type: int
    pid: int
    descriptors: list[Descriptor]

class SectionType:
    UNKNOWN: int
    PAT: int
    PMT: int
    CAT: int
    TSDT: int
    EIT: int
    NIT: int
    BAT: int
    SDT: int
    TDT: int
    TOT: int
    SIT: int
    ATSC_TVCT: int
    ATSC_CVCT: int
    ATSC_MGT: int
    ATSC_ETT: int
    ATSC_EIT: int
    ATSC_STT: int
    ATSC_RRT: int
    SCTE_SIT: int

class Section:
    section_type: SectionType
    pid: int
    table_id: int
    subtable_extension: int
    version_number: int
    current_next_indicator: bool
    section_number: int
    last_section_number: int
    crc: int

    def get_data(self) -> GLib.Bytes:
        """Gets the original unparsed section data."""

    def get_pmt(self) -> PMT | None:
        """Parses the Program Map Table contained in the section."""

    @staticmethod
    def new(pid: int, data: bytes) -> Section:
        """Creates a new Section with the given PID and data."""

    def send_event(self, element: Gst.Element) -> bool:
        """Sends the section as a Gst event to the given element."""

class StreamType:
    RESERVED_00: int
    VIDEO_MPEG1: int
    VIDEO_MPEG2: int
    AUDIO_MPEG1: int
    AUDIO_MPEG2: int
    PRIVATE_SECTIONS: int
    PRIVATE_PES_PACKETS: int
    MHEG: int
    DSM_CC: int
    H_222_1: int
    DSMCC_A: int
    DSMCC_B: int
    DSMCC_C: int
    DSMCC_D: int
    AUXILIARY: int
    AUDIO_AAC_ADTS: int
    VIDEO_MPEG4: int
    AUDIO_AAC_LATM: int
    SL_FLEXMUX_PES_PACKETS: int
    SL_FLEXMUX_SECTIONS: int
    SYNCHRONIZED_DOWNLOAD: int
    METADATA_PES_PACKETS: int
    METADATA_SECTIONS: int
    METADATA_DATA_CAROUSEL: int
    METADATA_OBJECT_CAROUSEL: int
    METADATA_SYNCHRONIZED_DOWNLOAD: int
    MPEG2_IPMP: int
    VIDEO_H264: int
    AUDIO_AAC_CLEAN: int
    MPEG4_TIMED_TEXT: int
    VIDEO_RVC: int
    VIDEO_H264_SVC_SUB_BITSTREAM: int
    VIDEO_H264_MVC_SUB_BITSTREAM: int
    VIDEO_JP2K: int
    VIDEO_MPEG2_STEREO_ADDITIONAL_VIEW: int
    VIDEO_H264_STEREO_ADDITIONAL_VIEW: int
    VIDEO_HEVC: int
    VIDEO_JPEG_XS: int
    VIDEO_VVC: int
    IPMP_STREAM: int
    USER_PRIVATE_EA: int

class ScteStreamType:
    SUBTITLING: int  # (130) – SCTE-27 Subtitling
    ISOCH_DATA: int  # (131) – SCTE-19 Isochronous data
    SIT: int  # (134) – SCTE-35 Splice Information Table
    DST_NRT: int  # (149) – SCTE-07 Data Service or Network Resource Table
    DSMCC_DCB: int  # (176) – Type B - DSM-CC Data Carousel [IEC 13818-6])
    SIGNALING: int  # (192) – Enhanced Television Application Signaling (OC-SP-ETV-AM1.0.1-120614)
    SYNC_DATA: int  # (194) – SCTE-07 Synchronous data
    ASYNC_DATA: int  # (195) – SCTE-53 Asynchronous data

def initialize() -> None:
    """Initializes the MPEG-TS helper library. Must be called before any usage."""

def message_parse_mpegts_section(message: Gst.Message) -> Section | None:
    """Returns the GstMpegts.Section contained in a message."""
