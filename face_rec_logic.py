import io
import base64

import numpy as np
from PIL import Image
import face_recognition as fr


def decode_b64(json_name):
    """
    Конвертация json массивов из base64 в объекты bytesIO
    """
    return io.BytesIO(base64.b64decode(json_name['PhotoDB'])), io.BytesIO(
        base64.b64decode(json_name['PhotoReal']))


def to_numpy(array1, array2):
    """
    Конвертация объектов BytesIO в numpy массивы
    """
    return np.asarray(
        Image.open(array1).convert('RGB')
        ).astype('uint8'), np.asarray(
        Image.open(array2).convert('RGB')
        ).astype('uint8')


def decode_json(json_name):
    """
    Декодирование json
    """
    array1, array2 = decode_b64(json_name)
    return to_numpy(array1, array2)


def mini_api(file_name):
    """
    Передача массивов в face_recognition
    """
    first_photo, second_photo = decode_json(file_name)
    result = fr.compare_faces(  # face_recognition as fr
            [fr.face_encodings(first_photo)[0]],
            fr.face_encodings(second_photo)[0])[0]
    return result
