
def crowd_cnt(image_path):
    """
    Parameters
    ----------
    image : The input image file.

    Returns
    -------
    result : int
        The processing result.
    """
    
    import sys
    sys.path.append('/home/myzhou/lsc-cnn-master')
    from crowd_count import crowd_count

    return crowd_count(image_path)
