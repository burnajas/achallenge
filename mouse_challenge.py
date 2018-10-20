class Mouse(object):
    """Contains methods for Mouse challenge"""
    def gen_mouse(self, fn=None):
        """Takes the filename containing the list of mouse descriptions and determines which type of mouse
        is being described
        """
        if fn is None:
            # Check file exists
            raise Exception('File required')
        row_idx = 0  # Keep track of where we are
        with open(fn) as median_file:
            rows = (x.rstrip('\n') for x in median_file.readlines())  # Strip out return and convert string into number
            for row in rows:
                if not row_idx:
                    row_idx += 1  # First row
                else:
                    # Run check algorithm and return results
                    yield self._determine_mouse(row)

    def _determine_mouse(self, description):
        """Determine if the description is of a animal or a computer-mouse
        Build a list of characteristics that can only be associated to each type of mouse.
        Test to see if those characteristics appear in the description argument.
        """
        lst_animal_characteristics = ['genome', 'postnatal', 'tail', 'legs', 'fur', 'feed', 'smell', 'climbing',
                                      'running', 'run', 'ears', 'nose', 'snout', 'rodent', 'rat']
        lst_computer_characteristics = ['input', 'device', 'computer', 'optical', 'ball', 'ergonomic',
                                        'ergonomics', 'cable', 'tablet', 'phone', 'laptop', 'keyboard', 'construction']
        # Split description down into a list
        lst_description = [w.lower().rstrip('.,?!:;') for w in description.split(' ')]  # lower case the words
        #
        if len(set(lst_animal_characteristics).intersection(set(lst_description))):
            return 'animal'
        if len(set(lst_computer_characteristics).intersection(set(lst_description))):
            return 'computer-mouse'
        # Unable to determine type from this method. Look for description patterns that may match.
        lst_animal_descriptions = []
        if [a for a in lst_animal_descriptions if a in description]:
            return 'animal'
        lst_computer_descriptions = ['flat surface', 'using a mouse', 'elbow level']
        if [a for a in lst_computer_descriptions if a in description]:
            return 'computer-mouse'
        raise Exception('Unable to determine mouse type: {}'.format(description), 404)
