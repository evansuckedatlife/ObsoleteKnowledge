---
type: term
category: science
defines: [GPU, graphics processing unit, graphics card, video card]
related: ["[[central-processing-unit]]", "[[pci-express]]", "[[motherboard]]", "[[power-supply-unit]]"]
requires: []
lists: ["[[computer-components]]"]
tour_order: 0
read: false
---

# Graphics Card

## summary

A **graphics card** (or GPU, graphics processing unit) is a specialized processor optimized for rendering images and video. It offloads graphics computations from the CPU, drastically improving performance for games, 3D modeling, and machine learning; modern GPUs contain thousands of small cores working in parallel.

## you gotta know

- The *fundamental role* of a GPU is *rasterization* (or *ray tracing*) — converting 3D scene data into a 2D image on a display, pixel by pixel, using highly parallel arithmetic.
- GPUs excel at *data parallelism*: they are built around thousands of small cores (compared to a CPU's handful of large cores), each executing the same operation on different data; this design dominates graphics, physics simulation, and deep learning.
- A GPU connects to the motherboard via *PCI Express*, typically a 16-lane x16 slot that offers 15+ GB/s of bandwidth, allowing the CPU to quickly transfer geometry and texture data.
- *VRAM* (video memory) — usually 4 GB to 24 GB of fast GDDR or HBM memory on the GPU card itself — stores the textures, framebuffers, and model data; it is separate from system RAM.
- *Framebuffer* is the portion of VRAM holding the current image to be displayed; the GPU writes pixels to the framebuffer, and a *display controller* reads it continuously, refreshing the monitor at 60 Hz or higher.
- Modern discrete GPUs are manufactured by *NVIDIA* (GeForce, Tesla, RTX), *AMD* (Radeon, RDNA), and *Intel* (Arc); each has proprietary driver software and compute ecosystems (CUDA for NVIDIA, HIP for AMD).
- Integrated GPUs (in the CPU) share system RAM and are slower but sufficient for office work and web browsing; discrete GPUs are necessary for gaming, professional 3D, and machine learning.
- GPUs generate significant *heat* and consume 50–450 watts depending on model; they require dedicated power connectors (6-pin, 8-pin, or dual 8-pin) directly from the PSU.

## connections

- [[central-processing-unit]] — the GPU and CPU work in tandem; the CPU prepares scene data, issues draw commands, and handles non-graphics logic, while the GPU executes the graphics pipeline in parallel.
- [[pci-express]] — the GPU plugs into a PCIe x16 slot; the bus bandwidth and latency are critical for CPU-GPU communication.
- [[motherboard]] — houses the PCIe slot and power delivery; the motherboard's *UEFI* initializes the GPU at boot.
- [[power-supply-unit]] — discrete GPUs require high wattage; an undersized PSU cannot deliver sustained power to a high-end GPU, causing crashes or throttling.
- [[cooling]] — GPUs are hotter than CPUs (70–85 °C under load); on-card cooling (fans or liquid) is mandatory.

## see also

- [[central-processing-unit]] · [[pci-express]] · [[motherboard]] · [[power-supply-unit]]

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
