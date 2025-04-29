# sentryissue

The Sentry background thread deadlocks on 7th generation x86-64 EC2 instance types in the `us-east-1` region when running Django 1.11 on Gunicorn with Gevent workers on Python 3.6.

## 

1. Create an x86-64 Debian based EC2 instance in AWS `us-east-1` region using a `7i`, `7a`, or `7i-flex` type instance. The instance must be able to access the internet either via public IP address or NAT, and you need to be able to SSH into the instance.

2. SSH into the instance.

    ```
    ssh admin@<IPADDR>
    ```

3. Install git and pull the sentryissue repo down.

    ```
    sudo apt update \
    && sudo apt install --yes git \
    && git clone https://github.com/jonhuber/sentryissue.git
    ```

4. Run the sentryissue setup script. This installs Python 3.6.15, creates a virtualenv, and installs the project requirements.

    ```
    cd sentryissue && \
    ./setup.sh
    ```

5. Run the sentryissue server. This launches Gunicorn using a Gevent worker.

    ```
    SENTRY_DSN="https://host/path" ./runserver.sh
    ```

6. From another SSH terminal, run the sentryissue curl script a couple of times to send the Sentry client into a non-sending state. This makes requests and should produce a situation where Sentry isn't sending events.

    ```
    ./runcurl.sh
    ```
