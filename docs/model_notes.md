# Modern CV Models & Live Inference Pipelines

### 1. Object Detection Architecture (YOLO)
* **Mechanics:** One-stage anchor-free regression architecture that executes bounding box localization and multi-class mapping simultaneously in a single forward pass.
* **Inference vs. Training:** Training optimizes parameter weight thresholds via backpropagation. Inference passes live inputs through the static network weights file to compute immediate coordinate arrays.

### 2. Pose Estimation
* **Mechanics:** Models like `yolov8-pose` isolate localized target boxes and run secondary structural landmark calculations to generate coordinate maps of key anatomical nodes (joints).
* **Industrial Utility:** Provides directional kinematic orientation vectors, crucial for spatial behavior profiling, fall detection, and ergonomics monitoring.

### 3. Identity Tracking & Temporal Analysis
* **Tracking Engines (ByteTrack/DeepSORT):** Sits above spatial detection layers to assign persistent unique IDs to individual entities across sequential frames, tracking movement vector lines.
* **Temporal Models (LSTMs/Transformers):** Analyzes historical video blocks over a time-series matrix to classify dynamic compound activities (e.g., distinguishing walking from falling) that single static frames cannot identify.

### 4. Production Engineering Tradeoffs
* **The Latency/Accuracy Balance:** Large model variations (YOLOv8x) yield supreme precision but require heavy VRAM footprints and violate real-time latency budgets. Small iterations (YOLOv8n) offer rapid sub-10ms inference time, making them highly optimized for resource-restricted Edge hardware and embedded sensors.