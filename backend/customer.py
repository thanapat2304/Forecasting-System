from flask import render_template, session, request
from backend.db_connection import connect_aep_DB, connect_aep_portal
from datetime import datetime
import pandas as pd
from backend.product import get_years
import random

def import_customer():
    current_user = 'admin'
    year = get_years()
    product = get_product()
    month = get_month()

    results = None
    chart_data = {"labels": [], "data": []}
    selected_product = None
    selected_month = None
    selected_year = None
    total_sum = 0
    distinct_count = 0
    
    if request.method == 'POST':
        selected_product = request.form.get('product')
        selected_month = request.form.get('month')
        selected_year = request.form.get('year')

        parts_product = [p.strip() for p in selected_product.split(' | ')]
        product_code = parts_product[0]

        results = get_data(product_code, selected_month, selected_year)
        chart_data = process_master_mat(results)

        total_sum = sum(row[2] for row in results) if results else 0

        distinct_count = len(set(row[2] for row in results)) if results else 0

    return render_template('customer.html', current_user=current_user, results=results, selected_product=selected_product, selected_year=selected_year, year=year, product=product, month=month,
                           selected_month=selected_month, chart_data=chart_data, total_sum=total_sum, distinct_count=distinct_count)

def get_product():
    # สร้างรายการรหัสสินค้าและชื่อสินค้าแบบมั่วๆ
    products = [
        ('MAT001', 'สินค้า A'),
        ('MAT002', 'สินค้า B'),
        ('MAT003', 'สินค้า C'),
        ('MAT004', 'สินค้า D'),
        ('MAT005', 'สินค้า E')
    ]

    # รวม MATNO และ MATDESC ตามฟอร์แมตที่ SQL ใช้
    product_list = [f"{matno} | {desc}" for matno, desc in products]

    return product_list

def get_month():
    return [
        "1 | Jan",
        "2 | Feb",
        "3 | Mar",
        "4 | Apr",
        "5 | May",
        "6 | Jun",
        "7 | Jul",
        "8 | Aug",
        "9 | Sep",
        "10 | Oct",
        "11 | Nov",
        "12 | Dec"
    ]

def get_data(product_code, selected_month, selected_year):
    # รายชื่อลูกค้าและผู้สร้าง mock
    customers = [
        ('CUST001', 'ลูกค้า A'),
        ('CUST002', 'ลูกค้า B'),
        ('CUST003', 'ลูกค้า C'),
        ('CUST004', 'ลูกค้า D')
    ]
    created_bys = ['admin', 'user1', 'user2']

    # สร้าง mock data
    results = []
    for cust_code, cust_name in customers:
        if product_code == 'ALL' or product_code in ['MAT001', 'MAT002', 'MAT003']:
            forecast_value = random.randint(100, 1000)
            created_by = random.choice(created_bys)
            results.append((
                cust_code,         # doc_customer
                cust_name,         # name_customer
                forecast_value,    # forecast_value
                created_by         # created_by
            ))

    return results

def process_master_mat(results):
    raw_data = pd.DataFrame(results) if results else pd.DataFrame()

    if raw_data.empty:
        return {"labels": [], "data": []}

    summary = raw_data.groupby(3)[2].sum().reset_index()

    labels = summary[3].tolist()
    data = summary[2].tolist()

    return {"labels": labels, "data": data}