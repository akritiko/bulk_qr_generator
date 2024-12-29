
# Changelog

All notable changes to this project will be documented in this file.

## [0.9.1] - Current
### Changed
- Replaced `werkzeug.urls.url_quote` with `urllib.parse.quote` for compatibility with Werkzeug 2.2+.

## [0.9.0] - Previous Release
### Added
- Web application interface using Flask for single and bulk QR code generation.
- Desktop application interface with Tkinter for GUI-based single and batch QR code creation.
- Command-line interface (CLI) for advanced and automated QR code generation.
- Support for embedding icons in QR codes.
- Bulk QR code generation from CSV files.
- High-resolution output with organized storage of QR codes.
- Success and error handling with feedback in GUI and web interfaces.

### Changed
- Initial version with modular design and multi-platform support.

### Fixed
- N/A
