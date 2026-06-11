## README.md — THE REAPER MARGIN (PROJECT REDGRAVE)
PROOF OF CONCEPT • PUBLIC DOMAIN SANDBOX
## 📌 OVERVIEW & DESIGN INTENT
THE REAPER MARGIN (Workshop Title: Project Redgrave) is an open-source, high-velocity character action mechanics framework. It is built specifically as a design template and code proof-of-concept (PoC) for independent developers. The goal is to provide a clean, modular structural blueprint that can be ported directly into engines like Unreal Engine, Unity, or Godot.
The game mechanics fuse aggressive, momentum-driven character combat with a corporate liquidation theme. Performance determines not just your score, but your real-time animation data, weapon speed, and character personality.
------------------------------
## 🎮 CORE MECHANICS## 1. The Kinetic Camera Blueprint
To facilitate unbroken combat momentum, the camera decouples from the player's shoulder and utilizes a wide-angle Dynamic Spring-Arm System:

* Standard State: Arm Length: 4.5m | FOV: 85°. Balanced spatial awareness.
* Momentum State (Slide/Grapple): Arm interpolates to 6.5m | FOV: 105°. High-velocity widescreen distortion.
* Vertical State (Bayonet Vault): Camera lags behind vertical Z-axis climb and tilts down 25°, keeping the arena floor fully visible.

## 2. Real-Time Execution Scaling (Personality & Frame Data)
Corey’s mechanical behavior, recovery windows, and audio profile scale dynamically across execution tiers:

* D–B Tiers [Liquidity Crisis]: High emotional friction. Corey is aggressive, frustrated, and uses vulgar or sarcastic taunts. Weapons feel heavy with high recovery frame counts.
* A–S Tiers [Compliant Operation]: Balanced corporate compliance. Corey uses disciplined military callouts. Movement and frame data are standardized.
* SS–SSS Tiers [The Black Margin]: Transition to the ex-military "Reaper" mindset. Corey goes completely quiet, letting her weapons do the talking. Animations become ultra-efficient, minimalist, and feature heavily shortened recovery windows.
* Ultimate State [Reaper Mode Overclock]: An amber night-vision tactical overlay engages and audio drops into low-frequency sub-bass pulses. Corey is dead silent. Cybernetics completely eliminate weapon transformation animation frames, enabling instant zero-frame configuration snaps.

------------------------------
## 🔄 THE CHIMAERA FRAME & HAZMAT MATRIX
To eliminate 3D asset-switching overhead, the player wields the Chimaera Frame—a single modular tool that pneumatically telescopes and reconfigures mid-combo. Elemental payloads can be re-routed on the fly:

* R2 / RT: Gun-Fu Form. Fires current weapon form (Pistols, Shotgun, Rifle, or Overclock AR).
* L2 / LT (Tap): Toggle configuration between Dual Pistols & Shotgun.
* L2 / LT (Hold ≥0.35s): Extend barrel into Anti-Material Sniper Form.
* Triangle / Y (Tap): Quick Bayonet Parry.
* Triangle / Y (Hold): Rear Rocket Booster Impact Smash.
* Triangle / Y (Mid-Air): Engage Hover Boots.
* Square / X: Grenade Bumper. Launch Cooldown-Based Elemental Canisters through injection lines.
* Circle / B (Ground): High-Velocity Slide.
* Circle / B (Air / Lock-On): Grapple Zip Cable.
* D-Pad: Element Cycle. Shift active internal core payload between Slag, Pyro, Cryo, and Volt.
* L3 + R3: Reaper Mode Overclock. Activate ultimate state when gauge hits 100%.

## 🧪 Hazmat Interaction Combinations

* Slag Fluid: Deploys a chemical oil slick. Corey's slide length and velocity are multiplied by 2.0x across it.
* Pyro Fluid: Blasting Pyro hitscan rounds or canisters into a Slag pool detonates it into a continuous thermal loop trap zone.
* Cryo Coolant: Flash-freezes targets. Freezing an airborne target turns them into a stationary physics anchor you can Grapple Zip off of to slingshot across gaps.
* Ionized Volt: Strips corporate energy shields. Firing it into a Slag pool electrifies the floor surface, allowing Corey to safely hover above using her Hover Boots.

------------------------------
## 👥 CHARACTER ROSTER SPREAD

Cordelia "Corey" Cross is the primary player character. Others are implemented as proof of scalability.

* Corey (The Reaper): High-speed, frame-canceling multi-form specialist utilizing the shifting Chimaera Frame.
* Debt Collector: Elite Stalker utilizing an Odachi, Dual Daggers, and a Coiled Whip-Blade for high-stagger tracking counters.
* Sage: Heavy hydraulic archetype using hyper-armor charge stances. Features a perfect "Hydraulic Re-route" manual parry/cancel loop.
* Glitch: Zero-frame timeline trickster that drops digital Rewind Buffer hologram anchors to snap back to previous spatial coordinates and health values.
* Zen: Tactical mirror-cloner and alchemist. Can freeze style decay during active shop browsing at the cost of a temporary corporate markup liability.

------------------------------
## 📉 THE PERFORMANCE AUDIT & LEDGER ENGINE
Traditional style ranks are rebranded into real-time corporate operational efficiency tracking, evaluated through the MasterPerformanceAuditEngine.

* Rank SSS: 5000+ points | Decay rate 60.0/s | 6.0x Gauge multiplier | The Black Margin (Silent / Cold)
* Rank SS: 3500 points | Decay rate 45.0/s | 4.5x Gauge multiplier | The Black Margin (Silent / Cold)
* Rank S: 2000 points | Decay rate 30.0/s | 3.0x Gauge multiplier | Compliant Operation (Professional)
* Rank A: 1000 points | Decay rate 20.0/s | 2.0x Gauge multiplier | Compliant Operation (Professional)
* Rank B: 500 points | Decay rate 15.0/s | 1.5x Gauge multiplier | Liquidity Crisis (Frustrated / Vulgar)
* Rank C: 150 points | Decay rate 10.0/s | 1.0x Gauge multiplier | Liquidity Crisis (Frustrated / Vulgar)
* Rank D: 0 points | Decay rate 5.0/s | 0.5x Gauge multiplier | Liquidity Crisis (Frustrated / Vulgar)

## ⏱️ Buzzer Beater Grace Period
When the Reaper Gauge empties, a strict 1.5-second grace window triggers. Landing an attack during this frame window secures a "Buzzer Beater" modifier, freezing your style points. Failing the window causes your points to plummet at 5x the normal decay rate.
## 📈 Master Economy Balancing Rules
To protect player progression from being choked out by poor execution penalties, the engine strictly isolates immediate funding from structural liabilities:

* Cash-In-Hand: Sourced from enemy drops. Spent at vending machines for immediate upgrades. It is never drained by mid-game performance penalties.
* Global Lifetime Debt: A persistent, overarching negative ledger balance. Structural damage (breaking glass/walls) and interest penalties accrued during a level are compiled and applied to this lifetime total only during the End-of-Level Financial Audit. High global debt values cause the aggressive Debt Collector Elite Stalker to spawn dynamically in future zones.

------------------------------
## 🔓 PUBLIC DOMAIN USE TERMS (CC0) [1] 
This project is completely dedicated to the public domain under Creative Commons Zero (CC0).
You are free to take this documentation, underlying mathematics, structural systems, and character configurations to use in standalone indie developments, conversion mods, or full commercial projects. No attribution required, no licensing strings attached. Build upon it, modify it, change it, and make it your own.

