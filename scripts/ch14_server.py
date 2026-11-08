# -*- coding: utf-8 -*-
"""14장 측정 서버(14.2·14.3절 코드 모음). 실행: uvicorn ch14_server:app --port 8620"""
from fastapi import FastAPI
from pydantic import BaseModel, Field
from statistics import median

class Measure(BaseModel):
    node_id: str = Field(min_length=1, max_length=16)   # 기기 번호
    zone: str = Field(pattern=r"^D[1-4]$")              # 측정 지점 D1~D4
    rssi: int = Field(ge=-100, le=0)                    # 신호 세기(dBm)

app = FastAPI(title="piDocs 측정 서버")
records = []                                   # 수신 기록(서버를 다시 실행하면 초기화)

@app.post("/measure")
def post_measure(m: Measure):
    records.append(m.model_dump())             # 모델 → 딕셔너리
    return {"ok": True, "count": len(records)}

@app.get("/summary")
def get_summary():
    zones = sorted({r["zone"] for r in records})
    return {z: {"count": sum(1 for r in records if r["zone"] == z),
                "median": median(r["rssi"] for r in records if r["zone"] == z)}
            for z in zones}

# judge.py: 7.1절 지점별 분위수 기준(11/4 수업 기록)
THRESH = {"D1": (-62.0, -56.0), "D2": (-77.0, -74.0),
          "D3": (-68.0, -66.0), "D4": (-73.3, -69.0)}   # (10% 분위수, 25% 분위수)

def judge_rssi(zone, v):
    """지점별 분위수 기준으로 신호 세기를 3단계 판정한다."""
    q10, q25 = THRESH[zone]
    if v < q10:
        return "경고"
    if v < q25:
        return "주의"
    return "정상"


@app.post("/judge")
def post_judge(m: Measure):
    level = judge_rssi(m.zone, m.rssi)
    records.append({**m.model_dump(), "level": level})
    return {"ok": True, "level": level}

