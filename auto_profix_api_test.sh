#!/bin/bash

# --- CONFIGURATION ---
COLLECTION="Profix API.postman_collection.json"
ENVIRONMENT="Profix_Dev.postman_environment.json"
REPORT_DIR="./Reports"
NEWMAN="./node_modules/.bin/newman"
SCRIPTS_DIR=".agent/skills/api_automation_expert/scripts"

echo "🚀 BAT DAU QUY TRINH AUTOMATION API PROFIX..."

# STEP 1: Injection & Flattening (Dung Python)
echo "1. Dang chen kịch bản automation va lam phang Collection..."
python3 /tmp/inject_postman_tests.py
python3 /tmp/flatten_postman.py

# STEP 2: Run Newman
echo "2. Dang thuc thi bo test bang Newman..."
mkdir -p $REPORT_DIR
$NEWMAN run Profix_API_Flattened.postman_collection.json \
    -e "$ENVIRONMENT" \
    -r htmlextra,json \
    --reporter-json-export "$REPORT_DIR/summary.json" \
    --reporter-htmlextra-export "$REPORT_DIR/Profix_Report.html" \
    --reporter-htmlextra-title "Bao cao Automation API ProfiX"

# STEP 3: Analysis & Assessment
echo "3. Dang phan tich loi (Root Cause Analysis)..."
python3 $SCRIPTS_DIR/parse_newman_errors.py

echo "-------------------------------------------------------"
echo "✅ HOAN TAT! Ket qua tai:"
echo "   - Bao cao HTML: $REPORT_DIR/Profix_Report.html"
echo "   - Ban danh gia loi: $REPORT_DIR/API_Error_Assessment.md"
echo "-------------------------------------------------------"

# Optional: Mo bao cao HTML tu dong (Chi cho Mac)
if [[ "$OSTYPE" == "darwin"* ]]; then
    open "$REPORT_DIR/Profix_Report.html"
fi
