from import_export import resources
from import_export.fields import Field
from .models import Finding


class FindingResource(resources.ModelResource):
    severity = Field(attribute='severity__severity', column_name='severity')
    finding_type = Field(attribute='finding_type__finding_type', column_name='finding_type')

    class Meta:
        model = Finding
        skip_unchanged = True
        fields = (
            'id', 'title', 'details', 'risk_determination',
            'recommendation', 'source', 'tools',
            'references', 'additional_guidance'
            )
        export_order = (
            'id', 'severity', 'finding_type', 'title', 'details',
            'risk_determination', 'source', 'tools',
            'references', 'additional_guidance'
            )
