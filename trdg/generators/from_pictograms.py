import os
import random

from ..data_generator import FakeTextDataGenerator
from ..utils import load_dict, load_fonts


class GeneratorFromPictograms:
    """Generator that uses a given list of strings"""

    def __init__(
        self,
        pictogram_mapping,
        pictograms_path,
        count=-1,
        fonts=[],
        language="en",
        size=32,
        skewing_angle=0,
        random_skew=False,
        blur=0,
        random_blur=False,
        background_type=0,
        distorsion_type=0,
        distorsion_orientation=0,
        is_handwritten=False,
        width=-1,
        alignment=1,
        text_color="#282828",
        orientation=0,
        space_width=1.0,
        character_spacing=0,
        margins=(5, 5, 5, 5),
        fit=False,
        output_mask=False,
        word_split=False,
        image_dir=os.path.join(
            "..", os.path.split(os.path.realpath(__file__))[0], "images"
        ),
        stroke_width=0, 
        stroke_fill="#282828",
        image_mode="RGB",
    ):
        self.count = count
        self.fonts = fonts
        if len(fonts) == 0:
            self.fonts = load_fonts(language)
        self.language = language
        self.size = size
        self.skewing_angle = skewing_angle
        self.random_skew = random_skew
        self.blur = blur
        self.random_blur = random_blur
        self.background_type = background_type
        self.distorsion_type = distorsion_type
        self.distorsion_orientation = distorsion_orientation
        self.is_handwritten = is_handwritten
        self.width = width
        self.alignment = alignment
        self.text_color = text_color
        self.orientation = orientation
        self.space_width = space_width
        self.character_spacing = character_spacing
        self.margins = margins
        self.fit = fit
        self.output_mask = output_mask
        self.word_split = word_split
        self.image_dir = image_dir
        self.generated_count = 0
        self.stroke_width = stroke_width
        self.stroke_fill = stroke_fill
        self.image_mode = image_mode 
        self.pictograms_path = pictograms_path
        self.pictogram_mapping = pictogram_mapping
        self.pictogram_files = os.listdir(pictograms_path)

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

    def next(self):
        if self.generated_count == self.count:
            raise StopIteration
        self.generated_count += 1

        pictograms = self.getRandomPictos()
        print(len(pictograms))

        return (
            FakeTextDataGenerator.generate(
                self.generated_count,
                "",
                "",
                None,
                self.size,
                None,
                self.skewing_angle,
                self.random_skew,
                self.blur,
                self.random_blur,
                self.background_type,
                self.distorsion_type,
                self.distorsion_orientation,
                self.is_handwritten,
                0,
                self.width,
                self.alignment,
                self.text_color,
                self.orientation,
                self.space_width,
                self.character_spacing,
                self.margins,
                self.fit,
                self.output_mask,
                self.word_split,
                self.image_dir,
                self.stroke_width,
                self.stroke_fill,
                self.image_mode, 
                pictograms = pictograms,
                pictograms_path = self.pictograms_path,
                is_picto=True
            ),
            "".join([self.pictogram_mapping[p.replace(".png","")] if p.replace(".png","") in self.pictogram_mapping else "" for p in pictograms]),
        )

    def getRandomPictos(self):
        pictograms = []
        for i in range(random.randint(1,3)):
            pictograms.append(random.choice(self.pictogram_files))
        return pictograms
