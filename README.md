# 🎨 Color Selector Pro

A modern Python GUI application for selecting and managing multiple colors with advanced features.

## Features

### ✨ Core Functionality
- **Multiple Color Selection**: Select up to 20 colors at once
- **Random Color Generation**: Generate random colors with one click
- **Color Picker Integration**: Use system color picker for precise selection
- **Visual Color Display**: See all selected colors in a beautiful grid layout

### 🎯 Advanced Features
- **Configurable Limit**: Set how many colors you want to select (1-20)
- **Fill Random**: Instantly fill all slots with random colors
- **Color History**: Keep track of previously used colors
- **Export/Import**: Save and load color palettes as JSON or text files
- **Modern UI**: Clean, intuitive interface with emojis and modern styling

### 🚀 Quick Actions
- **➕ Add Color**: Open color picker to select a specific color
- **🎲 Random Color**: Add one random color
- **🎯 Fill Random**: Fill all available slots with random colors
- **🗑️ Clear All**: Remove all selected colors
- **💾 Export Colors**: Save your color palette
- **📁 Import Colors**: Load previously saved palettes

## Installation

1. **Clone or download** this repository
2. **Ensure Python 3.6+** is installed on your system
3. **No additional packages required** - uses only built-in Python libraries

## Usage

### Running the Application
```bash
python color_selector_app.py
```

### Basic Workflow
1. **Set Color Limit**: Use the spinbox to choose how many colors you want (1-20)
2. **Add Colors**: 
   - Click "➕ Add Color" to use the color picker
   - Click "🎲 Random Color" for a random color
   - Click "🎯 Fill Random" to fill all slots with random colors
3. **Manage Colors**: View all colors in the visual display area
4. **Use History**: Double-click any color in the history to reuse it
5. **Export/Import**: Save your palettes for later use

### Keyboard Shortcuts
- **Double-click** on history items to reuse colors
- **Scroll** through the color display area if you have many colors

## File Formats

### Export Options
- **JSON**: Complete data including colors, settings, and history
- **TXT**: Simple text format with color hex codes

### Import Options
- **JSON**: Full restoration of colors, settings, and history
- **TXT**: Import color hex codes from text files

## Technical Details

### Built With
- **Python 3.6+**
- **tkinter** (GUI framework)
- **json** (data persistence)
- **random** (color generation)

### Data Storage
- Color history is automatically saved to `color_history.json`
- Export files are saved in your chosen location
- No database required - everything is file-based

## Screenshots

The application features:
- Clean, modern interface with emoji icons
- Visual color grid display
- Scrollable color history
- Professional color picker integration
- Export/import functionality

## Customization

### Color Limits
- Minimum: 1 color
- Maximum: 20 colors
- Adjustable via the spinbox control

### History Management
- Automatically saves last 50 colors
- Persistent across application restarts
- Clear history option available

## Troubleshooting

### Common Issues
1. **Colors not displaying**: Ensure you have selected at least one color
2. **Import not working**: Check that the file format matches (JSON or TXT)
3. **History not saving**: Ensure write permissions in the application directory

### System Requirements
- **Operating System**: Windows, macOS, or Linux
- **Python Version**: 3.6 or higher
- **Memory**: Minimal requirements (uses built-in libraries only)

## License

This project is open source and available under the MIT License.

## Contributing

Feel free to submit issues, feature requests, or pull requests to improve the application!

---

**Enjoy creating beautiful color palettes! 🎨✨**