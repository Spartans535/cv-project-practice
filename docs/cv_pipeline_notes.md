# Computer Vision Foundations & Task Taxonomy

## Core Definitions
* **Computer Vision (CV):** The field of AI enabling systems to extract meaningful information from digital images, videos, or visual inputs.
* **Matrix Representation:** Input data is processed as an array of pixel intensities across color channels (RGB).

## Task Taxonomy
| Task | Core Objective | Primary Output |
| :--- | :--- | :--- |
| **Classification** | Identify global image contents | Single Class Label |
| **Object Detection** | Localize and identify discrete items | Bounding Boxes $(x, y, w, h)$ + Labels |
| **Segmentation** | Deep pixel-level boundary isolation | Binary/Categorical Pixel Masks |
| **Pose Estimation** | Map structural coordinates of a subject | Anatomical Keypoints $(x, y)$ |
| **Tracking** | Maintain identity across temporal sequences | Unique Object IDs ($ID\_01$, $ID\_02$) |

## Architectural Scope
* **Non-Sequential Models:** Frame-isolated inference (e.g., standard YOLO object detection).
* **Sequential Models:** Frame-sequence analysis accounting for temporal dynamics (essential for action classification and behavior modeling).
---

## Data Collection & Environmental Constraints

### The Core Law
* **Garbage In, Garbage Out (GIGO):** Pipeline efficacy is directly bound to dataset quality. Model optimization cannot compensate for fundamentally flawed training data.

### Production Dataset Anomalies
1. **Lighting Variance:** Fluctuations in lux levels (glare, shadows, low-light) change pixel intensity matrices drastically, causing inference failure if unrepresented in training.
2. **Occlusion:** Truncation or partial masking of target subjects by structural objects. Models must be exposed to partial features to ensure robust feature extraction.
3. **Domain Shift:** Architectural divergence between the training distribution (source domain) and the live production environment (target domain).
4. **Data Imbalance:** Severe class distribution asymmetry (e.g., Anomaly Detection where negative samples vastly outnumber critical positive samples), forcing the model to bias toward the majority class.

### Benchmark Infrastructure: COCO Dataset
* **Significance:** Industry-standard evaluation benchmark featuring 330k+ images. It provides foundational spatial context for object localization, semantic segmentation, and human pose keypoint mapping.
---

## Data Annotation Infrastructure

### Core Objective
* **Supervised Learning Ground Truth:** Raw visual data requires human-generated categorical constraints (labels) to establish a mathematical target during model optimization.

### Annotation Schema & Data Formats
1. **Bounding Boxes:** Represented via absolute/normalized spatial vectors. Standard YOLO formatting uses: `[class_index, x_center, y_center, width, height]`.
2. **Segmentation Masks:** Highly granular pixel-wise coordinate arrays. Maps binary or multi-class masks directly onto the spatial landscape of the image.
3. **Pose Keypoint Mapping:** Explicit spatial coordinate tracking of anatomical target nodes $(x, y)$ configured with a visibility topology vector $(v)$ indicating occlusion status.
4. **Temporal Indexing:** Frame-range labeling over a sequential timeline timeline (e.g., `[Frame 120-180: Fall_Event]`), establishing temporal bounding boxes for sequential action recognition.

### Tooling Ecosystem
* **CVAT:** Enterprise-grade open-source video annotation frame-engine optimized for heavy object-tracking and pose datasets.
* **Roboflow:** Specialized cloud platform aggregating collection, formatting, and augmentation pipelines into a clean development workflow.