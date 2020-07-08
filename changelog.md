# NorthState Change Log
## Add non-root user to run Docker:
- If docker group does not exist: `sudo groupadd docker`
- Add user to docker group: `sudo usermod -aG docker username`
- Apply new group changes: `newgrp docker`
- Test changes: `docker version; docker run hello-world`

## Update Company Logo
Default logo is located in `/ghostwriter/static/images` and is titled `domain.png`. Updating the default SpecterOps image with your company logo will change the image on the side-bar bottom.

## Changing Findings Fields
### HTML

### Models

