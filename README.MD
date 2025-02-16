
# การใช้งานโปรเจค

โปรเจคนี้เป็นตัวอย่างการค้นหาข้อมูลจากไฟล์ OWL โดยใช้ FastAPI และ React.js. 

## สิ่งที่ต้องเตรียม

1. **ติดตั้ง Python และไลบรารีที่จำเป็น**
   - ติดตั้ง Python 3.7 ขึ้นไป
   - ติดตั้งไลบรารีที่จำเป็นโดยใช้คำสั่ง:
     ```bash
     cd backend
     pip install -r requirements.txt
     ```

2. **ติดตั้ง Node.js และ React Dependencies**
   - ติดตั้ง [Node.js](https://nodejs.org/) (แนะนำให้ใช้เวอร์ชัน LTS)
   - ติดตั้ง dependencies ของ React ด้วยคำสั่ง:
     ```bash
     cd frontend
     npm install
     ```

3. **ไฟล์ OWL**
   - โปรเจคนี้ใช้ไฟล์ `mytourism.owl` ที่ต้องมีอยู่ในโฟลเดอร์เดียวกับโปรเจค.
   - ตรวจสอบให้แน่ใจว่าไฟล์ `mytourism.owl` อยู่ในไดเรกทอรีเดียวกับไฟล์โปรเจค.

## วิธีการใช้งาน

1. **เริ่มต้น FastAPI server**
   - หลังจากติดตั้งไลบรารีทั้งหมดแล้ว ให้รัน FastAPI server โดยใช้คำสั่ง:
     ```bash
     cd backend
     uvicorn main:app --reload
     ```
   - FastAPI จะเริ่มทำงานที่ `http://127.0.0.1:8000`.

2. **เริ่มต้น React application**
   - รัน React app ด้วยคำสั่ง:
     ```bash
     cd frontend
     npm start
     ```
   - React app จะเริ่มทำงานที่ `http://localhost:5173`.

3. **การค้นหาข้อมูล**
   - คุณสามารถค้นหาข้อมูลเกี่ยวกับจังหวัดในประเทศไทยโดยการพิมพ์ชื่อจังหวัดในช่องค้นหาของแอปพลิเคชัน React.
   - ระบบจะค้นหาข้อมูลจากไฟล์ OWL และแสดงผลที่ตรงกับคำค้น.

## โครงสร้างโปรเจค

- `main.py`: ไฟล์ที่ใช้ในการสร้าง FastAPI server และโหลดข้อมูลจากไฟล์ OWL.
- `mytourism.owl`: ไฟล์ OWL ที่ใช้ในการเก็บข้อมูล.
- `frontend/`: โฟลเดอร์ที่เก็บ React application.
  - `App.jsx`: ส่วนของ React ที่แสดงอินเตอร์เฟซการค้นหาข้อมูล.
  - `package.json`: ไฟล์ที่ใช้ในการจัดการ dependencies ของ React.
- `requirements.txt`: ไฟล์ที่ใช้ในการติดตั้งไลบรารีของ Python.


