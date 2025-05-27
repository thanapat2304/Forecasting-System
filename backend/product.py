from flask import render_template, session, request
from backend.db_connection import connect_aep_DB, connect_aep_portal
from datetime import datetime
import pandas as pd
import random

def import_product():
    current_user = 'admin'
    brands = get_brand_all()
    year = get_years()

    results = None
    selected_brands = None
    selected_year = None
    
    if request.method == 'POST':
        selected_brands = request.form.get('brands')
        selected_year = request.form.get('year')

    results = process_master_mat(selected_brands, selected_year)

    return render_template('product.html', current_user=current_user, brands=brands, year=year, results=results, selected_brands=selected_brands, selected_year=selected_year)

def get_brand_all():
    return ['BrandX', 'BrandY', 'BrandZ', 'BrandA', 'BrandB']

def get_years():
    current_year = datetime.now().year
    start_year = current_year - 2
    years = [{'id': str(year), 'AS_Name_year': str(year)} for year in range(current_year, start_year - 1, -1)]
    return years

def forecast_mat(selected_brands, selected_year):
    sample_brands = ['BRAND_A', 'BRAND_B', 'BRAND_C']
    sample_products = [
        ('MAT001', 'Product A'),
        ('MAT002', 'Product B'),
        ('MAT003', 'Product C'),
        ('MAT004', 'Product D')
    ]
    uoms = ['PCS', 'BOX', 'PACK']

    if selected_brands != 'ALL':
        brands = [selected_brands]
    else:
        brands = sample_brands

    if selected_year != 'ALL':
        years = list(range(2022, 2026))
    else:
        years = [int(selected_year)]

    results = []
    for year in years:
        for month in range(1, 13):
            for brand in brands:
                for matno, matdesc in sample_products:
                    qty = random.randint(100, 1000)
                    uom = random.choice(uoms)
                    results.append((
                        year,
                        month,
                        matno,
                        matdesc,
                        brand,
                        uom,
                        qty
                    ))

    return results

def process_master_mat(selected_brands, selected_year):
    df = forecast_mat(selected_brands, selected_year)
    raw_data = pd.DataFrame(df) if df else pd.DataFrame()

    if raw_data.empty:
        return []
    
    raw_data.columns = ['year', 'month', 'product_code', 'product_name', 'brand', 'unit', 'quantity']

    pivot_df = raw_data.pivot_table(
        index=['product_code', 'product_name', 'brand', 'unit'],
        columns=['month'],
        values='quantity',
        aggfunc='sum'
    ).reset_index()

    all_months = range(1, 13)

    for month in all_months:
        if month not in pivot_df.columns:
            pivot_df[month] = 0

    pivot_df = pivot_df[['product_code', 'product_name', 'brand', 'unit'] + list(all_months)]

    stacked_pivot = pivot_df.fillna(0)

    cols_to_format = stacked_pivot.columns[4:]

    for col in cols_to_format:  
        stacked_pivot[col] = stacked_pivot[col].apply(
            lambda x: int(x) if x == int(x) else round(x, 2)
        )

    list_data = []
    for _, row in stacked_pivot.iterrows():
        list_row = [
            row['product_code'],
            row['product_name'],
            row['brand'],
            row['unit']
        ]

        for month in range(1, 13):
            value = row.get(month, 0)
            if isinstance(value, int) or value == int(value):
                formatted_value = f"{int(value):,}"
            else:
                formatted_value = str(value)
            list_row.append(formatted_value)
        list_data.append(list_row)

    return list_data