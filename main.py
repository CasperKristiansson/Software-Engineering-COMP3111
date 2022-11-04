import library.process
import library.output
import library.input


def main():
    p = library.process.Process()
    o = library.output.Output()
    i = library.input.Input()

    print(p, o, i)


if __name__ == "__main__":
    main()
