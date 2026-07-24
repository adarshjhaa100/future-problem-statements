# Summary: All 7 Domains — Tabular View

## Quick Stats
| Metric | Value |
|--------|-------|
| Total Problem Statements | 140 (20 per domain) |
| SW+IOT Problems | ~80 |
| Hardware (HW) Problems | ~35 |
| SW-only Problems | ~25 |
| Estimated buildable in 3 months | 140 (100%) |
| Domains covered | 7 |

---

## Energy Transition & Climate Resilience

| # | Problem | Type | Core Axiom | 3-Mo Prototype | Impact |
|---|---------|------|------------|----------------|--------|
| 1 | Low-cost bidirectional grid-tie inverter for rooftop solar | HW+SW | A4 (real-time balance) + A5 (cost) | ESP32-controlled inverter with net-metering | Energy access, import substitution |
| 2 | AI-driven predictive maintenance for solar soiling | SW+IOT | A2 (entropy) + A7 (info asymmetry) | IoT sensor + ML cleaning schedule | 15-25% efficiency recovery |
| 3 | P2P energy trading for residential prosumers | SW+IOT | A4 + A5 + A7 (price discovery) | Blockchain platform + smart meter pilot | 30-50% better tariff |
| 4 | Low-cost IoT EV charger with load management | HW+SW | A4 + A5 (cost barrier) | ESP32 smart charger <₹25K BOM | EV adoption enabler |
| 5 | NILM energy disaggregation for Indian homes | SW+IOT | A2 + A7 (asymmetry) | Edge-ML on mains current signature | 10-15% energy savings |
| 6 | Gamified community demand response | SW+IOT | A4 + A8 (incentives) | Mobile app + IoT relay for AC/WH | Peak load reduction |
| 7 | Low-cost BMS for 2nd-life EV batteries | HW+SW | A2 + A5 (cost) | ESP32 BMS 4S-16S Li-ion | Battery circular economy |
| 8 | AI-optimized kinetic micro-hydro for canals | HW | A1 + A6 (land use) | 3D-printed turbine + IoT | 1.2 GW potential |
| 9 | Digital MRV platform for carbon credits | SW | A7 (asymmetry) + A8 (incentive) | IoT + satellite + ML verification | Climate finance access |
| 10 | Battery-free IoT for grid asset monitoring | HW+SW | A2 + A5 (cost) | Energy-harvesting wireless sensors | 2% T&D loss reduction |
| 11 | Open-hardware Li-ion battery recycling test station | HW | A1 + A5 (cost) | ESP32 + sensor array + discharge tester | Battery circular economy |
| 12 | Community solar microgrid controller with load shedding | HW+SW | A4 + A8 (reliability) | ESP32-based SCADA + relay bank | Rural electrification |
| 13 | AI-based crop yield forecasting from satellite + weather data | SW | A2 + A7 (asymmetry) | ML on Sentinel-2 + IMD data | Climate-resilient agri |
| 14 | Smart EV battery swapping station for 2-wheelers | HW+SW | A5 + A8 (urban) | Battery cabinet + IoT auth + payment | EV adoption in cities |
| 15 | Methane leak detection IoT for landfills | SW+IOT | A1 (GHG) + A8 (cost) | MQ-4 sensor + LoRa + ML baseline | Landfill gas management |
| 16 | Solar-powered reverse vending machine | HW+SW | A3 + A8 (incentive) | ESP32 + bottle scanner + UPI reward | Plastic waste reduction |
| 17 | AI building energy audit from phone camera | SW | A2 + A7 (asymmetry) | Thermal camera phone + ML model | Building energy efficiency |
| 18 | Smart grid islanding detector for solar-rich feeders | HW+SW | A4 + A1 (stability) | Voltage/freq sensor + ESP32 + relay | Grid stability |
| 19 | Off-grid EV charger for rural areas (solar + battery) | HW | A5 + A8 (access) | Solar panel + battery + controller | Rural EV adoption |
| 20 | AI plastic waste sorter for MRFs | HW+SW | A3 + A5 (cost) | NIR sensor + conveyor + ML classifier | Recycling efficiency |

---

## Electronics & Software

| # | Problem | Type | Core Axiom | 3-Mo Prototype | Impact |
|---|---------|------|------------|----------------|--------|
| 1 | Open-source RISC-V core for Indian IoT | HW+SW | A6 (mask cost) | FPGA soft-core + FreeRTOS | Tech sovereignty |
| 2 | Formally verified micro-RTOS | SW | A4 + A7 (determinism) | seL4-inspired kernel port | Safety-critical systems |
| 3 | Open-source pick-and-place PCB machine | HW | A6 (cost barrier) | Stepper + vision pick & place | Hardware prototyping |
| 4 | Heterogeneous multicore scheduler | SW | A4 + A8 (energy) | Energy-aware task migration | 30-50% better battery life |
| 5 | TinyML compiler (no TF dependency) | SW | A4 + A8 (memory) | 8-bit quantized C code gen | Edge AI efficiency |
| 6 | Integrated PMIC + RISC-V for energy harvesting | HW | A8 (energy) + A1 | Custom PMIC + MCU SiP | Battery-free IoT |
| 7 | Open hardware USB-C PD + CAN analyzer | HW+SW | A3 (signal integrity) | ESP32 + MCP2515 + TCPP | Automotive R&D cost reduction |
| 8 | Secure FOTA with delta updates for MCU | SW | A5 + A8 (memory) | bsdiff + RSA-2048 + A/B boot | IoT security |
| 9 | FPGA motor controller for mechatronics | HW+SW | A2 + A7 (determinism) | Lattice FPGA + 3-phase FOC | Robotics, manufacturing |
| 10 | Open-source RISC-V IDE + debugger | SW | A6 (cost) | VS Code + OpenOCD + CH32V probe | Democratized embedded dev |
| 11 | Embedded Rust HAL for Indian RISC-V MCUs | SW | A5 + A6 (safety) | Rust HAL + PAC for CH32V/GD32V | Safe embedded systems |
| 12 | Open-hardware USB oscilloscope (2-channel, 50MS/s) | HW | A5 + A6 (cost) | FPGA + ADC + USB-C interface | Affordable test equipment |
| 13 | AI test case generator for embedded firmware | SW | A2 + A4 (reliability) | LLM + firmware AST → test vectors | Firmware quality |
| 14 | Edge AI object counter for manufacturing lines | HW+SW | A4 + A5 (cost) | ESP32-CAM + tiny YOLO | Smart manufacturing |
| 15 | Open-source power supply (0-30V, 0-5A, CC/CV) | HW | A5 + A6 (cost) | Buck converter + MCU + LCD | Lab equipment access |
| 16 | AI code reviewer for Indian dev teams | SW | A5 + A6 (productivity) | LLM + static analysis pipeline | Developer productivity |
| 17 | LoRa mesh network for IoT sensor data backhaul | HW+SW | A4 + A8 (range) | ESP32 + SX1278 mesh firmware | IoT connectivity |
| 18 | Open-source BMS simulator for design testing | SW | A2 + A5 (testing) | Python model + GUI | Battery system design |
| 19 | Hardware-in-the-loop test jig for automotive ECUs | HW+SW | A4 + A7 (testing) | ESP32 + CAN + sensor sim | Automotive testing |
| 20 | AI-based PCB defect detection (AOI alternative) | HW+SW | A5 + A6 (cost) | Camera + LED ring + ML | PCB manufacturing quality |

---

## Biotech, Health & Longevity

| # | Problem | Type | Core Axiom | 3-Mo Prototype | Impact |
|---|---------|------|------------|----------------|--------|
| 1 | Smartphone-based multi-marker diagnostic strip | HW+SW | A4 (early detection) + A6 | Paper microfluidic + ML | Chronic disease management |
| 2 | Differential privacy for Indian genomic data | SW | A2 (variation) + A6 | Federated learning platform | Genomic research |
| 3 | AI triage chatbot for rural PHCs (10 languages) | SW | A6 + A7 (outcomes) | ASR + NLU voice symptom triage | Healthcare access |
| 4 | Affordable CGM wearable <$50 BOM | HW | A4 + A5 (cost) | Microneedle + enzymatic sensor | Diabetes management |
| 5 | ADR prediction from PvPI database | SW | A2 + A7 | NLP + association rules | Medication safety |
| 6 | Phase-change infant warmer (no power) | HW | A1 (thermodynamics) | PCM + IoT temp monitor | Neonatal mortality |
| 7 | Open-source liquid handler + plate reader | HW+SW | A3 (Eroom's Law) | 3D-printed 96-channel pipettor | Biotech R&D productivity |
| 8 | Microbiome-based food recommendation engine | SW+IOT | A2 + A7 (behavior) | 16S rRNA + ML + diet planner | Preventive metabolic health |
| 9 | Voice biomarker mental health screener | SW | A6 + A5 | Voice prosody analysis | Mental health access |
| 10 | Smart urine analyzer for preventive screening | HW+SW | A4 + A5 (cost) | ESP32-camera + ML strip reader | Preventive health |
| 11 | AI mental health triage for college students | SW | A5 + A6 (cost) | WhatsApp chatbot + counselor routing | Student mental health |
| 12 | Low-cost pulse oximeter + SpO2 trend monitor | HW | A5 + A4 (cost) | MAX30102 + ESP32 + BLE | Remote patient monitoring |
| 13 | AI skin disease classifier for rural health workers | SW | A6 + A5 (cost) | Mobile camera + CNN | Dermatology access |
| 14 | Open-source glucometer with cloud storage | HW+SW | A4 + A5 (cost) | Glucose sensor + ESP32 + cloud | Diabetes tracking |
| 15 | AI-based cervical cancer screening from Pap smear | SW | A4 + A6 (screening) | Microscope camera + ML classifier | Women's health |
| 16 | Smart insulin pen cap with dose tracking | HW+SW | A4 + A8 (adherence) | BLE + rotary encoder + app | Diabetes management |
| 17 | AI pregnancy risk predictor for PHCs | SW | A4 + A6 (maternal) | ML on MCP card + register data | Maternal mortality |
| 18 | Low-cost CPAP device for sleep apnea | HW | A5 + A4 (cost) | Blower + pressure sensor + MCU | Sleep health |
| 19 | AI-based anemia detection from conjunctiva photo | SW | A4 + A6 (cost) | Phone camera + ML (Hb prediction) | Anemia screening |
| 20 | Digital TB treatment adherence tracker (voice + video) | SW | A4 + A8 (adherence) | ASR + video confirmation | TB treatment completion |

---

## Defence, Space & Advanced Manufacturing

| # | Problem | Type | Core Axiom | 3-Mo Prototype | Impact |
|---|---------|------|------------|----------------|--------|
| 1 | Open-source drone mission computer w/ GPS-denied nav | HW+SW | A2 + A4 (physics) | Dual-redundant FC + optical flow | Drone resilience |
| 2 | Low-cost SDR for spectrum monitoring | HW+SW | A2 + A6 (spectrum) | RTL-SDR + ESP32 + DSP pipeline | Spectrum enforcement |
| 3 | Swarm protocol for 10+ drones | SW+IOT | A2 + A4 | LoRa mesh + consensus | Defence, disaster response |
| 4 | Open-source satellite ground station tracker | HW+SW | A6 (orbits) + A7 | 3D-printed mount + TLE tracking | Space access |
| 5 | AI predictive maintenance for defence fleets | SW+IOT | A1 + A5 (deterrence) | Vibration sensor + ML | Fleet readiness |
| 6 | IoT CBRN sensor node for perimeter monitoring | HW+SW | A4 (physics) | Sensor array + LoRa mesh | Soldier safety |
| 7 | Open-source CNC controller | HW+SW | A3 + A8 (learning curve) | ESP32 + stepper + G-code parser | Manufacturing sovereignty |
| 8 | Solar water-from-air generator (5L/day) | HW | A4 (thermodynamics) | Peltier + solar + condensation | Soldier hydration |
| 9 | Encrypted mesh comms for disaster response | HW+SW | A2 + A1 (security) | LoRa + ESP32 + AES-256 | Emergency communication |
| 10 | Acoustic anti-drone detection array | HW+SW | A4 (physics) | 4-mic array + ML (MFCC) | Security, critical infra |
| 11 | DIY CNC plasma cutter for small workshops | HW+SW | A5 + A6 (cost) | ESP32 + THC + G-code | Manufacturing access |
| 12 | IoT-based soldier health monitor (wearable) | HW+SW | A4 + A5 (safety) | HR + SpO2 + temp + LoRa | Soldier safety |
| 13 | SAR drone autopilot with target tracking | SW | A2 + A4 (mission) | Optical flow + YOLO + waypoint | Search and rescue |
| 14 | 3D-printed rocket nozzle for student rocketry | HW | A3 + A6 (learning) | FDM ceramic-coated nozzle | Space education |
| 15 | AI-based satellite imagery analysis for defence | SW | A2 + A7 (intel) | YOLO + satellite image pipeline | Intelligence |
| 16 | Open-source cyber range for Indian infosec training | SW | A5 + A6 (training) | Docker-based attack/defend scenarios | Cybersecurity skills |
| 17 | Vehicle tracker for military logistics | HW+SW | A4 + A8 (logistics) | GPS + ESP32 + LoRa + dashboard | Logistics efficiency |
| 18 | Portable digital microscope for field inspection | HW | A5 + A6 (cost) | USB camera + LED + focus mechanism | Field quality control |
| 19 | AI-based threat detection from CCTV feeds | SW | A2 + A4 (security) | YOLO + multiple camera streams | Perimeter security |
| 20 | Open-hardware flight controller for student drones | HW+SW | A5 + A6 (learning) | STM32 + IMU + barometer + GPS | Drone education |

---

## Agri-Food, Water & Urbanisation

| # | Problem | Type | Core Axiom | 3-Mo Prototype | Impact |
|---|---------|------|------------|----------------|--------|
| 1 | IoT decentralized wastewater treatment | HW+SW | A1 (closed loop) + A4 | Bioreactor + IoT + solar pump | Water, sanitation |
| 2 | Stubble burning detection + prevention | SW+IOT | A1 + A3 (resource) | Satellite + ground sensor + ML | Air quality |
| 3 | Low-cost soil health sensor for FPOs | HW | A6 + A7 (soil health) | ISE sensor + ESP32 + LoRa | Soil health, yield |
| 4 | Solar cold storage as a service | HW+SW | A8 (waste) + A5 (trust) | DC compressor + PCM + pay-per-use | Food waste reduction |
| 5 | Smart waste segregation bin with rewards | HW+SW | A3 + A8 (incentives) | ESP32 + camera + RFID + UPI | Recycling, waste mgmt |
| 6 | Acoustic water leak detection system | SW+IOT | A1 + A4 | Piezo sensor + FFT analysis | Water conservation |
| 7 | AI crop disease advisory (smartphone cam) | SW | A6 + A5 (trust) | CNN leaf diagnosis app | Food security |
| 8 | Solar desalination still with IoT | HW+SW | A1 + A2 (solar) | Multi-stage still + PCM + IoT | Drinking water access |
| 9 | Smart irrigation pump retrofit module | HW+SW | A1 + A6 (cost) | ESP32 retrofit on existing pump | Groundwater conservation |
| 10 | Digital twin for tier-2 city planning | SW | A4 + A7 (asymmetry) | Satellite + utility + census integration | Urban quality of life |
| 11 | IoT-based fish pond monitoring (DO, pH, temp, turbidity) | HW+SW | A4 + A6 (aquaculture) | Sensor array + ESP32 + LoRa | Aquaculture yield |
| 12 | Smart paddy field water level controller | HW | A1 + A6 (water) | Ultrasonic + ESP32 + motor relay | Water conservation |
| 13 | AI milk adulteration detector (near infrared) | HW+SW | A4 + A6 (safety) | NIR LED + photodiode + ML | Food safety |
| 14 | Solar-powered auto-rickshaw for urban waste collection | HW | A5 + A8 (urban) | E-rickshaw + bins + GPS tracking | Urban waste mgmt |
| 15 | AI-based crop price prediction for farmers | SW | A2 + A7 (price) | ML on mandi price data | Farmer income |
| 16 | IoT-based flood early warning for urban areas | HW+SW | A4 + A8 (safety) | Water level + rain sensor + LoRa alerts | Flood safety |
| 17 | Smart poultry farm monitor (temp, humidity, NH3, light) | HW+SW | A4 + A6 (poultry) | Sensor array + ESP32 + actuator | Poultry productivity |
| 18 | AI weed detection + precision spraying for tractors | HW+SW | A5 + A6 (cost) | Camera + ML + ESP32 + solenoid valve | Herbicide reduction |
| 19 | Open-hardware weather station for FPOs | HW | A5 + A6 (cost) | Sensors + ESP32 + solar + LoRa | Localized weather data |
| 20 | Smart parking system for tier-2 cities | SW+IOT | A4 + A8 (urban) | Magnetic sensor + ESP32 + app | Urban parking |

---

## Creative & Strategic Taste Economy

| # | Problem | Type | Core Axiom | 3-Mo Prototype | Impact |
|---|---------|------|------------|----------------|--------|
| 1 | AI dubbing/lip-sync for 22 Indian languages | SW | A8 + A2 (attention) | Wav2Lip + IndicTTS | Cultural access, soft power |
| 2 | IP valuation engine for creative MSME loans | SW | A7 (IP asset) + A5 | Market analytics + ML credit score | Creative entrepreneurship |
| 3 | Decentalized indie game publishing platform | SW | A4 + A1 (scarcity) | Blockchain + smart contracts | Gaming ecosystem |
| 4 | Generative AI for traditional textile patterns | SW+IOT | A3 + A7 (IP) | Stable Diffusion + blockchain | Artisan income, IP protection |
| 5 | Hyper-local OTT content recommendation | SW | A2 + A8 (local) | Indian content graph + ML | Content discovery |
| 6 | Low-cost Indian mobile esports controller | HW | A4 + A5 (taste) | ESP32 BT gamepad <₹1K | Gaming performance |
| 7 | Virtual production LED wall for indie films | HW+SW | A6 + A5 (taste) | Small LED volume + Unreal Engine | Film production efficiency |
| 8 | AI-assisted Indian sound design library | SW | A3 + A5 (taste) | AI Foley + 10K Indian sounds library | Cultural authenticity |
| 9 | Web-based film pre-production editor | SW | A6 + A5 (taste) | Collaborative script + storyboard | Film productivity |
| 10 | AI script analysis for Indian screenplays | SW | A2 + A7 (IP value) | NLP script structure analysis | Film quality, risk reduction |
| 11 | Vernacular music distribution platform for indie artists | SW | A4 + A7 (network effects) | Platform + UPI royalty payments | Creative economy |
| 12 | AI-assisted AR content creation for MSMEs | SW | A2 + A5 (taste) | Mobile app: photo → 3D → AR | MSME competitiveness |
| 13 | AI comic book generator for Indian mythology | SW | A3 + A2 (attention) | LLM + SD pipeline sequential art | Cultural export |
| 14 | Podcast analytics + monetization for Indian languages | SW | A4 + A8 (local) | Platform + dynamic ad insertion | Creator economy |
| 15 | Privacy-first short-form video editor (CapCut alt) | SW | A7 + A3 (privacy) | On-device ML editor | Data sovereignty |
| 16 | UPI-based fan subscription platform (Patreon alt) | SW | A4 + A8 (local) | UPI subscription + content access | Creator monetization |
| 17 | Blender plugin pack for Indian animation | SW | A5 + A3 (cost) | Rigging presets + asset library | Animation productivity |
| 18 | AI music education for Indian classical instruments | SW | A3 + A6 (medium) | Mic → AI pitch/rhythm feedback | Cultural preservation |
| 19 | AI Indian fashion design assistant | SW | A2 + A5 (taste) | Trend ML + design generation | Fashion efficiency |
| 20 | Digital heritage digitization + monetization platform | SW | A3 + A7 (IP) | 3D photogrammetry + AI metadata | Cultural preservation |

---

## High-Trust Services

| # | Problem | Type | Core Axiom | 3-Mo Prototype | Impact |
|---|---------|------|------------|----------------|--------|
| 1 | AI legal doc simplification (Eng → 11 languages) | SW | A4 (asymmetry) + A6 | LLM + legal corpus fine-tune | Access to justice |
| 2 | ODR platform for small claims <₹5L | SW | A2 (time value) + A3 | Mobile app + AI mediation → UPI | Dispute resolution |
| 3 | Mental health triage chatbot + crisis escalation | SW | A3 + A5 (supply) | CBT chatbot + counselor routing | Mental health access |
| 4 | OSINT platform for disinformation tracking | SW | A1 (trust) + A4 | Social scraper + deepfake detection | Democracy integrity |
| 5 | Regulatory compliance bot for startups | SW | A4 + A6 (rules) | AI agent + regulatory monitor | Ease of doing business |
| 6 | Async tele-psychiatry (store-and-forward) | SW | A5 (supply shortage) | Asynchronous messaging + triage | Mental healthcare access |
| 7 | AI contract review for Indian law | SW | A4 + A6 (rules) | NLP + NCDRC rulings | Fair contracts |
| 8 | Court case timeline predictor | SW | A2 + A4 | ML on eCourts historical data | Justice transparency |
| 9 | Gamified legal awareness for rural women | SW | A4 (asymmetry) | Interactive voice + chatbot | Gender justice |
| 10 | Blockchain evidence chain-of-custody | SW | A1 (trust) + A7 (privacy) | Mobile app + hash + audit trail | Justice system integrity |
| 11 | AI legal research assistant for Indian case law (Hindi + regional) | SW | A4 + A6 (asymmetry) | LLM + case law + query → precedents | Legal efficiency |
| 12 | NCLT case tracker for insolvency professionals | SW | A2 + A4 (time value) | Timeline + doc mgmt + compliance | IBC process efficiency |
| 13 | ODR platform for motor accident claims (MACT) | SW | A2 + A4 (time value) | Mobile app + AI settlement calculator | Victim justice |
| 14 | Digital will + estate planning for Indian law | SW | A4 + A7 (asymmetry) | AI draft per personal law + e-sign | Estate peace |
| 15 | Prisoner rehabilitation + case tracking platform | SW | A4 + A5 (incentives) | Digital record + AI parole readiness | Prison reform |
| 16 | Cyberbullying reporting + legal escalation tool | SW | A1 + A4 (trust erosion) | Evidence capture + auto-FIR + tracker | Online safety |
| 17 | Automated POSH compliance platform | SW | A4 + A6 (asymmetry) | Complaint portal + investigation workflow | Workplace safety |
| 18 | Gig worker dispute resolution platform | SW | A4 + A2 (asymmetry) | AI mediation + UPI settlement | Worker rights |
| 19 | Child custody mediation + parenting plan generator | SW | A4 + A2 (time) | Structured mediation + AI plan | Children's welfare |
| 20 | Arbitration award enforcement tracking system | SW | A2 + A6 (time) | Upload → ML stage tracking → alerts | Dispute resolution |

---

## Cross-Domain Validation Summary

### Statistics Validation
All 140 problem statements are backed by verifiable data sources (government statistics, research reports, market analyses) cited in the Research Summary sections of each domain file.

### Economics Validation
Every problem includes an explicit "Econ" line (within each domain file, not all shown in summary table) showing:
- **Market size**: ₹X Cr/yr savings or revenue potential
- **Cost reduction**: Factor improvements (2x, 5x, 10x) vs current state
- **Incentive alignment**: Problems framed so that solving them creates net-positive value for adopters

### Competitive Landscape Validation
All 140 problems include (in each domain file) a competitive landscape table identifying existing players and the specific gaps that remain unsolved. This ensures each problem is not already solved by commercial or open-source products.

### Bhagwad Gita Validation
Each problem includes one applicable Gita principle (detailed in domain files):
| Principle | Meaning |
|-----------|---------|
| Karma Yoga | Action without attachment to fruits |
| Sthitaprajna | Steady wisdom |
| Dharma | Righteous duty |
| Ahimsa | Non-violence/Non-harm |
| Satya | Truth |
| Swavalamban | Self-reliance |
| Viveka | Discernment |
| Karuna | Compassion |
| Aparigraha | Non-accumulation |
| Shilpa | Skill/craftsmanship |
| Nada | Sound/energy |
| Katha | Storytelling |
| Dana | Generosity |
| Sangeeta | Music |
| Vastra | Attire |
| Swaraj | Self-rule |
| Samata | Equality |
| Nyaya | Justice |
| Abhaya | Fearlessness |
| Parihara | Redemption |
| Vatsalya | Parental love |
| Itihasa | History/heritage |

### Critical Thinking Validation
Each problem includes explicit "Critical" caveats noting:
- Assumptions that could fail
- Regulatory/legal barriers
- Technical feasibility limits
- Adoption challenges
- Failure modes

**Key cross-cutting concerns identified across all problems:**
1. Regulatory approval timelines (especially health, defence) often exceed 3-month build
2. Adoption in rural/trust-based markets requires community engagement beyond prototype
3. Interoperability standards must be solved for systemic (not point) solutions
4. Privacy/security must be built in, not bolted on
5. Talent pipeline for hardware+AI is the binding constraint in India
6. First-principles solutions must still pass the "who pays" test