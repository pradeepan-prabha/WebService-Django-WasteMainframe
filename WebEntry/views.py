import base64

import pymysql
from django.shortcuts import render
import uuid
from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json
import time
import datetime


# Create your views here.
@api_view(["GET"])
def Jsonsplit(data):
    try:
        received_json_data = json.loads(data.body)
        # print(str(received_json_data))
        source_type_val = received_json_data['source_type']
        waste_type_val = received_json_data['waste_type']
        loc_type_val = received_json_data['loc_type']
        img_raw_val = received_json_data['img_raw']
        img_processed_val = received_json_data['img_processed']
        time_date_val = received_json_data['time_date']
        waste_char_val = received_json_data['waste_char']
        waste_shape_val = received_json_data['waste_shape']
        waste_status_val = received_json_data['waste_status']
        waste_prod_name_val = received_json_data['waste_prod_name']
        waste_prod_address_val = received_json_data['waste_prod_address']
        other_val = received_json_data['other']
        latitude_val = received_json_data['latitude']
        longitude_val = received_json_data['longitude']
        country_val = received_json_data['country']
        state_val = received_json_data['state']
        district_val = received_json_data['district']
        region_val = received_json_data['region']
        city_val = received_json_data['city']
        street_val = received_json_data['street']
        pincode_val = received_json_data['pincode']

        print(str(source_type_val))
        print(str(waste_type_val))
        print(str(loc_type_val))
        print(str(img_raw_val))
        print(str(img_processed_val))
        print(str(time_date_val))
        print(str(waste_char_val))
        print(str(waste_shape_val))
        print(str(waste_status_val))
        print(str(waste_prod_name_val))
        print(str(waste_prod_address_val))
        print(str(other_val))
        print(str(latitude_val))
        print(str(longitude_val))
        print(str(country_val))
        print(str(state_val))
        print(str(district_val))
        print(str(region_val))
        print(str(city_val))
        print(str(street_val))
        print(str(pincode_val))
        return JsonResponse("done", safe=False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def Databasecon(data):
    try:
        print(str(json.loads(data.body)['refid']))

        # Open database connection
        db = pymysql.connect("localhost", "root", "", "waste_mainframe_db")

        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        #         sql = """INSERT INTO EMPLOYEE(refid,
        # waste_type,
        # loc_type,
        # img_raw_url,
        # img_processed_url,
        # time_date,
        # waste_char,
        # waste_shape,
        # waste_status,
        # )VALUES (1,1,2,'L3yetLycKOvehsluDinJ8u40AOX26Dim7fvU','L3yetLycKOvehsluDinJ8u40AOX26Dim7fvU',
        # 2019-05-08 15:19:23,2,5,35,3)"""
        received_json_data = "'{}'".format(str(json.loads(data.body)['refid']))

        sql = """INSERT INTO testnew(number)VALUES (%s)"""
        print(sql)
        try:
            # Execute the SQL command
            cursor.execute(sql, str(json.loads(data.body)['refid']))
            print(sql)
            # Commit your changes in the database
            db.commit()
        except:
            print("**************Rollback***************")

            # Rollback in case there is any error
            db.rollback()

        # execute SQL query using execute() method.
        cursor.execute("SELECT VERSION()")

        # Fetch a single row using fetchone() method.
        data = cursor.fetchone()
        print("Database version : %s " % data)

        # disconnect from server
        db.close()

        return JsonResponse(sql, safe=False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def imageDB(data1):
    try:
        received_json_data = json.loads(data1.body)
        # print(str(received_json_data))
        # refid_val = received_json_data['refid']
        source_type_val = received_json_data['source_type']
        waste_type_val = received_json_data['waste_type']
        loc_type_val = received_json_data['loc_type']
        img_raw_val = received_json_data['img_raw']
        img_processed_val = received_json_data['img_processed']
        time_date_val = received_json_data['time_date']
        waste_char_val = received_json_data['waste_char']
        waste_shape_val = received_json_data['waste_shape']
        waste_status_val = received_json_data['waste_status']
        waste_prod_name_val = received_json_data['waste_prod_name']
        waste_prod_address_val = received_json_data['waste_prod_address']
        other_val = received_json_data['other']
        latitude_val = received_json_data['latitude']
        longitude_val = received_json_data['longitude']
        country_val = received_json_data['country']
        state_val = received_json_data['state']
        district_val = received_json_data['district']
        region_val = received_json_data['region']
        city_val = received_json_data['city']
        street_val = received_json_data['street']
        pincode_val = received_json_data['pincode']
        on_progress_val = received_json_data['on_progress']
        waste_fun_status = 1

        # print(str(source_type_val))
        # print(str(waste_type_val))
        # print(str(loc_type_val))
        # print(str(img_raw_val))
        # print(str(img_processed_val))
        # print(str(time_date_val))
        # print(str(waste_char_val))
        # print(str(waste_shape_val))
        # print(str(waste_status_val))
        # print(str(waste_prod_name_val))
        # print(str(waste_prod_address_val))
        # print(str(other_val))
        # print(str(latitude_val))
        # print(str(longitude_val))
        # print(str(country_val))
        # print(str(state_val))
        # print(str(district_val))
        # print(str(region_val))
        # print(str(city_val))
        # print(str(street_val))
        # print(str(pincode_val))
        # print(str(on_progress_val))
        # return JsonResponse("done", safe=False)

        ts = time.time()
        timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        img_raw_val = imageProcess(img_raw_val, timestamp)

        # Open database connection
        db = pymysql.connect("localhost", "root", "", "waste_mainframe_db")

        # prepare a cursor object using cursor() method
        cursor = db.cursor()

        sql_max_val = """select max(refid) from waste_details"""

        sql_waste_details = """INSERT INTO waste_details(refid, waste_type, loc_type, img_raw_url, img_processed_url, time_date, waste_char, waste_shape, waste_status, waste_fun_status, source_type, on_progress) 
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

        sql_product_details = """insert into waste_product_details(refid, waste_prod_name, waste_prod_address, other) 
        values(%s,%s,%s,%s);"""
        # sql_location_details ="""insert into waste_location_details(refid,latitude,longitude,country,state,district,region,city,street,pincode)
        # values(1,12.1231234,34.123313,'india','tamilnadu','kanchipuram','dfse','asdd','sdfe',601239);"""
        sql_location_details = """insert into waste_location_details(refid,latitude,longitude,country,state,district,region,city,street,pincode) 
        values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"""

        print(sql_max_val)

        try:
            cursor.execute(sql_max_val)

            rows = cursor.fetchall()

            refid_val = 0
            for row in rows:
                if str(row[0]) == "null" or str(row[0]) == "None":
                    refid_val = 1
                else:
                    refid_val = row[0] + 1

            print(refid_val)

            cursor.execute(sql_waste_details, (
                str(refid_val), str(waste_type_val), str(loc_type_val), str(img_raw_val), str(img_processed_val),
                str(timestamp), str(waste_char_val), str(waste_shape_val), str(waste_status_val), str(waste_fun_status),
                str(source_type_val), str(on_progress_val)))

            cursor.execute(sql_product_details, (str(refid_val), str(waste_prod_name_val), str(waste_prod_address_val),
                                                 str(other_val)))
            cursor.execute(sql_location_details, (str(refid_val), str(latitude_val), str(longitude_val),
                                                  str(country_val), str(state_val), str(district_val), str(region_val),
                                                  str(city_val), str(street_val), str(pincode_val)))

            print(sql_waste_details)
            print(sql_product_details)
            # Commit your changes in the database
            db.commit()
        except:
            print("**************Rollback***************")

            # Rollback in case there is any error
            db.rollback()

        # execute SQL query using execute() method.
        cursor.execute("SELECT VERSION()")

        # Fetch a single row using fetchone() method.
        data = cursor.fetchone()
        print("Database version : %s " % data)

        # disconnect from server
        db.close()

        # return JsonResponse("done", safe=False)
        return JsonResponse(sql_waste_details, safe=False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)

    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)


def imageProcess(img_base_64, timestamp):
    from django.core.files.base import ContentFile
    format, imgstr = str(img_base_64).split(';base64,')
    ext = format.split('/')[-1]

    data = ContentFile(base64.b64decode(imgstr), 'temp.' + ext)  # You can save this as file instance.
    path = 'WasteRawImage/'+str(uuid.uuid4()) + '.jpg'
    print(path)
    with open(path, "wb") as fh:
        fh.write(base64.b64decode(imgstr))
    return path
