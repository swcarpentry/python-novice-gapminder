#!/usr/bin/env python

import sys
import os
import glob
from optparse import OptionParser

from util import Reporter, read_markdown


def main():
    """Main driver."""

    args = parse_args()
    images = []
    for filename in get_filenames(args.source_dir):
        images += get_images(args.parser, filename)
    save(sys.stdout, images)


def parse_args():
    """Parse command-line arguments."""

    parser = OptionParser()
    parser.add_option('-p', '--parser',
                      default=None,
                      dest='parser',
                      help='path to Markdown parser')
    parser.add_option('-s', '--source',
                      default=None,
                      dest='source_dir',
                      help='source directory')

    args, extras = parser.parse_args()
    require(args.parser is not None,
            'Path to Markdown parser not provided')
    require(args.source_dir is not None,
            'Source directory not provided')
    require(not extras,
            'Unexpected trailing command-line arguments "{0}"'.format(extras))

    return args


def get_filenames(source_dir):
    """Get all filenames to be searched for images."""

    return glob.glob(os.path.join(source_dir, '*.md'))


def get_images(parser, filename):
    """Extract all images from file."""

    content = read_markdown(parser, filename)
    result = []
    find_image_nodes(content['doc'], result)
    return result


def find_image_nodes(doc, result):
    """Find all nested nodes representing images."""

    if (doc["type"] == "img") or \
       ((doc["type"] == "html_element") and (doc["value"] == "img")):
        result.append({'alt': doc['attr']['alt'], 'src': doc['attr']['src']})
    else:
        for child in doc.get("children", []):
            find_image_nodes(child, result)


def save(stream, images):
    """Save results as Markdown."""

    text = '\n<hr/>\n'.join(['<p><img alt="{0}" src="{1}" /></p>'.format(img['alt'], img['src']) for img in images])
    print(text, file=stream)


def require(condition, message):
    """Fail if condition not met."""

    if not condition:
        print(message, file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
