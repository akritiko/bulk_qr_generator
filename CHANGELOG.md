
# Changelog

All notable changes to this project will be documented in this file.

## [1.2.0] 
### Added
- Deployment packaging for Render platform (demo).
- Configuration updates and environment setup for seamless hosting and execution on Render.

## [1.1.0] 
### Changed
- Updated business logic to avoid hosting QR code images and ZIP files on the server.
- Files are now directly offered to users for download, improving privacy and server resource management.
- Enhanced file-handling workflows to support this feature.

## [1.0.0] 
### Added
- Initial release of the completed web application version, providing a Flask-based interface for single and bulk QR code generation.
- Commit includes features for single QR code creation, bulk generation from CSV files, and icon embedding.

## [0.9.1] 
### Fixed
- Replaced `werkzeug.urls.url_quote` with `urllib.parse.quote` for compatibility with Werkzeug 2.2+.

## [0.9.0] 
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