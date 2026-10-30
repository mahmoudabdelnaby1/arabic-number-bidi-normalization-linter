# Arabic Number Formatting & BiDi Text Normalization Linter

> Eliminate scrambled phone numbers, flipped percentages, and mixed numerals on Arabic web pages with automated BiDi normalization.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Format: CLI_SCRIPT](https://img.shields.io/badge/Format-CLI--SCRIPT-green.svg)](#)
[![Tier: 2](https://img.shields.io/badge/Tier-2-orange.svg)](#)
[![Region: MENA](https://img.shields.io/badge/Region-Egypt%20%7C%20GCC%20%7C%20Saudi-purple.svg)](#)
[![Tests: Passing](https://img.shields.io/badge/Tests-Passing-brightgreen.svg)](#)
[![Owner: mahmoudabdelnaby1](https://img.shields.io/badge/Owner-mahmoudabdelnaby1-blue.svg)](https://github.com/mahmoudabdelnaby1)

---

## 📌 Problem Statement & Target Persona

### Target Persona
**BOTH** operating in high-growth e-commerce, digital publishing, and direct-response marketing across Saudi Arabia, UAE, and Egypt.

### Core Problem
Develop a pure Python Arabic numeral and bidirectional text normalization CLI (`bidi_linter.py`): 1) Scans text and HTML files for mixed Western/Eastern numerals, 2) Automates one-click normalization to either system, 3) Detects phone numbers and currency strings that lack proper `<bdi>` or Unicode RLM/LRM isolation marks, 4) Outputs a clean terminal report and corrected text files.

---

## 🛠️ Repository Architecture & Deliverables

This repository provides self-contained, documented implementations and specifications:

- `docs/unicode-bidi-best-practices.md`
- `examples/scrambled_and_fixed_text.html`
- `LICENSE`
- `README.md`
- `src/bidi_linter.py`
- `tests/test_bidi.py`
- `tools/web_normalizer.html`


---

## 🚀 Quick Start & How to Run Locally

### Run Test Suite Locally
```bash
# Ensure no bytecode generation
export PYTHONDONTWRITEBYTECODE=1  # Linux / macOS
$env:PYTHONDONTWRITEBYTECODE="1"  # Windows PowerShell

# Run Python unittest discovery
python -m unittest discover -s tests
```

### Run CLI Script
```bash
python src/bidi_linter.py --help
```

### Interactive Browser Tool
Open `examples/scrambled_and_fixed_text.html` directly in your web browser (Chrome, Edge, Safari) to use the local interactive calculator or dashboard. Operates 100% client-side with zero external network calls.

---

## 📊 Sample Input & Output Fixtures

> **Data Disclosure:** Any included sample data is illustrative and may be synthetic; it is not a measured customer result or market benchmark unless a source and collection method are stated alongside it. These files run offline with standard libraries and require no paid third-party API credentials.

```json
{
  "domain": "localization",
  "repository": "arabic-number-bidi-normalization-linter",
  "status": "READY_FOR_LOCAL_REVIEW",
  "license": "MIT"
}
```

---

## ⚠️ Known Technical & Domain Constraints

- **Eastern Arabic (٠-٩) vs Western Arabic (0-9) Digits:** Enforces numeral consistency within regional markets (Saudi retail predominantly Western 0-9).
- **BiDi Formatting Characters:** Injects Unicode Left-to-Right Mark (&lrm; / U+200E) around telephone numbers and prices to prevent displaced currency symbols.
- **Mathematical Operator Placement:** Preserves proper visual ordering for percentages (e.g. 50%) and mathematical ranges within RTL sentences.

---

## 📚 Primary Documentation & Verifiable References

- [Unicode Consortium: Unicode Bidirectional Algorithm (UAX #9)](https://www.unicode.org/reports/tr9/) - Definitive specification for directional text rendering and BiDi control characters.
- [Unicode Technical Standard #35: Locale Data Markup Language (LDML)](https://www.unicode.org/reports/tr35/) - Standard formatting specifications for regional numbers, currencies, and dates.
- [W3C Internationalization: Structural Markup and RTL Text](https://www.w3.org/International/questions/qa-bidi-controls) - Practical guide on using directional markup and avoiding displaced punctuation.

---


## 👤 Maintainer & License

- **Author & Maintainer:** [Mahmoud Abdelnaby](https://github.com/mahmoudabdelnaby1) (`@mahmoudabdelnaby1`)
- **License:** [MIT License](LICENSE) - Open-source, auditable, and freely adaptable for internal enterprise or commercial use.
