from fastapi import FastAPI
import time
import redis
import os

app = FastAPI()

redis_client = redis.Redis(host="redis",port=6379,decode_responses=True)

@app.get("/heavy")
def heavy():
    cached = redis_client.get("heavy_response")
    if cached:  #cache hit
        return {"message":cached, "cached":True}
    #cache miss 
    time.sleep(0.2)  # simulate heavy DB call (200ms)
    response = "Heavy response"
    redis_client.set("heavy_response",response,ex=60)  #expire after 60 seconds
    return {"message": response, "cached": False}
    #caution: can cause Cache stampede