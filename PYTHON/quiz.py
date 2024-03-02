from flask import jsonify
from app import app, db
from models import Review

@app.route("/reviews", methods=["GET"])
def get_reviews():
    reviews = Review.query.all()
    
    # Convert Review objects to dictionaries
    reviews_data = []
    for review in reviews:
        review_data = {
            "id": review.id,
            "user_id": review.user_id,
            "product_id": review.product_id,
            "rating": review.rating,
            "comment": review.comment,
            # Add other attributes as needed
        }
        reviews_data.append(review_data)
    
    return jsonify(reviews_data), 200
