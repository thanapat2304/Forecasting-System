# Forecasting System

ระบบพยากรณ์ยอดขาย (Forecasting System) เป็นแอปพลิเคชันเว็บที่พัฒนาด้วย Python Flask สำหรับการจัดการและพยากรณ์ยอดขาย

## คุณสมบัติหลัก (Features)

- 🔐 ระบบล็อกอินและการจัดการผู้ใช้
- 📊 การนำเข้าข้อมูลสินค้า
- 👥 การจัดการข้อมูลลูกค้า
- 📈 การพยากรณ์ยอดขาย
- 🔄 การจัดการเซสชัน (Session Management)

## การติดตั้ง (Installation)

1. ติดตั้ง Python 3.x
2. Clone repository นี้:
```bash
git clone https://github.com/thanapat2304/Forecasting-System.git
cd Forecasting-System
```

3. ติดตั้ง dependencies:
```bash
pip install -r requirements.txt
```

## การใช้งาน (Usage)

1. รันแอปพลิเคชัน:
```bash
python app.py
```

2. เปิดเว็บเบราว์เซอร์และไปที่:
```
http://localhost:8080
```

## โครงสร้างโปรเจค (Project Structure)

```
Forecasting-System/
├── app.py              # แอปพลิเคชันหลัก
├── backend/            # โค้ดส่วน Backend
├── static/            # ไฟล์ Static (CSS, JavaScript, Images)
├── templates/         # ไฟล์ HTML Templates
└── requirements.txt   # รายการ Python dependencies
```

## การตั้งค่าระบบ (Configuration)

- Port: 8080 (default)
- Host: 0.0.0.0 (สามารถเข้าถึงได้จากทุก IP)
- Session timeout: 30 นาที

## ความต้องการของระบบ (Requirements)

- Python 3.x
- Flask
- เว็บเบราว์เซอร์ที่ทันสมัย (Chrome, Firefox, Safari, Edge)

## การรักษาความปลอดภัย (Security)

- ระบบมีการเข้ารหัสเซสชัน
- การยืนยันตัวตนผู้ใช้ผ่านระบบล็อกอิน
- การป้องกันการเข้าถึงหน้าที่ไม่ได้รับอนุญาต

## 👨‍💻 ผู้พัฒนา

**ธนภัทร โสภณ**