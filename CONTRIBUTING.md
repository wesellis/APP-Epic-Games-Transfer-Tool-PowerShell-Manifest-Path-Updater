# Contributing to Epic Games Manifest Updater

Thank you for your interest in contributing to the Epic Games Manifest Updater! This project helps gamers avoid re-downloading their Epic Games library after moving installations, and your contributions make it better for everyone.

## 🌟 Ways to Contribute

### 🐛 **Bug Reports**
- Report issues with the script functionality
- Document compatibility problems with specific Windows versions
- Share edge cases or unexpected behavior

### 💡 **Feature Enhancements**
- Suggest new functionality or improvements
- Propose UI/UX enhancements
- Share ideas for automation features

### 📖 **Documentation**
- Improve setup instructions and troubleshooting guides
- Add usage examples for different scenarios
- Translate documentation to other languages

### 🧪 **Testing & Quality Assurance**
- Test on different Windows versions and configurations
- Validate with various Epic Games installations
- Help identify and reproduce bugs

### 💻 **Code Contributions**
- Fix bugs and implement new features
- Improve error handling and validation
- Optimize performance and reliability

## 🚀 Getting Started

### Prerequisites

- **Windows 10/11** with PowerShell 5.1+
- **Epic Games Launcher** installed for testing
- **Git** for version control
- **Visual Studio Code** with PowerShell extension (recommended)

### Development Setup

1. **Fork and clone the repository**
   ```powershell
   git clone https://github.com/YOUR-USERNAME/epic-manifest-updater.git
   cd epic-manifest-updater
   ```

2. **Install development tools**
   ```powershell
   # Install PowerShell modules for development
   Install-Module -Name Pester -Force -Scope CurrentUser
   Install-Module -Name PSScriptAnalyzer -Force -Scope CurrentUser
   Install-Module -Name platyPS -Force -Scope CurrentUser
   ```

3. **Create a test environment**
   ```powershell
   # Create test manifest directory (don't use production manifests!)
   $testDir = \"$env:TEMP\\EpicManifestTest\"
   New-Item -ItemType Directory -Path $testDir -Force
   ```

4. **Create a feature branch**
   ```powershell
   git checkout -b feature/your-feature-name
   ```

## 📝 Development Guidelines

### PowerShell Coding Standards

#### **Script Structure**
```powershell
<#
.SYNOPSIS
    Brief description of the script or function

.DESCRIPTION
    Detailed description of functionality and purpose

.PARAMETER ParameterName
    Description of parameter and expected values

.EXAMPLE
    PS> .\\EpicManifestUpdater.ps1
    Description of what this example demonstrates

.NOTES
    Author: Your Name
    Date: YYYY-MM-DD
    Version: X.X.X
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $false)]
    [string]$Parameter
)
```

#### **Coding Best Practices**

- **Use approved verbs** for function names (`Get-Verb` for reference)
- **Include proper error handling** with `try/catch/finally` blocks
- **Add input validation** using parameter attributes
- **Use meaningful variable names** (descriptive but concise)
- **Include progress indicators** for long-running operations
- **Add verbose output** for debugging (`Write-Verbose`)
- **Follow PowerShell conventions** (PascalCase for functions, camelCase for variables)

#### **Error Handling Standards**
```powershell
try {
    # Main logic here
    Write-Verbose \"Performing operation...\"
}
catch {
    Write-ColorOutput Red \"Error: $($_.Exception.Message)\"
    Write-Verbose \"Full error details: $($_.Exception)\"
    throw
}
finally {
    # Cleanup code
}
```

### Code Quality Requirements

#### **Mandatory Elements**
- **Comment-based help** with complete documentation
- **Parameter validation** for all inputs
- **Comprehensive error handling** with user-friendly messages
- **Verbose output** for troubleshooting
- **Input sanitization** for file paths and user data
- **Exit codes** for automation scenarios

#### **Security Guidelines**
- **No hardcoded paths** - use environment variables or detection
- **Validate all inputs** before processing
- **Handle permissions gracefully** - don't assume admin rights
- **Safe file operations** - use proper file locking and validation
- **No sensitive data logging** - avoid logging paths or user information

## 🧪 Testing Requirements

### Unit Testing with Pester

Create tests for all new functionality:

```powershell
Describe \"EpicManifestUpdater\" {
    BeforeAll {
        # Setup test environment
        $script:testManifestDir = \"$env:TEMP\\EpicManifestTest\"
        New-Item -ItemType Directory -Path $script:testManifestDir -Force
    }
    
    Context \"Manifest File Processing\" {
        It \"Should detect valid manifest files\" {
            # Test implementation
        }
        
        It \"Should update paths correctly\" {
            # Test implementation
        }
        
        It \"Should handle missing game folders gracefully\" {
            # Test implementation
        }
    }
    
    Context \"Error Handling\" {
        It \"Should fail gracefully with invalid paths\" {
            # Test implementation
        }
        
        It \"Should validate Epic Games installation\" {
            # Test implementation
        }
    }
    
    AfterAll {
        # Cleanup test environment
        Remove-Item -Path $script:testManifestDir -Recurse -Force -ErrorAction SilentlyContinue
    }
}
```

### Integration Testing

1. **Test with real manifests** (backup first!)
2. **Verify Epic Games detection** after script execution
3. **Test various folder structures** and path scenarios
4. **Validate on different Windows versions**

### Test Scenarios

| Scenario | Expected Result |
|----------|----------------|
| Valid game folder | Manifest updated, game detected |
| Missing game folder | Skip with warning message |
| Invalid manifest JSON | Skip with error message |
| No Epic Games installation | Exit with clear error |
| Permission denied | Graceful failure with guidance |

## 📋 Submission Process

### Before Submitting

1. **Run PowerShell Script Analyzer**
   ```powershell
   Invoke-ScriptAnalyzer -Path .\\EpicManifestUpdater.ps1 -Severity Error,Warning
   ```

2. **Execute all tests**
   ```powershell
   Invoke-Pester -Path .\\tests\\ -CodeCoverage .\\EpicManifestUpdater.ps1
   ```

3. **Test manually** with real Epic Games installation

4. **Update documentation** as needed

### Pull Request Guidelines

#### **PR Title Format**
- `feat: add support for multiple Epic installations`
- `fix: resolve manifest parsing error with special characters`
- `docs: improve troubleshooting guide`
- `test: add integration tests for path validation`

#### **PR Description Template**
```markdown
## Description
Brief description of changes and motivation

## Type of Change
- [ ] Bug fix (non-breaking change that fixes an issue)
- [ ] New feature (non-breaking change that adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update
- [ ] Performance improvement
- [ ] Code refactoring

## Testing Performed
- [ ] Tested with real Epic Games installation
- [ ] PowerShell Script Analyzer validation passed
- [ ] Pester tests pass
- [ ] Manual testing on Windows 10/11
- [ ] Tested edge cases and error conditions

## Screenshots (if applicable)
Add screenshots of console output or behavior changes

## Checklist
- [ ] Code follows project style guidelines
- [ ] Self-review of code completed
- [ ] Documentation updated (README, comments, help text)
- [ ] Tests added/updated for new functionality
- [ ] No breaking changes introduced
- [ ] Security considerations reviewed
```

## 🔍 Code Review Process

### What Reviewers Look For

- **Functionality** - Does the code work as intended?
- **Security** - Are there any security implications?
- **Performance** - Is the code efficient and responsive?
- **Maintainability** - Is the code easy to understand and modify?
- **Compatibility** - Does it work across different Windows versions?
- **User Experience** - Is the output clear and helpful?

### Review Timeline

- **Initial review** within 2-3 business days
- **Follow-up reviews** within 1-2 business days
- **Approval and merge** after all checks pass

## 🎯 Priority Areas

### High-Priority Improvements

- **Multi-installation support** - Handle multiple Epic Games installations
- **Backup functionality** - Create manifest backups before modification
- **Configuration file** - Allow user preferences and settings
- **GUI interface** - Windows Forms or WPF interface option
- **Logging system** - Comprehensive logging for troubleshooting

### Beginner-Friendly Tasks

- **Documentation improvements** - Fix typos, add examples
- **Error message enhancement** - Make messages more user-friendly
- **Code cleanup** - Improve formatting and comments
- **Test coverage** - Add more unit tests
- **Validation improvements** - Better input validation

## 📞 Getting Help

### Support Channels

- **💬 GitHub Discussions** - [Ask questions and discuss ideas](https://github.com/wesellis/epic-manifest-updater/discussions)
- **🐛 GitHub Issues** - [Report bugs or request features](https://github.com/wesellis/epic-manifest-updater/issues)
- **📧 Direct Contact** - Check repository for maintainer contact information

### Development Resources

- **[PowerShell Documentation](https://docs.microsoft.com/powershell/)** - Official PowerShell guides
- **[Pester Documentation](https://pester.dev/)** - Testing framework documentation
- **[PSScriptAnalyzer](https://github.com/PowerShell/PSScriptAnalyzer)** - Code analysis tool
- **[Epic Games API](https://dev.epicgames.com/)** - Epic Games developer documentation

## 🏆 Recognition

Contributors are recognized through:
- **README.md** acknowledgments section
- **Release notes** credit for contributions
- **Special recognition** for significant contributions
- **Collaborator access** for ongoing contributors

## 📜 Code of Conduct

This project follows the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). By participating, you agree to abide by its terms.

### Our Standards

- **Be respectful** and inclusive in all interactions
- **Provide constructive feedback** and suggestions
- **Focus on the project** and technical discussions
- **Help create a welcoming environment** for all contributors

## 🔒 Security Policy

### Reporting Security Issues

If you discover a security vulnerability, please:
1. **Do not** open a public issue
2. **Email** the maintainer directly (check repository for contact)
3. **Include** detailed information about the vulnerability
4. **Wait** for confirmation before public disclosure

### Security Guidelines

- **No credential exposure** - Never include passwords or API keys
- **Safe file operations** - Validate all file operations
- **Input sanitization** - Sanitize all user inputs
- **Principle of least privilege** - Request minimal necessary permissions

---

Thank you for contributing to Epic Games Manifest Updater! Your efforts help thousands of gamers save time and bandwidth. 🎮✨
