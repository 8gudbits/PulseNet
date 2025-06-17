# PulseNet

PulseNet is a simple command-line tool for testing internet speed. It measures peak speed of both **download** and **upload** using the Speedtest.net API and provides results in Mbps.

## Usage

```bash
Usage: pulsenet [options]
```

### Options

- `-u, --upload`    Test upload speed only.  
- `-d, --download`  Test download speed only.  
- `-n, --nobanner`  Suppress the banner output.  
- `-h, --help`      Display this help message.

## Download exe for Windows

This tool is part of the [8gudbitsKit](https://github.com/8gudbits/8gudbitsKit) project. To download the executable for Windows, visit the [8gudbitsKit](https://github.com/8gudbits/8gudbitsKit) repository.

## For the Tech People

- Uses **Speedtest.net API** via the `speedtest` Python module.  
- Finds the **best server** based on ping before testing.  
- Measures **download speed** using `st.download()`.  
- Measures **upload speed** using `st.upload()`.  
- Implements a **custom help formatter** for cleaner CLI output.  
- Handles **CLI arguments** using `argparse`.  
