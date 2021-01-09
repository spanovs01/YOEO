import imgaug.augmenters as iaa
from .transforms import *

class DefaultAug(ImgAug):
    def __init__(self, ):
        self.augmentations = iaa.Sequential([
            iaa.Dropout([0.0, 0.1]),      # drop 5% or 20% of all pixels
            iaa.Sharpen((0.0, 0.2)),       # sharpen the image
            iaa.Affine(rotate=(-20, 20), translate_percent=(-0.2,0.2)),  # rotate by -45 to 45 degrees (affects segmaps)
            iaa.AddToBrightness((-30, 30)), 
            iaa.AddToHue((-20, 20)),
            iaa.Fliplr(0.5),
            #iaa.ElasticTransformation(alpha=80, sigma=10)  # apply water effect (affects segmaps)
        ], random_order=True)


AUGMENTATION_TRANSFORMS = transforms.Compose([
        AbsoluteLabels(),
        DefaultAug(),
        PadSquare(),
        RelativeLabels(),
        ToTensor(),
    ])
