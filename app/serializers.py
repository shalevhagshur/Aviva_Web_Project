from rest_framework import serializers
from .models import Appointment

# Create your serializers here.

class AppointmentSerializer(serializers.ModelSerializer):
    '''
    Moshe L. 14/11/2023 13:37
    '''
    class Meta:
        model = Appointment
        fields = ['id', 'date', 'start_time', 'end_time', 'available']

    def validate(self, data):
        # Validate the start_time and end_time to ensure end_time is greater than start_time.
        start_time = data.get('start_time')
        end_time = data.get('end_time')

        if start_time and end_time and end_time <= start_time:
            raise serializers.ValidationError("End time must be greater than start time.")

        return data
