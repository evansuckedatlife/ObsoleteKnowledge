---
type: term
category: science
defines: [BIOS, firmware, UEFI, CMOS]
related: ["[[motherboard]]", "[[central-processing-unit]]", "[[power-supply-unit]]"]
requires: []
lists: ["[[computer-components]]"]
tour_order: 0
read: false
---

# BIOS

## summary

The **BIOS** (Basic Input/Output System) is firmware—a low-level software program stored on the motherboard—that initializes all hardware at power-up and hands control to the operating system. Modern systems use **UEFI** (Unified Extensible Firmware Interface), a more advanced standard replacing legacy BIOS, offering better security, faster boot, and support for larger drives.

## you gotta know

- BIOS/UEFI is *non-volatile* firmware, stored in a small flash memory chip (historically an EEPROM) on the motherboard; it persists when power is lost, unlike RAM.
- At *power-on*, the CPU executes BIOS instructions first; BIOS discovers CPU, RAM, storage, and expansion cards, performs *self-tests*, and then loads the operating system from the boot device.
- UEFI uses a *Graphical User Interface* (menus, mouse support) and runs in a 32/64-bit protected mode, versus legacy BIOS running in 16-bit real mode; this makes UEFI faster and more capable.
- The BIOS *settings* are user-configurable via the Setup utility (entered at boot, typically by pressing F2, Del, or F10 during startup); settings control CPU clock multiplier, RAM timing, boot order, and security features.
- *Secure Boot* (UEFI feature) verifies the bootloader's digital signature before executing it, preventing *rootkits* that load before the OS; Windows requires Secure Boot, though it can be disabled for Linux or custom kernels.
- *CMOS* (Complementary Metal-Oxide Semiconductor) is a small, battery-backed memory chip holding BIOS settings; the battery (coin cell on the motherboard) keeps settings when the system is powered off.
- BIOS *updates* ("flashing the BIOS") involve rewriting the firmware with a newer version to fix bugs, add CPU support, or improve performance; flashing is delicate—a power loss during flashing can brick the motherboard.
- The *TPM* (Trusted Platform Module) is a security chip accessed by the BIOS and OS to store cryptographic keys and perform secure operations; it is integrated on modern motherboards.

## connections

- [[motherboard]] — BIOS firmware lives on the motherboard's flash chip; the motherboard's design determines CPU models supported, RAM timings, and PCIe options exposed via BIOS.
- [[central-processing-unit]] — BIOS initializes the CPU, configuring clock speeds, voltage, and cores; BIOS sets multipliers that determine the final CPU frequency.
- [[power-supply-unit]] — BIOS configures voltage regulators on the motherboard via PMBus signaling; correct voltage delivery depends on proper BIOS CPU configuration.

## see also

- [[motherboard]] · [[central-processing-unit]] · [[power-supply-unit]]

<!-- crosslinks -->
```dataviewjs
dv.view("_dv/crosslinks")
```
<!-- /crosslinks -->

<!-- tournav -->
```dataviewjs
dv.view("_dv/tournav")
```
<!-- /tournav -->

<!-- footer -->

---

Lists: [[computer-components]] · Mark read: `INPUT[toggle:read]`
