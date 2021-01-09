
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
    print(sys.path)
    print('0000')
    from crowd_count import crowd_count
    print('1111')

    return crowd_count(image_path)
