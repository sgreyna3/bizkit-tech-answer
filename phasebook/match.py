import time
from flask import Blueprint

from .data.match_data import MATCHES


bp = Blueprint("match", __name__, url_prefix="/match")


@bp.route("<int:match_id>")
def match(match_id):
    if match_id < 0 or match_id >= len(MATCHES):
        return "Invalid match id", 404

    start = time.time()
    msg = "Match found" if (is_match(*MATCHES[match_id])) else "No match"
    end = time.time()

    return {"message": msg, "elapsedTime": end - start}, 200


def is_match(fave_numbers_1, fave_numbers_2):

    num_1_set = set(fave_numbers_1)
    num_2_set = set(fave_numbers_2)
    
    if num_1_set.issuperset(num_2_set):
        return True
    return False

    # We can also do that by doing this

    '''
    for number in num_2_set:
        if number not in num_1_set:
            return False

    return True
    '''
