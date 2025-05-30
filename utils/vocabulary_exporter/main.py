from __future__ import annotations

import argparse

from core import Vocabulary, VSCodeRevealExporter


def parse_args() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Export English vocabulary into various formats")

    parser.add_argument(
        "-i",
        "--input",
        dest="input_vocab_file_path",
        type=str,
        required=True,
        help="Input vocabulary file path in YAML format",
    )
    parser.add_argument(
        "-o",
        "--output",
        dest="export_output_file_path",
        type=str,
        required=True,
        help="Output file path to save the exported vocabulary to",
    )

    return parser.parse_args()


def main() -> None:
    parser = parse_args()

    vocabulary = Vocabulary.from_yaml(parser.input_vocab_file_path)
    exporter = VSCodeRevealExporter(parser.export_output_file_path)
    exporter.export(vocabulary)


if __name__ == "__main__":
    main()
