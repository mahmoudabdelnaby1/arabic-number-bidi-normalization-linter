#!/usr/bin/env python3
import argparse
import re
import sys
from pathlib import Path

def normalize_bidi_text(text):
    # Unify Arabic-Indic digits (٠١٢٣٤٥٦٧٨٩) to standard Arabic digits (0123456789)
    indic_to_arabic = str.maketrans("٠١٢٣٤٥٦٧٨٩", "0123456789")
    clean = text.translate(indic_to_arabic)
    # Fix punctuation reversals by wrapping standalone English numbers in LRM marks
    clean = re.sub(r'(\d+([.,]\d+)?\s*(SAR|EGP|AED|%))', '\u200e\\g<1>\u200f', clean)
    return clean

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--text", default="السعر: 150 SAR فقط!")
    args = p.parse_args()
    print(normalize_bidi_text(args.text))

if __name__ == "__main__":
    main()
