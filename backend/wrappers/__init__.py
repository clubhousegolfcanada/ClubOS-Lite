from .emergency_llm import EmergencyLLM
from .booking_llm import BookingLLM
from .trackman_llm import TrackManLLM
from .response_tone_llm import ResponseToneLLM
from .vanilla_llm import VanillaLLM

WRAPPERS = {
    "EmergencyLLM": EmergencyLLM(),
    "BookingLLM": BookingLLM(),
    "TrackManLLM": TrackManLLM(),
    "ResponseToneLLM": ResponseToneLLM(),
    "VanillaLLM": VanillaLLM()
}