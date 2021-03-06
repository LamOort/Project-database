from .models import Course, Curriculum, Degreeprogram, Implementation, Person, PersonDegreeprogram, PersonImplementation, Room, RoomImplementation, Subgroup, SubgroupImplementation
from rest_framework import serializers

class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ('url', 'code', 'name', 'changes', 'languages', 'credit', 'size', 'p1', 'p2', 'p3', 'p4', 'p5', 'total', 'curriculumid')

class CurriculumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Curriculum
        fields = ('url', 'name', 'degreeprogramid')
		
class DegreeprogramSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Degreeprogram
        fields = ('url', 'name', 'code')		
		
class ImplementationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Implementation
        fields = ('url', 'courseid')		
		
class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ('url', 'code',  'name')		
		
class PersonDegreeprogramSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PersonDegreeprogram
        fields = ('url', 'personid',  'degreeprogramid')		
		
class PersonImplementationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PersonImplementation
        fields = ('url', 'personid', 'implementationid')		
		
class RoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Room
        fields = ('url', 'topic',  'code', 'seats')	

class RoomImplementationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RoomImplementation
        fields = ('url', 'roomid', 'implementationid')	

class SubgroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subgroup
        fields = ('url', 'code',  'department', 'groupid')	

class SubgroupImplementationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SubgroupImplementation
        fields = ('url', 'subgroupid', 'implementationid')			