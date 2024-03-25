"""IBW -> ASCII conversion"""
import pprint

import numpy

from ..binarywave import load

from .script import Script


class WaveScript(Script):
    def _run(self, args):
        wave = load(args.infile)
        numpy.savetxt(args.outfile, wave["wave"]["wData"],
                      fmt="%g", delimiter="\t")
        self.plot_wave(args, wave)
        if args.verbose > 0:
            wave["wave"].pop("wData")
            pprint.pprint(wave)


def main():
    s = WaveScript(description=__doc__)
    s.run()


if __name__ == "__main__":
    main()
