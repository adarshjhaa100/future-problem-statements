# Replacement Logs

Problems swapped because a working solution already existed.

Pass 1 covered energy / agri / biotech (see README for narrative); the tables below are the **Pass 2** swaps, previously appended to the electronics, defence and creative domain files and moved here for cleanliness.

## Electronics & Software

| # | Replaced (was) | Existing solution found | Replaced with |
|---|----------------|------------------------|---------------|
| 3 | Open-source pick-and-place machine | LumenPnP / OpenPnP (sub-$1K open machines already ship) | EMI/EMC pre-compliance kit |
| 10 | RISC-V IDE + debugger toolchain | PlatformIO + OpenOCD + VS Code already support RISC-V | KiCad procurement & DFM plugin |
| 16 | Open-hardware RISC-V debug probe | CMSIS-DAP, WCH-Link, esp-prog (sub-$10 open probes exist) | Board bring-up copilot |
| 18 | WebUSB firmware flasher | esptool.js / ESP Web Serial tool already exist | Flying-probe in-circuit tester |

## Defence, Space & Advanced Manufacturing

| # | Replaced (was) | Existing solution found | Replaced with |
|---|----------------|------------------------|---------------|
| 1 | Open-source drone mission computer | Pixhawk / CubePilot already dominate; kept the real gap | GPS-denied visual-inertial odometry (reframed) |
| 2 | Low-cost SDR spectrum monitoring | RTL-SDR + GNU Radio is exactly this; the hardware is commodity | GNSS jamming & spoofing detection (reframed) |
| 4 | Satellite ground station tracker | SatNOGS fully solves this (open 3D-printed trackers + network) | Cubesat ADCS simulator + HIL testbed |
| 7 | Open-source CNC controller | GRBL / LinuxCNC / OpenBuilds controllers exist | Machine-tool condition monitoring |
| 9 | Encrypted mesh comms device | Meshtastic (LoRa + AES-256 + GPS + maps, open-source) | Software-defined HF/VHF tactical waveform |

## Creative & Strategic Taste Economy

| # | Replaced (was) | Existing solution found | Replaced with |
|---|----------------|------------------------|---------------|
| 1 | AI dubbing & lip-sync engine (22 languages) | Dubverse (India) already ships real-time lip-synced dubbing across 60+ languages; Rask and YouTube auto-dub too | Consent-based Indian voice corpus + licensing layer |
| 6 | Open-hardware mobile esports controller | Redgear, Flydigi and others sell sub-₹1,500 gamepads | Mobile-esports tournament integrity analytics |
