## Instructions
These instructions assume you're using Ubuntu LTS. Download the latest version of Docker with the [following guide](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04) and run these commands:
- `git clone https://github.com/rahmiere/docker-flask-demo.git`
- `nano docker-flask-demo/ngrok.yml` and replace the placeholders with the proper values
- `mkdir -p logs && touch logs/ngrok.log` 
- `docker compose build`
- `docker compose up`