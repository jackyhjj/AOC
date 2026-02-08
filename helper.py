def read_input_file(input_file, remove_space=True):
    """
    Read file and return as list of lines.
    
    Args:
        input_file: Path to the input file
        remove_space: If True, removes all spaces and strips lines
    
    Returns:
        List of lines from the file
    """
    input_list = []
    with open(input_file) as f:
        for line in f:
            if remove_space:
                line = line.strip()
                line = line.replace(" ", "")
            else:
                line = line.strip()
                
            if len(line) > 0:
                input_list.append(line)
    return input_list


def read_lines(input_file, strip=True):
    """
    Read file and return as list of lines.
    
    Args:
        input_file: Path to the input file
        strip: If True, strips whitespace from each line
    
    Returns:
        List of lines from the file
    """
    with open(input_file) as f:
        if strip:
            return [line.strip() for line in f]
        return [line for line in f]


def read_lines_no_empty(input_file, strip=True):
    """
    Read file and return as list of lines, excluding empty lines.
    
    Args:
        input_file: Path to the input file
        strip: If True, strips whitespace from each line
    
    Returns:
        List of non-empty lines from the file
    """
    with open(input_file) as f:
        if strip:
            return [line.strip() for line in f if line.strip()]
        return [line for line in f if line]


def read_as_string(input_file):
    """
    Read entire file as a single string.
    
    Args:
        input_file: Path to the input file
    
    Returns:
        File contents as a string
    """
    with open(input_file) as f:
        return f.read()


def read_as_integers(input_file):
    """
    Read file and return as list of integers (one per line).
    
    Args:
        input_file: Path to the input file
    
    Returns:
        List of integers from the file
    """
    with open(input_file) as f:
        return [int(line.strip()) for line in f if line.strip()]


def read_grid(input_file):
    """
    Read file and return as 2D grid (list of lists of characters).
    
    Args:
        input_file: Path to the input file
    
    Returns:
        2D list representing the grid
    """
    with open(input_file) as f:
        return [list(line.strip()) for line in f if line.strip()]