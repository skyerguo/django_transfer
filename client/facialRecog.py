def facial_recognition(image_path):
    """
    Parameters
    ----------
    image : The input image file.

    Returns
    -------
    result : int
        The processing result.
    """
    
    import face_recognition
    from PIL import Image
    import os
    import time 

    image = face_recognition.load_image_file(image_path, mode='L')

    start_time = int(time.time())
    res = len(face_recognition.face_locations(image, number_of_times_to_upsample=4, model='hog'))
    end_time = int(time.time())
    time_cost = end_time - start_time
    print("face_locations cost time: ", time_cost)

    return res
