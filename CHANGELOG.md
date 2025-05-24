# Changelog

All notable changes to Epic Games Manifest Updater will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Comprehensive project documentation and contribution guidelines
- GitHub Actions workflows for PowerShell linting and automated testing
- Issue templates for bug reports, feature requests, and general support
- Enhanced README with detailed usage examples and troubleshooting guide
- PowerShell Pester testing framework setup
- Code of conduct and security guidelines
- Professional project structure with docs, tests, and examples directories

### Changed
- Enhanced .gitignore with comprehensive PowerShell and Windows exclusions
- Restructured project with proper documentation hierarchy
- Updated LICENSE copyright year to 2025
- Improved script documentation with detailed parameter descriptions

### Security
- Added security guidelines for script development and usage
- Implemented secure coding standards for PowerShell scripts
- Enhanced input validation and error handling

### Documentation
- Added comprehensive troubleshooting section
- Included advanced usage examples and scenarios
- Created detailed development setup instructions
- Added project statistics and community information

## [1.2.0] - 2025-01-15

### Added
- Enhanced error handling for edge cases
- Improved validation of game folder structures
- Better console output with more detailed progress information
- Support for games with special characters in folder names

### Changed
- Optimized manifest file processing for better performance
- Improved user experience with clearer status messages
- Enhanced folder selection dialog with better descriptions

### Fixed
- Issue with manifest files containing unusual JSON formatting
- Problem with games installed in folders with spaces
- Rare case where Epic Games Launcher wouldn't close properly

### Security
- Added validation for manifest file integrity
- Improved path sanitization for security

## [1.1.0] - 2024-08-20

### Added
- GUI folder selection dialog for user-friendly operation
- Color-coded console output for better visual feedback
- Automatic Epic Games Launcher process termination
- Progress tracking and status updates during operation
- Support for games in subdirectories

### Changed
- Simplified user workflow - no more command line parameters needed
- Improved error messages with actionable guidance
- Better handling of missing or corrupted manifest files

### Fixed
- Issue with manifest files not being detected in some installations
- Problem with paths containing backslashes being incorrectly processed
- Rare issue with JSON parsing of manifest files

## [1.0.0] - 2024-03-15

### Added
- Initial release of Epic Games Manifest Updater
- Core functionality to update Epic Games manifest files
- Support for moving Epic Games installations to new locations
- Basic error handling and user feedback
- MIT license for open source distribution

### Features
- Automatic detection of Epic Games manifest directory
- Batch processing of all manifest files
- JSON parsing and updating of game installation paths
- Console-based user interface with basic feedback
- Validation of game folder existence before updating

### Requirements
- Windows 10/11 compatibility
- PowerShell 5.1 or newer
- Epic Games Launcher installation
- User permissions for manifest directory access

---

## Release Notes

### Version 1.2.0 Highlights
- **Enhanced Error Handling**: Better recovery from unexpected situations
- **Performance Improvements**: Faster processing of large game libraries
- **User Experience**: Clearer feedback and progress indication
- **Compatibility**: Support for more game installation scenarios

### Version 1.1.0 Highlights
- **GUI Introduction**: User-friendly folder selection dialog
- **Visual Feedback**: Color-coded console output for better UX
- **Automation**: Automatic launcher process management
- **Reliability**: Improved error handling and edge case support

### Version 1.0.0 Features
- **Core Functionality**: Basic manifest updating capability
- **Cross-Game Support**: Works with all Epic Games titles
- **Safe Operation**: Only modifies manifest files, not game data
- **Open Source**: MIT licensed for community use and modification

## Upcoming Features

### Version 1.3.0 (Planned)
- **Backup System**: Automatic manifest backup before modifications
- **Multi-Installation Support**: Handle multiple Epic Games installations
- **Configuration File**: User preferences and settings persistence
- **Enhanced Logging**: Detailed operation logs for troubleshooting
- **Rollback Capability**: Ability to undo manifest changes

### Version 2.0.0 (Future)
- **GUI Application**: Full Windows Forms or WPF interface
- **Scheduled Operations**: Automated manifest maintenance
- **Cloud Integration**: Backup manifests to cloud storage
- **Advanced Features**: Game library analysis and optimization
- **Plugin System**: Extensible architecture for custom functionality

## Migration Guide

### From 1.0.x to 1.1.x
- **No breaking changes** - all existing functionality preserved
- **New GUI features** - folder selection now uses dialog instead of manual path entry
- **Enhanced output** - color coding provides better visual feedback

### From 1.1.x to 1.2.x
- **No breaking changes** - fully backward compatible
- **Improved reliability** - better handling of edge cases
- **Performance gains** - faster processing for large game libraries

## Support and Compatibility

### Supported Platforms
- **Windows 10** (Version 1809 and later)
- **Windows 11** (All versions)
- **Windows Server 2019/2022** (Limited testing)

### Epic Games Launcher Versions
- **All current versions** supported
- **Legacy versions** back to 2020 releases
- **Beta/Preview** versions supported (best effort)

### PowerShell Compatibility
- **PowerShell 5.1** - Full support (Windows built-in)
- **PowerShell 7.x** - Full support and recommended
- **PowerShell Core 6.x** - Supported but not recommended

## Known Issues

### Current Limitations
- **Single Installation**: Only supports one Epic Games installation per system
- **Manual Process**: Requires manual execution (no automation)
- **Limited Backup**: No built-in manifest backup functionality
- **Windows Only**: No support for other operating systems

### Workarounds
- **Multiple Installations**: Run script separately for each installation
- **Automation**: Use Windows Task Scheduler for automated execution
- **Backup**: Manually backup manifest directory before running
- **Cross-Platform**: Use platform-specific alternatives for Mac/Linux

## Contributing

For information about contributing to this project, please see our [Contributing Guidelines](CONTRIBUTING.md).

## Support

If you encounter issues or have questions:
- Check the [troubleshooting guide](README.md#-troubleshooting) in the README
- Search [existing issues](https://github.com/wesellis/epic-manifest-updater/issues)
- Create a [new issue](https://github.com/wesellis/epic-manifest-updater/issues/new/choose) using our templates
- Start a [discussion](https://github.com/wesellis/epic-manifest-updater/discussions) for questions

## Acknowledgments

- **Epic Games** - For creating an excellent gaming platform
- **PowerShell Community** - For tools, guidance, and best practices
- **Gaming Community** - For feedback, testing, and feature requests
- **Contributors** - For bug reports, suggestions, and code contributions
- **Open Source Community** - For inspiration and collaborative development
