# Project Documentation: BaiduNetdisk Detector

This project aims to detect the installation of **BaiduNetdisk** (a cloud storage service) on Windows operating systems, check for executable files and folders related to the application, and generate a log file with the findings. Additionally, this documentation also explains the functionality for removing accents from text in the generated log.

## Project Structure

The main script performs the following actions:

1. **Installation Detection**: Checks common directories where BaiduNetdisk might be installed.
2. **Executable Check**: Looks for the main application executable in the found directories.
3. **Additional Folder Check**: Verifies the presence of configuration, cache, log, and resource folders associated with BaiduNetdisk.
4. **Accent Removal**: Normalizes and removes accents from all text entries in the generated log.
5. **Log Generation**: Generates a log file in the `C:\Windows\Temp\` directory with the gathered information.

## Features

### 1. Function `remove_accents(text)`
Removes accents and special characters from a given text. Uses Unicode normalization to remove accented characters.

**Parameters**:
- `text` (str): Input text that may contain accents.

**Returns**:
- The text with accents removed.

### 2. Function `detect_baidunetdisk()`
Detects if BaiduNetdisk is installed on the system and checks for executables and folders related to the application.

**Performed Tasks**:
- Checks for common installation folders of BaiduNetdisk.
- Looks for the main BaiduNetdisk executables.
- Checks for the existence of configuration, cache, log, and resource folders.
- Saves a log file with the results.

**Steps**:
1. Checks for the presence of common directory paths.
2. Searches for executables like `BaiduNetdisk.exe` or `BaiduNetdiskApp.exe`.
3. Checks for other related folders (Config, Cache, Logs, Resources).
4. If found, generates a log file in the `C:\Windows\Temp\` directory with a description of the findings.
5. If log saving fails, an error message is displayed.

## Dependencies

The script uses the following libraries:
- `os`: For file and path manipulation on the system.
- `unicodedata`: For accent removal from characters.

## How to Run

To run the script, follow the steps below:

1. Clone or download the project repository.
2. Make sure you have a configured Python environment.
3. Run the script in a terminal or command prompt:

```bash
python baidunetdisk_detector.py
```

After execution, a log file will be generated in `C:\Windows\Temp\Baidu_Detector.txt` with the findings related to the BaiduNetdisk installation.

## Example Log Output

The generated file may contain information such as:

```
Folder found: C:\Program Files\BaiduNetdisk
Executable found: C:\Program Files\BaiduNetdisk\BaiduNetdisk.exe
Configuration folder found: C:\Program Files\BaiduNetdisk\Config
Cache folder found: C:\Program Files\BaiduNetdisk\Cache
Logs folder found: C:\Program Files\BaiduNetdisk\Logs
Resources folder found: C:\Program Files\BaiduNetdisk\Resources
```

If BaiduNetdisk is not found, the log will be empty or contain only a failure message.

## Error Handling

If an error occurs during execution, such as failure to save the log or access folders, the following message will be shown in the console:

```
Error saving log: [Error message]
```

## Conclusion

This script is useful for detecting BaiduNetdisk installations on a Windows system and checking for the presence of its associated files and folders. It simplifies system administration, especially when checking for specific applications without the need for a graphical interface.
