class Median(object):
    """Contains methods for Running Median challenge"""
    def gen_median(self, fn=None):
        """Takes the filename containing the list of numbers a provides a returning the current """
        if fn is None:
            # Check file exists
            raise Exception('File required')
        row_idx = 0  # Keep track of where we are
        first_number = 0
        with open(fn) as median_file:
            rows = (float(x.rstrip('\n')) for x in median_file.readlines())  # Strip out return and convert string into number
            for row in rows:
                if not row_idx:
                    row_idx += 1  # First row
                else:
                    if row_idx == 1:
                        first_number = row  # Store first value
                        row_idx += 1
                        yield row
                    else:
                        row_idx += 1
                        yield first_number+((row - first_number)/2)  # Calculate mid point?
