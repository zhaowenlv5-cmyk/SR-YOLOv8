# Ultralytics YOLO 🚀, AGPL-3.0 license

from .predict import DetectionPredictor, SRDetectionPredictor
from .train import DetectionTrainer, SRDetectionTrainer
from .val import DetectionValidator, SRDetectionValidator

__all__ = "DetectionPredictor", "DetectionTrainer", "DetectionValidator", "SRDetectionPredictor", "SRDetectionTrainer", "SRDetectionValidator"
