# ClubOS Lite – LLM Situations Reference

This document defines the role, purpose, and document context of each LLM wrapper used in ClubOS Lite.

---

## 1. BookingLLM

- **Purpose**: Handles all booking-related inquiries.
- **Examples**: Returns, booking changes, access issues (e.g., code not working).
- **Attached Document**: `booking_flow_v3.md`
- **Tone**: Operational, clear, slightly sharp.

---

## 2. EmergencyLLM

- **Purpose**: Responds to critical system issues or safety concerns.
- **Examples**: Power outages, multi-bay failures, medical emergencies, system down.
- **Attached Document**: `emergency_protocol.md`
- **Tone**: Blunt, direct, zero-fluff triage operator.

---

## 3. TrackManLLM

- **Purpose**: Troubleshoots simulator hardware issues.
- **Examples**: Ball not tracking, side screens not working, system frozen.
- **Attached Document**: `trackman_ops_manual.md`
- **Tone**: Technical, helpful, no upselling.

---

## 4. ResponseToneLLM

- **Purpose**: Wraps and rewrites output or replies to match Clubhouse’s voice.
- **Examples**: Any message needing brand polish or humor/tone fix.
- **Attached Document**: `tone_rules.md`
- **Tone**: Dry, confident, sarcastic when appropriate.

---

## 5. ClubhouseInfoLLM

- **Purpose**: General knowledge reference across all Clubhouse systems and operations.
- **Examples**: Pricing, how the automation works, support philosophy, membership logic.
- **Attached Document**: `clubhouse_reference.md` (currently — SOP doc can replace)
- **Tone**: Friendly, informative, operational clarity.

---

## 6. SelectorLLM (Router)

- **Purpose**: Detects intent and routes to correct LLM automatically.
- **Routing Source**: Keyword-based (will evolve into classifier)
- **Tone**: Uses underlying LLM’s tone + optional tone enforcement via `?tone=strict`

---

# Notes

- `tone=strict` applies ResponseToneLLM after any LLM run
- `stream=True` enables streaming response behavior
- All LLMs can be memory-wrapped or log-monitored individually