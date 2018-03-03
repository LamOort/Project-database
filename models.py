# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Course(models.Model):
    code = models.CharField(db_column='Code', max_length=50, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    changes = models.CharField(db_column='Changes', max_length=50, blank=True, null=True)  # Field name made lowercase.
    languages = models.CharField(db_column='Languages', max_length=50, blank=True, null=True)  # Field name made lowercase.
    credit = models.IntegerField(db_column='Credit', blank=True, null=True)  # Field name made lowercase.
    size = models.IntegerField(db_column='Size', blank=True, null=True)  # Field name made lowercase.
    p1 = models.IntegerField(db_column='P1', blank=True, null=True)  # Field name made lowercase.
    p2 = models.IntegerField(db_column='P2', blank=True, null=True)  # Field name made lowercase.
    p3 = models.IntegerField(db_column='P3', blank=True, null=True)  # Field name made lowercase.
    p4 = models.IntegerField(db_column='P4', blank=True, null=True)  # Field name made lowercase.
    p5 = models.IntegerField(db_column='P5', blank=True, null=True)  # Field name made lowercase.
    total = models.IntegerField(db_column='Total', blank=True, null=True)  # Field name made lowercase.
    curriculumid = models.IntegerField(db_column='Curriculumid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Course'


class Curriculum(models.Model):
    name = models.CharField(db_column='Name', max_length=30, blank=True, null=True)  # Field name made lowercase.
    degreeprogramid = models.IntegerField(db_column='DegreeProgramid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Curriculum'


class Degreeprogram(models.Model):
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', unique=True, max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DegreeProgram'


class Implementation(models.Model):
    courseid = models.IntegerField(db_column='Courseid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Implementation'


class Person(models.Model):
    code = models.CharField(db_column='Code', unique=True, max_length=7)  # Field name made lowercase.
    name = models.CharField(db_column='Name', unique=True, max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Person'


class PersonDegreeprogram(models.Model):
    personid = models.IntegerField(db_column='Personid', primary_key=True)  # Field name made lowercase.
    degreeprogramid = models.IntegerField(db_column='DegreeProgramid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Person_DegreeProgram'
        unique_together = (('personid', 'degreeprogramid'),)


class PersonImplementation(models.Model):
    personid = models.IntegerField(db_column='Personid', primary_key=True)  # Field name made lowercase.
    implementationid = models.IntegerField(db_column='Implementationid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Person_Implementation'
        unique_together = (('personid', 'implementationid'),)


class Room(models.Model):
    topic = models.CharField(db_column='Topic', max_length=50, blank=True, null=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', unique=True, max_length=50)  # Field name made lowercase.
    seats = models.IntegerField(db_column='Seats', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Room'


class RoomImplementation(models.Model):
    roomid = models.IntegerField(db_column='Roomid', primary_key=True)  # Field name made lowercase.
    implementationid = models.IntegerField(db_column='Implementationid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Room_Implementation'
        unique_together = (('roomid', 'implementationid'),)


class Subgroup(models.Model):
    code = models.CharField(db_column='Code', max_length=20, blank=True, null=True)  # Field name made lowercase.
    department = models.CharField(db_column='Department', max_length=30, blank=True, null=True)  # Field name made lowercase.
    groupid = models.IntegerField(db_column='Groupid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SubGroup'


class SubgroupImplementation(models.Model):
    subgroupid = models.IntegerField(db_column='SubGroupid', primary_key=True)  # Field name made lowercase.
    implementationid = models.IntegerField(db_column='Implementationid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SubGroup_Implementation'
        unique_together = (('subgroupid', 'implementationid'),)
