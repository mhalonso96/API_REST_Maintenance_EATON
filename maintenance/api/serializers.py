from rest_framework.serializers import ModelSerializer
from maintenance.models import Maintenance

class MaintenanceSerializers(ModelSerializer):
    class Meta:
        model = Maintenance
        fields = ('id', 'company', 'departament', 'section', 'created_at', 'update_at', )