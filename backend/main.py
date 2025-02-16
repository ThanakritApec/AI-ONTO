from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from rdflib import Graph, Namespace
import unicodedata

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def load_ontology_data():
    try:
        g = Graph()
        g.parse("mytourism.owl", format="xml")
        mytourism = Namespace("http://www.my_ontology.edu/mytourism#")
        
        data = []
        # สร้าง dictionary เพื่อเก็บข้อมูลชื่อจังหวัดและชื่อดั้งเดิม
        province_names_map = {}
        traditional_names_map = {}
        
        # รอบแรก: เก็บชื่อจังหวัดและชื่อดั้งเดิม
        for subj, pred, obj in g:
            pred_label = str(pred).replace(str(mytourism), "mytourism:")
            province = str(subj).replace(str(mytourism), "mytourism:")
            
            if "hasNameOfProvince" in pred_label:
                if province not in province_names_map:
                    province_names_map[province] = []
                province_names_map[province].append(str(obj))
                
            if "hasTraditionalNameOfProvince" in pred_label:
                if province not in traditional_names_map:
                    traditional_names_map[province] = []
                traditional_names_map[province].append(str(obj))

        # รอบที่สอง: สร้างข้อมูลหลักพร้อมชื่อจังหวัดและชื่อดั้งเดิม
        for subj, pred, obj in g:
            subj_label = str(subj).replace(str(mytourism), "mytourism:")
            pred_label = str(pred).replace(str(mytourism), "mytourism:")
            
            if isinstance(obj, Namespace) or str(obj).startswith("http"):
                obj_label = str(obj).replace(str(mytourism), "mytourism:")
            else:
                obj_label = str(obj)

            if "owl#" not in obj_label:
                item = {
                    "subject": subj_label,
                    "predicate": pred_label,
                    "object": obj_label,
                }
                # เพิ่มชื่อจังหวัด
                if subj_label in province_names_map:
                    item["province_names"] = province_names_map[subj_label]
                # เพิ่มชื่อดั้งเดิม
                if subj_label in traditional_names_map:
                    item["traditional_names"] = traditional_names_map[subj_label]
                data.append(item)
                
        print("✅ OWL Data Loaded:", len(data), "items")
        return data
    except Exception as e:
        print(f"❌ Error loading OWL file: {e}")
        return []

ontology_data = load_ontology_data()

@app.get("/search")
def search_ontology(query: str):
    query = normalize(query.strip().lower())
    print(f"🔍 ค้นหา: {query}")
    
    results = []
    for item in ontology_data:
        # ค้นหาในทุกฟิลด์ รวมถึงชื่อจังหวัดและชื่อดั้งเดิม
        if (query in normalize(item["subject"].lower()) or 
            query in normalize(item["object"].lower()) or
            any(query in normalize(name.lower()) 
                for name in item.get("province_names", [])) or
            any(query in normalize(trad_name.lower()) 
                for trad_name in item.get("traditional_names", []))):
            results.append(item)
    
    # ถ้าไม่พบผลลัพธ์ ให้ค้นหาใน Uthaithani
    if not results:
        results = [
            item for item in ontology_data 
            if "Uthaithani" in item["subject"] or 
               "Uthaithani" in item["object"]
        ]
    
    print(f"✅ ผลลัพธ์ที่พบ: {len(results)} รายการ")
    if results:
        for item in results[:5]:
            print(f"🔹 Subject: {item['subject']} | Object: {item['object']}")
            # แสดงชื่อจังหวัดถ้ามี
            if "province_names" in item:
                print(f"  Province names: {item['province_names']}")
    
    return {"results": results}

def normalize(text):
    return unicodedata.normalize("NFKC", text).lower()