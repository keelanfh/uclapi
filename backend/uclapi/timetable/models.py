from django.db import models

# Create your models here.
# CREATE TABLE CMIS_OWNER.CLASSGRPS
# (
#   SETID VARCHAR2(10 CHAR)
# , CLASSGROUPID VARCHAR2(10 CHAR)
# , COURSEID VARCHAR2(12 CHAR)
# , GRPCODE VARCHAR2(10 CHAR)
# , CRSYEAR NUMBER(*, 0)
# , NAME VARCHAR2(25 CHAR)
# , CSIZE NUMBER(*, 0)
# , MINSIZE NUMBER(*, 0)
# , MAXSIZE NUMBER(*, 0)
# , PREFMAXSIZE NUMBER(*, 0)
# , LINKCODE VARCHAR2(20 CHAR)
# , ESTSIZE NUMBER(*, 0)
# , THISKEY NUMBER(*, 0)
# , PARENTKEY NUMBER(*, 0)
# , GROUPNUM NUMBER(*, 0)
# , CEQUIVID NUMBER(*, 0)
# , YEAR NUMBER(*, 0)
# )


class TimeTable(models.Model):
    slotid = models.BigIntegerField(primary_key=True)
    setid = models.CharField(max_length=40, blank=True, null=True)
    classgroupid = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "TIMETABLE"
        _DATABASE = 'roombookings'
