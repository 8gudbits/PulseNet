import argparse
import speedtest
import sys


class CustomHelpFormatter(argparse.HelpFormatter):
    def format_help(self):
        return (
            "\nPulseNet 1.1 (x64) : (c) 8gudbits - All rights reserved.\n"
            "Source - \"https://github.com/8gudbits/8gudbitsKit\"\n\n"
            "Usage: pulsenet [options]\n\n"
            "Options:\n"
            "  -h, --help      Show this help message and exit.\n"
            "  -u, --upload    Test upload speed only.\n"
            "  -d, --download  Test download speed only.\n"
            "  -n, --nobanner  Suppress the banner.\n"
        )


def test_network_speed(test_download=True, test_upload=True):
    """Test network speed and return the results."""
    try:
        st = speedtest.Speedtest()  # Initialize the Speedtest object
        st.get_best_server()  # Get the best server based on ping

        # Initialize results
        download_speed_mbps = None
        upload_speed_mbps = None

        # Perform the download speed test
        if test_download:
            download_speed = st.download()
            download_speed_mbps = download_speed / 1e6

        # Perform the upload speed test
        if test_upload:
            upload_speed = st.upload()
            upload_speed_mbps = upload_speed / 1e6

        return download_speed_mbps, upload_speed_mbps
    except speedtest.SpeedtestException as e:
        print(f"Speedtest failed: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    """Main function to execute the network speed test based on CLI arguments."""
    # Set up the argument parser with custom formatter
    parser = argparse.ArgumentParser(
        description="PulseNet 1.1 (x64) : (c) 8gudbits - All rights reserved.",
        formatter_class=CustomHelpFormatter,
        add_help=False  # Disable default help
    )
    
    parser.add_argument('-u', '--upload', action='store_true', help='Test upload speed only.')
    parser.add_argument('-d', '--download', action='store_true', help='Test download speed only.')
    parser.add_argument('-n', '--nobanner', action='store_true', help='Suppress the banner.')
    parser.add_argument('-h', '--help', action='store_true', help='Display help message.')

    # Parse the arguments
    args = parser.parse_args()

    if args.help:
        print(parser.format_help())  # Use the custom help formatter
        sys.exit(0)

    # Print the banner unless the --nobanner/-n flag is provided
    if not args.nobanner:
        print("\nPulseNet 1.1 (x64) : (c) 8gudbits - All rights reserved.")
        print("Source - \"https://github.com/8gudbits/8gudbitsKit\"")

    # If both upload and download are specified, or neither, test both
    test_both = args.upload and args.download or not (args.upload or args.download)

    # Run the network speed test
    download_speed, upload_speed = test_network_speed(test_download=test_both or args.download, test_upload=test_both or args.upload)

    # Print the results based on the arguments
    if test_both:
        print(f"\nDownload Speed: {download_speed:.2f} Mbps")
        print(f"Upload Speed: {upload_speed:.2f} Mbps")
    elif args.download:
        print(f"\nDownload Speed: {download_speed:.2f} Mbps")
    elif args.upload:
        print(f"\nUpload Speed: {upload_speed:.2f} Mbps")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nOperation aborted by user.")
        sys.exit(0)
