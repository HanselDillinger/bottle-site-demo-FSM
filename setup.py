import sys

try:
    import my_site
except ImportError:
    raise ImportError('Couldn\'t import "my_site.py"')


if __name__ == '__main__':
    try:
        my_site.main(sys.argv[1], sys.argv[2])
    except IndexError:
        my_site.main()
