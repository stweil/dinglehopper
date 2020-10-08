from __future__ import division

import unicodedata
from typing import Tuple

from uniseg.graphemecluster import grapheme_clusters

from qurator.dinglehopper.edit_distance import distance
from qurator.dinglehopper.ocr_files import ExtractedText


def character_error_rate_n(reference, compared) -> Tuple[float, int]:
    """
    Compute character error rate.

    :return: character error rate and length of the reference
    """
    if isinstance(reference, str):
        return character_error_rate_n(
                ExtractedText.from_text(reference),
                compared)

    d = distance(reference, compared)
    n = len(list(grapheme_clusters(reference.text)))

    if d == 0:
        return 0, n
    if n == 0:
        return float('inf'), n
    return d/n, n

    # XXX Should we really count newlines here?


def character_error_rate(reference, compared) -> float:
    """
    Compute character error rate.

    :return: character error rate
    """
    cer, _ = character_error_rate_n(reference, compared)
    return cer
