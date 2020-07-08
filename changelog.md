# NorthState Change Log
## Add non-root user to run Docker:
- If docker group does not exist: `sudo groupadd docker`
- Add user to docker group: `sudo usermod -aG docker username`
- Apply new group changes: `newgrp docker`
- Test changes: `docker version; docker run hello-world`

## Update Company Logo
Default logo is located in `/ghostwriter/static/images` and is titled `domain.png`. Updating the default SpecterOps image with your company logo will change the image on the side-bar bottom.

## Changing Findings Fields
### Models (Database)
Updating the models updates the backend database. The findings model can be edited by making changes to `models.py` in the `/ghostwriter/reporting` directory. Each class essentially gets built as a table, with all the variables essentially representing database fields in the table ([Django Reference](https://docs.djangoproject.com/en/3.0/intro/tutorial02/)). When a field is updated, the following commands need to be run in order to migrate the model changes:
```sh
docker-compose -f local.yml run --rm django python manage.py makemigrations
docker-compose -f local.yml run --rm django python manage.py migrate
```
__Be sure to understand and properly alter all model links when preparing to make migrations__
Fields edited:
- `finding_guidance` changed to `additional_guidance` in the `Finding` and `ReportFindingLink` classes.
- `description` changed to `details`
- `mitigation` changed to `recommendation`
- `source` added
- `tools` added
- `impact` changed to `risk_determination`
- `replication_steps` removed
- `host_detection_techniques` removed
- `network_detection_techniques` removed

### Backend
Certain backend scripts are used to process front-end request variables and create labels for HTML rendering. For altering findings fields, these files are located in `/ghostwriter/reporting`. The following changes were made:
- `forms.py`: 
  - `finding_guidance` changed to `additional_guidance`.
  - `description` changed to `details`
  - `impact` changed to `risk_determination`
  - `mitigation` changed to `recommendation`
  - `source` added
  - `tools` added`
  - `replication_steps` removed
  - `host_detection_techniques` removed
  - `network_detection_techniques` removed
- `admin.py` FindingAdmin class:
  - `description` changed to `details`
  - `impact` changed to `risk_determination`
  - `mitigation` changed to `recommendation`
  - `source` added
  - `tools` added`
  - `replication_steps` removed
  - `host_detection_techniques` removed
  - `network_detection_techniques` removed
- `views.py` assign_blank_finding function:
- `views.py` assign_finding function:
- `/migrations/0005_reportfindinglink_finding_guidance.py`: `finding_guidance` changed to `additional_guidance`

### HTML
The HTML templates need to be altered in order to properly reflect back-end changes. These files are located in `/ghostwriter/reporting/templates/reporting`. The following changes were made:
- `finding_form.html`: 
  - `Defender Section` was commented out as none of those fields will be used in our report.
  - `{{ form.finding_guidance.label }}` and `{{ form.finding_guidance }}` altered to reflect `additional_guidance` changes.

