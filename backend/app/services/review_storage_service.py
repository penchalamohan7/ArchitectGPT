import json
import os
from datetime import datetime

REVIEW_FOLDER = "storage/reviews"

os.makedirs(REVIEW_FOLDER, exist_ok=True)


def save_review(review):

    filename = datetime.now().strftime("%Y%m%d_%H%M%S")

    filepath = os.path.join(
        REVIEW_FOLDER,
        filename + ".json"
    )

    with open(filepath, "w") as f:

        json.dump(
            review,
            f,
            indent=4
        )

    return filepath


def load_reviews():

    reviews = []

    for file in os.listdir(REVIEW_FOLDER):

        with open(
            os.path.join(REVIEW_FOLDER, file),
            "r"
        ) as f:

            reviews.append(
                json.load(f)
            )

    return reviews