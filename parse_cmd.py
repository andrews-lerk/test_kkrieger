import argparse


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('input', nargs='?')
    parser.add_argument('-o', '--output')
    return parser


def getCmdArgs():
    parser = createParser()
    namespace = parser.parse_args()
    return {'input': namespace.input, 'output': namespace.output}
