# Epic Games Manifest Updater - Project Structure

## 📁 Repository Overview

```
epic-manifest-updater/
├── 📄 EpicManifestUpdater.ps1     # Main PowerShell script
├── 🌐 index.html                  # GitHub Pages website
├── 📋 README.md                   # Project documentation
├── 📝 CONTRIBUTING.md             # Contribution guidelines
├── 📅 CHANGELOG.md                # Version history
├── ⚖️ LICENSE                      # MIT License
├── 🚫 .gitignore                  # Git exclusions
├── 🏷️ .nojekyll                   # GitHub Pages config
├── 📁 .github/                    # GitHub configuration
│   ├── 📁 workflows/              # GitHub Actions
│   │   ├── powershell-validation.yml
│   │   ├── create-release.yml
│   │   └── static.yml
│   └── 📁 ISSUE_TEMPLATE/         # Issue templates
│       ├── bug_report.md
│       ├── feature_request.md
│       └── support_request.md
├── 📁 docs/                       # Documentation
│   └── troubleshooting.md
├── 📁 examples/                   # Usage examples
│   └── usage-examples.md
└── 📁 tests/                      # PowerShell tests
    └── EpicManifestUpdater.Tests.ps1
```

## 🔧 Core Components

### Main Script (`EpicManifestUpdater.ps1`)
- **Purpose**: The primary PowerShell script that updates Epic Games manifest files
- **Features**:
  - GUI folder selection
  - Automatic Epic Games Launcher closure
  - Manifest file processing and updating
  - Color-coded console output
  - Error handling and validation

### Web Interface (`index.html`)
- **Purpose**: GitHub Pages website for project presentation and downloads
- **Features**:
  - Professional landing page
  - Download links and instructions
  - Feature overview and requirements
  - Responsive design for mobile/desktop

### Documentation
- **README.md**: Comprehensive project documentation
- **CONTRIBUTING.md**: Guidelines for contributors
- **CHANGELOG.md**: Version history and release notes
- **docs/troubleshooting.md**: Detailed troubleshooting guide

## 🤖 Automation & CI/CD

### GitHub Actions Workflows

#### PowerShell Validation (`powershell-validation.yml`)
- **Triggers**: Push to main/develop, PRs
- **Purpose**: Quality assurance for PowerShell code
- **Actions**:
  - PSScriptAnalyzer linting
  - Syntax validation
  - Security scanning
  - Pester test execution

#### Release Creation (`create-release.yml`)
- **Triggers**: Git tags, manual workflow dispatch
- **Purpose**: Automated release process
- **Actions**:
  - Script validation
  - Release notes generation from CHANGELOG
  - ZIP package creation
  - GitHub Release creation with assets

#### GitHub Pages (`static.yml`)
- **Triggers**: Push to main branch
- **Purpose**: Deploy website to GitHub Pages
- **Actions**:
  - Static site deployment

### Issue Templates
- **Bug Report**: Structured bug reporting with system info
- **Feature Request**: Comprehensive feature suggestion format
- **Support Request**: Help and question template

## 🧪 Testing Framework

### Pester Tests (`tests/EpicManifestUpdater.Tests.ps1`)
- **Script Validation**: Syntax and structure checks
- **Function Testing**: Individual function validation
- **Integration Tests**: End-to-end workflow simulation
- **Error Handling**: Edge case and error scenario testing

### Test Categories
1. **Script File Validation**
   - File existence and syntax
   - Required function presence
   - Assembly imports

2. **Manifest Processing**
   - JSON reading and writing
   - Path manipulation
   - Data integrity

3. **Error Scenarios**
   - Missing directories
   - Invalid JSON handling
   - Process management

4. **Integration Testing**
   - Multi-file processing
   - Complete workflow simulation
   - Validation procedures

## 📖 Documentation Structure

### User Documentation
- **README.md**: Primary user guide with features, installation, and usage
- **troubleshooting.md**: Comprehensive problem-solving guide
- **usage-examples.md**: Real-world scenarios and advanced usage

### Developer Documentation
- **CONTRIBUTING.md**: Development setup, coding standards, PR process
- **CHANGELOG.md**: Version tracking and release planning
- **Project Structure**: This file - technical overview

### Web Documentation
- **index.html**: User-friendly web interface with downloads and guides

## 🔒 Security & Quality

### Code Quality
- **PSScriptAnalyzer**: PowerShell best practices enforcement
- **Pester Testing**: Automated test coverage
- **Security Scanning**: Hardcoded credential detection
- **Input Validation**: Path and parameter sanitization

### Security Measures
- **No Credential Storage**: Script operates without storing sensitive data
- **Limited Scope**: Only modifies Epic Games manifest files
- **Permission Validation**: Checks for required access rights
- **Safe Operations**: Atomic updates with error recovery

## 🚀 Release Process

### Version Management
1. **Development**: Feature branches with PR validation
2. **Testing**: Automated quality checks on all changes
3. **Release**: Tag-based automated release creation
4. **Distribution**: GitHub Releases with multiple download formats

### Release Assets
- **Main Script**: `EpicManifestUpdater.ps1`
- **Complete Package**: ZIP with documentation and installation guide
- **Web Download**: Direct script download from GitHub Pages

## 🌐 GitHub Pages Integration

### Website Features
- **Landing Page**: Professional presentation of the tool
- **Download Section**: Direct links to latest releases
- **Documentation**: Embedded usage instructions
- **Support Links**: Easy access to issue reporting and discussions

### SEO & Accessibility
- **Meta Tags**: Proper metadata for search engines
- **Responsive Design**: Mobile and desktop compatibility
- **Fast Loading**: Optimized assets and minimal dependencies

## 🤝 Community Features

### Contribution Workflow
1. **Issue Creation**: Structured templates for different types of feedback
2. **Pull Requests**: Automated validation and review process
3. **Discussions**: GitHub Discussions for community questions
4. **Documentation**: Comprehensive guides for contributors

### Support Channels
- **GitHub Issues**: Bug reports and feature requests
- **GitHub Discussions**: Questions and community support
- **Documentation**: Self-service troubleshooting guides

## 📊 Project Metrics

### Quality Indicators
- **Test Coverage**: Comprehensive Pester test suite
- **Code Quality**: PSScriptAnalyzer compliance
- **Documentation**: Complete user and developer guides
- **Automation**: Full CI/CD pipeline

### Community Health
- **Issue Templates**: Structured feedback collection
- **Contributing Guidelines**: Clear contribution process
- **Code of Conduct**: Professional community standards
- **Security Policy**: Responsible disclosure guidelines

## 🔄 Maintenance & Updates

### Regular Maintenance
- **Dependency Updates**: PowerShell module compatibility
- **Documentation Reviews**: Keeping guides current
- **Test Updates**: Ensuring test coverage remains comprehensive
- **Security Audits**: Regular security best practice reviews

### Feature Development
- **Community Feedback**: Issue and discussion monitoring
- **Epic Games Compatibility**: Staying current with Epic Games Launcher changes
- **Performance Optimization**: Continuous improvement
- **User Experience**: Interface and workflow enhancements

This project structure ensures professional development practices, comprehensive documentation, automated quality assurance, and excellent user experience for the Epic Games Manifest Updater tool.
