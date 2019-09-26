from django.shortcuts import render
from django.core.serializers.json import DjangoJSONEncoder
from django.views.decorators.csrf import csrf_exempt
import datetime

# Create your views here.

from django.http import HttpResponse

import pyodbc
import json
from django.core import serializers

def db():
    return pyodbc.connect(  'Driver={SQL Server};'
                        'Server=NAVEEN\\MSSQLSERVER_2016;'
                        'Database=Python;'
                        'USER = sa;'
                        'PASSWORD= 12345;'
                        'Trusted_Connection=false;')

def query_read(query, args=(), one=False):
    cur = db().cursor()
    cur.execute(query, args)
    r = [dict((cur.description[i][0], value) \
               for i, value in enumerate(row)) for row in cur.fetchall()]
    cur.connection.close()
    return (r[0] if r else None) if one else r

def query_exec(query, args=(), one=False):
    cur = db().cursor()
    cur.execute(query, args)
    cur.connection.commit()
    cur.connection.close()
    return 1

@csrf_exempt
def create(request):
    if request.method == 'POST':
        now = datetime.datetime.utcnow()
        reqbody = request.body
        jsonObj = json.loads(reqbody)

        my_query = query_exec("insert into employee(EmployeeName,Age,DateOfBirth,EmailID,MobileNumber,Address,City,State,IsActive,CreatedDateTime,CreatedBy) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (jsonObj['EmployeeName'],jsonObj['Age'],jsonObj['DateOfBirth'],jsonObj['EmailID'],jsonObj['MobileNumber'],jsonObj['Address'],jsonObj['City'],jsonObj['State'], 1, now.strftime('%Y-%m-%d %H:%M:%S'), 'Test'))
        
        return HttpResponse("[{'Code':1,'Message':'Saved successfully'}]")
    else:
        return HttpResponse("[{'Code':0,'Message':'Invalid request'}]")


    # conn = pyodbc.connect(  'Driver={SQL Server};'
    #                     'Server=NAVEEN\\MSSQLSERVER_2016;'
    #                     'Database=Python;'
    #                     'USER = sa;'
    #                     'PASSWORD= 12345;'
    #                     'Trusted_Connection=false;')
    # cursor = conn.cursor()
    # data = cursor.execute('select EmployeeID,EmployeeName,Age,EmailID,MobileNumber,Address,City,State,IsActive from Employee for json auto').fetchall()
    # return json.dumps( [dict(ix) for ix in cursor] ) #CREATE JSON
    # return HttpResponse(json.dumps([tuple(row) for row in data]))
    # return HttpResponse(data)

@csrf_exempt
def read(request):
    my_query = query_read("select * from Employee")
    json_output = json.dumps(my_query, sort_keys=True, indent=1, cls=DjangoJSONEncoder)
    return HttpResponse(json_output)

@csrf_exempt
def update(request):
    if request.method == 'POST':
        now = datetime.datetime.utcnow()
        reqbody = request.body
        jsonObj = json.loads(reqbody)

        my_query = query_exec("update employee set EmployeeName = ?,Age = ? ,DateOfBirth = ?,EmailID = ?,MobileNumber = ?,Address = ?,City = ?,State = ?, ModifiedDateTime =?, ModifiedBy=? where EmployeeID = ?", (jsonObj['EmployeeName'],jsonObj['Age'],jsonObj['DateOfBirth'],jsonObj['EmailID'],jsonObj['MobileNumber'],jsonObj['Address'],jsonObj['City'],jsonObj['State'], now.strftime('%Y-%m-%d %H:%M:%S'), 'Test', jsonObj['EmployeeID']))
        
        return HttpResponse("[{'Code':1,'Message':'Updated successfully'}]")
    else:
        return HttpResponse("[{'Code':0,'Message':'Invalid request'}]")

@csrf_exempt
def delete(request):
    if request.method == 'POST':
        reqbody = request.body
        jsonObj = json.loads(reqbody)

        my_query = query_exec("delete from employee where EmployeeID = ?", (jsonObj['EmployeeID']))
        
        return HttpResponse("[{'Code':1,'Message':'Deleted successfully'}]")
    else:
        return HttpResponse("[{'Code':0,'Message':'Invalid request'}]")