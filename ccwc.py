import argparse
import sys


def main():
    parser = argparse.ArgumentParser(description="ccwc - word/line/byte/char count")
    parser.add_argument("file", nargs="?", help="file to process")
    parser.add_argument("-c", "--byte", action="store_true", help="print byte count")
    parser.add_argument("-l", "--line", action="store_true", help="print line count")
    parser.add_argument("-w", "--word", action="store_true", help="print word count")
    parser.add_argument(
        "-m", "--char", action="store_true", help="print character count"
    )

    args = parser.parse_args()

    if args.file is None:
        data = sys.stdin.buffer.read()
        filename = ""
    else:
        with open(args.file, "rb") as f:
            data = f.read()
        filename = f" {args.file}"

    no_flags = not (args.byte or args.line or args.word or args.char)

    if no_flags:
        lines = data.count(b"\n")
        words = len(data.split())
        size = len(data)
        print(f"{lines} {words} {size}{filename}")
        return

    if args.byte:
        size = len(data)
        print(f"{size}{filename}")

    if args.line:
        lines = data.count(b"\n")
        print(f"{lines}{filename}")

    if args.word:
        words = len(data.split())
        print(f"{words}{filename}")

    if args.char:
        text = data.decode("utf-8", errors="replace")
        chars = len(text)
        print(f"{chars}{filename}")


if __name__ == "__main__":
    main()
