from rest_framework.viewsets import ModelViewSet
from maintenance.api.serializers import MaintenanceSerializers
from maintenance.models import Maintenance

class MaintenanceViewsets(ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = MaintenanceSerializers
    queryset = Maintenance.objects.all()