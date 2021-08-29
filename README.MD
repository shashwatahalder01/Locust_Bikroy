#   Locust Demo Bikroy.com



# Run command

#### With UI (http://localhost:8089/)
    $ locust -f  locust_files/filename.py
#### Without UI (headless)
    $ locust --headless --users 10 --spawn-rate 1 -H http://your-server.com
#### Using master.conf
    $ locust --config=master.conf

