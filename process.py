import argparse

from pypdf import PdfReader, PdfWriter
from pypdf.generic import RectangleObject

INCH = 72  # PDF points per inch
LABEL_WIDTH = 4 * INCH
LABEL_HEIGHT = 6 * INCH

# Centre of the label content on the unrotated A4 page, in PDF points
# (measured from input.pdf: content spans x 152-558, y 12-305).
LABEL_CENTRE_X = (152.06 + 557.71) / 2
LABEL_CENTRE_Y = (12.0 + 305.0) / 2


def process_pdf(input, output):

    reader = PdfReader(input)
    writer = PdfWriter()

    writer.add_page(reader.pages[0])
    page = writer.pages[0]

    # The label is printed sideways in the bottom-right of the unrotated page,
    # so crop around it (6" wide x 4" tall) before rotating it upright to 4" x 6".
    box = RectangleObject(
        [
            LABEL_CENTRE_X - LABEL_HEIGHT / 2,
            LABEL_CENTRE_Y - LABEL_WIDTH / 2,
            LABEL_CENTRE_X + LABEL_HEIGHT / 2,
            LABEL_CENTRE_Y + LABEL_WIDTH / 2,
        ]
    )
    page.mediabox = box
    page.cropbox = box

    page.rotate(270)

    writer.write(output)


def parse_args():
    parser = argparse.ArgumentParser(description="Fix InPost label format for .")
    parser.add_argument(
        "-i",
        "--input",
        help="path of the pdf to process",
    )
    parser.add_argument(
        "-o",
        "--output",
        help="path of the processed pdf to output",
    )
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = parse_args()
    process_pdf(args.input, args.output)
