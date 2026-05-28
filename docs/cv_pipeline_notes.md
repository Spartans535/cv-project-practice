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
---

## Model Training Mechanics & Evaluation Metrics

### The Training Optimization Loop
* **Forward Pass:** The architecture processes input arrays to generate bounding box and class coordinate predictions.
* **Loss Computation:** Algorithmic calculation of error between empirical predictions and human ground truth annotations.
* **Backward Pass (Backpropagation):** Differentiating the loss function to adjust internal parameters (weights) to minimize error on subsequent iterations.

### Core Variables
* **Epoch:** A single full training pass across the entire active training dataset distribution.
* **Batch Size:** Sub-segment data arrays processed concurrently prior to parameter optimization.
* **Overfitting:** High variance anomaly where the model learns training distribution noise rather than generalized features, resulting in failure on out-of-distribution test items.

### Data Partitioning Strategies
* **Train Set:** Base data array utilized directly for weight optimization.
* **Validation Set:** Unseen calibration array used during hyperparameter tuning to monitor generalization capacity.
* **Test Set:** Pristine, isolated evaluation array held strictly to calculate ultimate production performance benchmarks.

### Matrix Evaluation Analytics
* **Precision:** True Positives divided by Total Predicted Positives. Quantifies false-positive suppression performance.
* **Recall:** True Positives divided by Total Actual Ground Truth Positives. Quantifies false-negative suppression performance.
* **IoU (Intersection over Union):** Spatial overlapping evaluation parameter mapping the intersection area divided by the union area of bounding boxes.
* **mAP (Mean Average Precision):** The integral mean of precision-recall curves across IoU thresholds. Serves as the primary performance benchmark metric for object detection pipelines.
---

## Production Lifecycle & Core Engineering Glossary

### The End-to-End MLOps Pipeline
1. **Data Collection:** Curating raw inputs representative of the ultimate deployment domain.
2. **Annotation:** Establishing structural constraints (bounding boxes, masks, keypoints) as targets.
3. **Data Splitting:** Protecting model evaluation integrity via structured Train/Val/Test partitioning.
4. **Training:** Iterative structural weight alignment driven by backpropagation and loss optimization.
5. **Evaluation:** Verifying out-of-distribution performance using localized confusion matrix analytics.
6. **Deployment:** Compiling the inference model engine into active execution environments (e.g., local webcam streams).
7. **Monitoring:** Tracking real-world telemetry to identify accuracy degradation, triggering subsequent data-collection cycles.

### Comprehensive Engineering Glossary
* **Classification:** Categorizing an entire visual scene into a singular global identity class.
* **Object Detection:** Simultaneous multi-target localized spatial coordinates tracking using bounding boxes.
* **Segmentation:** Micro-level pixel-by-pixel categorical isolation mapping precise boundary definitions.
* **Pose Estimation:** Calculating coordinates mapping explicit topological body joints and structural nodes.
* **Annotation:** Human-in-the-loop processing mapping ground-truth targets onto raw matrices.
* **Overfitting:** The extreme optimization variance where a network memorizes training features instead of distilling generalized trends.
* **Precision:** The mathematical metric evaluating false-positive mitigation performance ($\frac{\text{True Positives}}{\text{Total Predicted Positives}}$).
* **Recall:** The mathematical metric evaluating false-negative mitigation performance ($\frac{\text{True Positives}}{\text{Total Actual Positives}}$).
* **IoU (Intersection over Union):** The spatial overlap performance ratio bounding predicted boxes against annotated truths.
* **Deployment:** Integrating an optimized network matrix into production software layers to perform live inference calculations.