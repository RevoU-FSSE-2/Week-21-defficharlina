from flask import Blueprint, request
import jwt, os
from user.models import User
from tweet.models import Tweet
from auth.utils import decode_jwt

user_blueprint = Blueprint("user", __name__)

@user_blueprint.route("", methods=["GET"])
def get_user_profile():
    authorization_header = request.headers.get('Authorization')
    token = authorization_header.split("Bearer ")[1] if "Bearer " in authorization_header else None
    payload = decode_jwt(token)
    print("Decoded Payload:", payload)
    if not payload:
        return {"error": "Token tidak valid"}, 401

    user_id = payload.get("user_id")

    if not user_id:
        return {"error": "User ID tidak ditemukan"}, 401

    user = User.query.get(user_id)

    if not user:
        return {"error": "User tidak ditemukan!"}, 404
    
    tweets = Tweet.query.filter_by(user_id=user_id).order_by(Tweet.published_at.desc()).limit(10).all()

    following_count = user.following.count()
    followers_count = user.followers.count()

    tweet_details = [
            {
                'id': tweet.id,
                'published_at': tweet.published_at,
                'tweet': tweet.tweet
            }
            for tweet in tweets
        ]
    
    return {
        'id': user.id,
        'username': user.username,
        'bio': user.bio,
        'tweet':tweet_details,
        'following_count': following_count,
        'followers_count': followers_count
    }
