# website_traffic_simulator
Made a small load balancing simulation for System Design learning purpose

Details : used components ->
FastAPI for backend 
Nginx for Reversed Proxy 
Redis for caching
Docker compose for container orchestration
Locust for load testing and monitoring 

Phase1: Created simple fastapi server and hit it with 1000 requests using locust. Over the time, request increases
and response time increases as well

Phase2: Added nginx for reverse proxy. Created 3 instances of app (3 servers , same config) running in container. Requests hit nginx first, and then nginx, using Round Robin by default, sent the traffic to 3 servers respectively, drastically dropping the response time (latency).

Phase3: Added Redis, for in memory caching. For the first hit, its a cache miss as redis does not have the data, so it
fetches the data and after that, redis is able to response super fast. Response time dropped even faster. 

overall latency reduced from 200 ms to 10 ms

Note: Can cause cache stampede. In the main.py file, the redis cache has holds the data for 60 seconds, after that 
the data is gone, and if 1000 users request at that time, all faces cache miss, and has to wait 0.2 seconds latency. This can crash database. Should find a way to solve this problem in future.

