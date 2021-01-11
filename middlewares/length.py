import argparse

def required_length(nmin,nmax):
    """
        Middleware allowing to parse between min and max numbers of value for argparse's parsers.
    """
    class RequiredLength(argparse.Action):
        """
            Class inheriting from argparse.Action to perform validation when parsing arguments.
            So it can be passed in the action property.
        """
        def __call__(self, parser, args, values, option_string=None):
            if not nmin<=len(values)<=nmax:
                errMsg='argument "{f}" requires between {nmin} and {nmax} arguments'.format(
                    f=self.dest,nmin=nmin,nmax=nmax)
                parser.error(errMsg)
            setattr(args, self.dest, values)
    return RequiredLength