# aac

## About
This Python package will create a .bat script file in C:\ffmpeg\bin which you can use to batch convert a folder of audio files to AAC format (.m4a) 256kbps.

## Usage
NOTE: the package only works with AAC format, and the target folder should only have audio files with no other files or directories.

Import the package, and use the encode.mkScript function with a string containing the absolute path to a target folder with your audio files.

```
import aac

aac.encode.mkScript("C:\\absolute\\path\\to\\folder")
```

A .bat file will be deposited in C:\ffmpeg\bin. The ffmpeg installation needs to be at that directory for this package to work. Double-click or run the .bat file with cmd or powershell to execute the ffmpeg batch conversion.

